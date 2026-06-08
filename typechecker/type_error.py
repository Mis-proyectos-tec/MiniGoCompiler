class TypeErrorInfo:
    def __init__(self, line, column, message):
        self.line = line
        self.column = column
        self.message = message

    def __str__(self):
        return f"Línea {self.line}, columna {self.column}: {self.message}"