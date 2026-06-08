import sys

from syntaxchecker.syntax_checker import SyntaxChecker
from typechecker.type_checker import MiniGoTypeChecker

from pathlib import Path
from encoder.llvm_generator import MiniGoLLVMGenerator


class MiniGoCompiler:
    def __init__(self, source_file):
        self.source_file = source_file
        self.syntax_result = None
        self.type_result = None

    def compile(self):
        print("=== MiniGo Compiler ===")
        print(f"Archivo fuente: {self.source_file}")
        print()

        if not self._run_syntax_analysis():
            return

        if not self._run_code_generation():
            return

        if not self._run_type_checking():
            return

        print("Compilación finalizada correctamente hasta fase semántica.")

    def _run_syntax_analysis(self):
        print("[1] Ejecutando análisis sintáctico...")

        syntax_checker = SyntaxChecker(self.source_file)
        self.syntax_result = syntax_checker.analyze()

        if self.syntax_result.has_errors():
            print("Errores sintácticos encontrados:")
            self.syntax_result.print_errors()
            return False

        print("Análisis sintáctico correcto.")
        print("Árbol generado correctamente.")
        print()
        return True

    def _run_type_checking(self):
        print("[2] Ejecutando análisis semántico...")

        type_checker = MiniGoTypeChecker()
        self.type_result = type_checker.check(self.syntax_result.tree)

        if self.type_result.has_errors():
            print("Errores semánticos encontrados:")
            self.type_result.print_errors()
            return False

        print("Análisis semántico inicial correcto.")
        print()
        return True

    def _run_code_generation(self):
        print("[3] Generando LLVM IR...")

        generator = MiniGoLLVMGenerator()
        result = generator.generate(self.syntax_result.tree)

        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "program.ll"
        output_file.write_text(result.llvm_code, encoding="utf-8")

        print(f"LLVM generado en: {output_file}")
        print()
        return True


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("python main.py tests/test01_println.mgo")
        return

    source_file = sys.argv[1]

    compiler = MiniGoCompiler(source_file)
    compiler.compile()


if __name__ == "__main__":
    main()