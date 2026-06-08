from antlr4.error.ErrorListener import ErrorListener


class SyntaxErrorInfo:
    def __init__(self, line, column, message):
        self.line = line
        self.column = column
        self.message = message

    def __str__(self):
        return f"Línea {self.line}, columna {self.column}: {self.message}"


class MiniGoSyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = SyntaxErrorInfo(line, column, msg)
        self.errors.append(error)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors