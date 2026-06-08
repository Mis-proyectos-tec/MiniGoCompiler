let editor;
let currentDecorations = [];

const terminalOutput = document.getElementById("terminalOutput");
const llvmOutput = document.getElementById("llvmOutput");
const statusTag = document.getElementById("statusTag");

const compileBtn = document.getElementById("compileBtn");
const testSelector = document.getElementById("testSelector");
const loadTestBtn = document.getElementById("loadTestBtn");

compileBtn.disabled = true;
loadTestBtn.disabled = true;

require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function () {
    monaco.languages.register({ id: "minigo" });

    monaco.languages.setMonarchTokensProvider("minigo", {
        keywords: [
            "package", "var", "type", "func", "struct",
            "if", "else", "for", "switch", "case", "default",
            "break", "continue", "return",
            "true", "false"
        ],

        typeKeywords: [
            "int", "float64", "string", "rune", "bool"
        ],

        builtins: [
            "print", "println", "len", "cap", "append"
        ],

        operators: [
            "=", ":=", "+", "-", "*", "/", "%",
            "==", "!=", "<", "<=", ">", ">=",
            "&&", "||", "!", "++", "--",
            "+=", "-=", "*=", "/=", "%=",
            "&", "|", "^", "<<", ">>", "&^"
        ],

        symbols: /[=><!~?:&|+\-*\/\^%]+/,

        tokenizer: {
            root: [
                [/[a-zA-Z_]\w*/, {
                    cases: {
                        "@keywords": "keyword",
                        "@typeKeywords": "type",
                        "@builtins": "predefined",
                        "@default": "identifier"
                    }
                }],

                [/[{}()\[\]]/, "@brackets"],
                [/[;,.]/, "delimiter"],

                [/@symbols/, {
                    cases: {
                        "@operators": "operator",
                        "@default": ""
                    }
                }],

                [/\d+\.\d+([eE][\-+]?\d+)?/, "number.float"],
                [/0[xX][0-9a-fA-F_]+/, "number.hex"],
                [/0[bB][01_]+/, "number.binary"],
                [/0[oO][0-7_]+/, "number.octal"],
                [/\d+/, "number"],

                [/`/, "string.raw", "@rawString"],
                [/"/, "string", "@string"],
                [/'([^'\\]|\\.)'/, "string"],

                [/\/\/.*$/, "comment"],
                [/\/\*/, "comment", "@comment"],

                [/\s+/, "white"]
            ],

            rawString: [
                [/[^`]+/, "string.raw"],
                [/`/, "string.raw", "@pop"]
            ],

            string: [
                [/[^\\"]+/, "string"],
                [/\\./, "string.escape"],
                [/"/, "string", "@pop"]
            ],

            comment: [
                [/[^\/*]+/, "comment"],
                [/\/\*/, "comment", "@push"],
                [/\*\//, "comment", "@pop"],
                [/[\/*]/, "comment"]
            ]
        }
    });

    monaco.languages.setLanguageConfiguration("minigo", {
        comments: {
            lineComment: "//",
            blockComment: ["/*", "*/"]
        },
        brackets: [
            ["{", "}"],
            ["[", "]"],
            ["(", ")"]
        ],
        autoClosingPairs: [
            { open: "{", close: "}" },
            { open: "[", close: "]" },
            { open: "(", close: ")" },
            { open: "`", close: "`" },
            { open: '"', close: '"' },
            { open: "'", close: "'" }
        ]
    });

    editor = monaco.editor.create(document.getElementById("codeEditor"), {
        value: window.DEFAULT_CODE || "",
        language: "minigo",
        theme: "vs-dark",
        automaticLayout: true,
        fontSize: 15,
        minimap: {
            enabled: false
        },
        lineNumbers: "on",
        glyphMargin: true,
        roundedSelection: false,
        scrollBeyondLastLine: true,
        scrollBeyondLastColumn: 8,
        padding: {
            top: 8,
            bottom: 180
        },
        tabSize: 4,
        insertSpaces: true
    });

    compileBtn.disabled = false;
    loadTestBtn.disabled = false;

    loadTestFiles();
});

function clearEditorErrors() {
    if (!editor) return;

    const model = editor.getModel();

    monaco.editor.setModelMarkers(model, "minigo-owner", []);
    currentDecorations = editor.deltaDecorations(currentDecorations, []);
}

function applyEditorErrors(errors) {
    if (!editor) return;

    clearEditorErrors();

    if (!errors || errors.length === 0) {
        return;
    }

    const model = editor.getModel();

    const markers = errors.map(error => {
        const line = Math.max(1, error.line);
        const startColumn = Math.max(1, error.column + 1);
        const endColumn = Math.max(startColumn + 1, startColumn + getErrorLength(error));

        return {
            severity: monaco.MarkerSeverity.Error,
            message: error.message,
            startLineNumber: line,
            startColumn: startColumn,
            endLineNumber: line,
            endColumn: endColumn
        };
    });

    monaco.editor.setModelMarkers(model, "minigo-owner", markers);

    const decorations = errors.map(error => {
        const line = Math.max(1, error.line);

        return {
            range: new monaco.Range(line, 1, line, 1),
            options: {
                isWholeLine: true,
                className: "error-line-highlight",
                glyphMarginClassName: "error-glyph",
                hoverMessage: {
                    value: `**Error:** ${error.message}`
                }
            }
        };
    });

    currentDecorations = editor.deltaDecorations(currentDecorations, decorations);

    const firstError = errors[0];

    editor.revealPositionInCenter({
        lineNumber: firstError.line,
        column: firstError.column + 1
    });

    editor.setPosition({
        lineNumber: firstError.line,
        column: firstError.column + 1
    });

    editor.focus();
}

function getErrorLength(error) {
    if (error.length && error.length > 0) {
        return error.length;
    }

    return 1;
}

function formatErrorList(errors) {
    if (!errors || errors.length === 0) {
        return "";
    }

    return "\n\nErrores detectados:\n" + errors.map(error => {
        return `→ Línea ${error.line}, columna ${error.column}: ${error.message}`;
    }).join("\n");
}

async function sendRequest(endpoint) {
    if (!editor) return;

    compileBtn.disabled = true;
    loadTestBtn.disabled = true;

    clearEditorErrors();

    terminalOutput.textContent = "Compilando...";
    terminalOutput.className = "";
    statusTag.textContent = "compilando";
    statusTag.className = "tag";

    llvmOutput.textContent = "";

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: editor.getValue()
            })
        });

        const data = await response.json();

        applyEditorErrors(data.errors);

        llvmOutput.textContent = data.llvmCode || "No se generó LLVM.";

        if (data.success) {
            terminalOutput.textContent =
                data.programOutput && data.programOutput.trim() !== ""
                    ? data.programOutput.trim()
                    : "Compilación correcta. El programa no imprimió salida.";

            terminalOutput.className = "success";
            statusTag.textContent = "correcto";
            statusTag.className = "tag success";
        } else {
            terminalOutput.textContent =
                (data.compilerOutput || "Error de compilación.") +
                formatErrorList(data.errors);

            terminalOutput.className = "error";
            statusTag.textContent = "error";
            statusTag.className = "tag error";
        }

    } catch (error) {
        terminalOutput.textContent = "Error al comunicarse con Flask:\n" + error;
        terminalOutput.className = "error";
        statusTag.textContent = "error";
        statusTag.className = "tag error";
    } finally {
        compileBtn.disabled = false;
        loadTestBtn.disabled = false;
    }
}

async function loadTestFiles() {
    try {
        const response = await fetch("/tests");
        const data = await response.json();

        testSelector.innerHTML = `<option value="">Cargar archivo de prueba...</option>`;

        data.tests.forEach(testPath => {
            const option = document.createElement("option");
            option.value = testPath;
            option.textContent = testPath;
            testSelector.appendChild(option);
        });

    } catch (error) {
        console.error("No se pudieron cargar las pruebas:", error);
    }
}

async function loadSelectedTest() {
    const selectedPath = testSelector.value;

    if (!selectedPath) {
        terminalOutput.textContent = "Seleccioná un archivo de prueba primero.";
        terminalOutput.className = "error";
        statusTag.textContent = "error";
        statusTag.className = "tag error";
        return;
    }

    try {
        const response = await fetch("/tests/load", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                path: selectedPath
            })
        });

        const data = await response.json();

        if (!data.success) {
            terminalOutput.textContent = data.message || "No se pudo cargar la prueba.";
            terminalOutput.className = "error";
            statusTag.textContent = "error";
            statusTag.className = "tag error";
            return;
        }

        clearEditorErrors();

        editor.setValue(data.code);

        terminalOutput.textContent = `Archivo cargado: ${data.path}`;
        terminalOutput.className = "success";
        statusTag.textContent = "cargado";
        statusTag.className = "tag success";

        llvmOutput.textContent = "Aquí aparecerá el código LLVM IR.";

        editor.focus();

    } catch (error) {
        compilerOutput.textContent = "Error al cargar archivo de prueba:\n" + error;
        compilerOutput.className = "error";
    }
}

compileBtn.addEventListener("click", () => {
    sendRequest("/compile-run");
});

loadTestBtn.addEventListener("click", () => {
    loadSelectedTest();
});