import sys
from pathlib import Path

from antlr4 import FileStream, CommonTokenStream

# Ruta raíz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = PROJECT_ROOT / "generated"

# Permite importar MiniGoLexer y MiniGoParser desde generated/
if str(GENERATED_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATED_DIR))

from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser

from syntaxchecker.syntax_error_listener import MiniGoSyntaxErrorListener


class SyntaxResult:
    def __init__(self, success, tree=None, errors=None):
        self.success = success
        self.tree = tree
        self.errors = errors or []

    def has_errors(self):
        return not self.success

    def print_errors(self):
        for error in self.errors:
            print(error)


class SyntaxChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lexer = None
        self.parser = None
        self.tree = None
        self.lexer_error_listener = MiniGoSyntaxErrorListener()
        self.parser_error_listener = MiniGoSyntaxErrorListener()

    def analyze(self):
        input_stream = FileStream(self.file_path, encoding="utf-8")

        self.lexer = MiniGoLexer(input_stream)
        self._configure_lexer_errors()

        token_stream = CommonTokenStream(self.lexer)

        self.parser = MiniGoParser(token_stream)
        self._configure_parser_errors()

        self.tree = self.parser.root()

        errors = self._collect_errors()

        if errors:
            return SyntaxResult(False, self.tree, errors)

        return SyntaxResult(True, self.tree, [])

    def _configure_lexer_errors(self):
        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.lexer_error_listener)

    def _configure_parser_errors(self):
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.parser_error_listener)

    def _collect_errors(self):
        return (
            self.lexer_error_listener.get_errors()
            + self.parser_error_listener.get_errors()
        )