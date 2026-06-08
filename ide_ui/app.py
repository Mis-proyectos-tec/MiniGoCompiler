from pathlib import Path
import subprocess
import sys

from flask import Flask, render_template, request, jsonify

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from syntaxchecker.syntax_checker import SyntaxChecker
from typechecker.type_checker import MiniGoTypeChecker
from encoder.llvm_generator import MiniGoLLVMGenerator


OUTPUT_DIR = PROJECT_ROOT / "output"
TESTS_DIR = PROJECT_ROOT / "tests"
EDITOR_INPUT_FILE = OUTPUT_DIR / "editor_input.mgo"
LLVM_OUTPUT_FILE = OUTPUT_DIR / "program.ll"
COMPILE_SCRIPT = PROJECT_ROOT / "scripts" / "compile_llvm.bat"

app = Flask(
    __name__,
    template_folder=str(Path(__file__).parent / "templates"),
    static_folder=str(Path(__file__).parent / "static")
)


DEFAULT_CODE = """package main;

func suma(a int, b int) int {
    return a + b;
};

func main() {
    println(`Inicio MiniGo`);

    var x int = 10;
    var y int = 20;
    var r int = suma(x, y);

    println(r);

    if r > 20 {
        println(`Resultado mayor a 20`);
    } else {
        println(`Resultado menor o igual a 20`);
    };

    var nums [3]int;
    nums[0] = 5;
    nums[1] = 10;
    nums[2] = nums[0] + nums[1];

    println(nums[2]);
    println(len(nums));

    for i := 0; i < 3; i++ {
        println(i);
    };

    println(`Fin MiniGo`);
};
"""


def save_source_code(source_code):
    OUTPUT_DIR.mkdir(exist_ok=True)
    EDITOR_INPUT_FILE.write_text(source_code, encoding="utf-8")


def serialize_errors(errors, error_type):
    serialized = []

    for error in errors:
        serialized.append({
            "type": error_type,
            "line": error.line,
            "column": error.column,
            "length": 1,
            "message": error.message
        })

    return serialized


def format_errors(errors):
    if not errors:
        return ""

    lines = []

    for error in errors:
        lines.append(
            f"[{error['type']}] Línea {error['line']}, columna {error['column']}: {error['message']}"
        )

    return "\n".join(lines)


def compile_source(source_code):
    save_source_code(source_code)

    syntax_checker = SyntaxChecker(str(EDITOR_INPUT_FILE))
    syntax_result = syntax_checker.analyze()

    if syntax_result.has_errors():
        errors = serialize_errors(syntax_result.errors, "Sintáctico")

        return {
            "success": False,
            "stage": "syntax",
            "errors": errors,
            "compilerOutput": "Errores sintácticos encontrados:\n" + format_errors(errors),
            "llvmCode": "",
        }

    type_checker = MiniGoTypeChecker()
    type_result = type_checker.check(syntax_result.tree)

    if type_result.has_errors():
        errors = serialize_errors(type_result.errors, "Semántico")

        return {
            "success": False,
            "stage": "semantic",
            "errors": errors,
            "compilerOutput": "Errores semánticos encontrados:\n" + format_errors(errors),
            "llvmCode": "",
        }

    generator = MiniGoLLVMGenerator()
    llvm_result = generator.generate(syntax_result.tree)

    LLVM_OUTPUT_FILE.write_text(llvm_result.llvm_code, encoding="utf-8")

    return {
        "success": True,
        "stage": "llvm",
        "errors": [],
        "compilerOutput": "Compilación correcta.\nLLVM generado en output/program.ll",
        "llvmCode": llvm_result.llvm_code,
    }


def run_generated_program():
    if not COMPILE_SCRIPT.exists():
        return {
            "returncode": 1,
            "stdout": "",
            "stderr": f"No se encontró el script: {COMPILE_SCRIPT}"
        }

    result = subprocess.run(
        [str(COMPILE_SCRIPT)],
        cwd=str(PROJECT_ROOT),
        text=True,
        capture_output=True,
        shell=True
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }

def list_test_files():
    if not TESTS_DIR.exists():
        return []

    files = []

    for path in TESTS_DIR.rglob("*.mgo"):
        relative_path = path.relative_to(TESTS_DIR).as_posix()
        files.append(relative_path)

    return sorted(files)


def safe_test_path(relative_path):
    requested_path = (TESTS_DIR / relative_path).resolve()
    tests_root = TESTS_DIR.resolve()

    if not str(requested_path).startswith(str(tests_root)):
        return None

    if not requested_path.exists() or requested_path.suffix != ".mgo":
        return None

    return requested_path


@app.route("/")
def index():
    return render_template("index.html", default_code=DEFAULT_CODE)


@app.route("/compile", methods=["POST"])
def compile_code():
    data = request.get_json()
    source_code = data.get("code", "")

    result = compile_source(source_code)

    return jsonify({
        "success": result["success"],
        "stage": result["stage"],
        "errors": result["errors"],
        "compilerOutput": result["compilerOutput"],
        "llvmCode": result["llvmCode"],
        "programOutput": ""
    })


@app.route("/compile-run", methods=["POST"])
def compile_and_run_code():
    data = request.get_json()
    source_code = data.get("code", "")

    result = compile_source(source_code)

    if not result["success"]:
        return jsonify({
            "success": False,
            "stage": result["stage"],
            "errors": result["errors"],
            "compilerOutput": result["compilerOutput"],
            "llvmCode": result["llvmCode"],
            "programOutput": ""
        })

    run_result = run_generated_program()

    return jsonify({
        "success": run_result["returncode"] == 0,
        "stage": "execution",
        "errors": [],
        "compilerOutput": result["compilerOutput"],
        "llvmCode": result["llvmCode"],
        "programOutput": run_result["stdout"] + run_result["stderr"]
    })

@app.route("/tests", methods=["GET"])
def get_tests():
    return jsonify({
        "tests": list_test_files()
    })


@app.route("/tests/load", methods=["POST"])
def load_test():
    data = request.get_json()
    relative_path = data.get("path", "")

    test_path = safe_test_path(relative_path)

    if test_path is None:
        return jsonify({
            "success": False,
            "message": "Archivo de prueba no válido.",
            "code": ""
        }), 400

    return jsonify({
        "success": True,
        "path": relative_path,
        "code": test_path.read_text(encoding="utf-8")
    })


if __name__ == "__main__":
    app.run(debug=True)