class Scope:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.symbols = {}

    def define(self, symbol):
        if symbol.name in self.symbols:
            return False

        self.symbols[symbol.name] = symbol
        return True

    def resolve_current(self, name):
        return self.symbols.get(name)

    def resolve(self, name):
        symbol = self.resolve_current(name)

        if symbol is not None:
            return symbol

        if self.parent is not None:
            return self.parent.resolve(name)

        return None

    def __str__(self):
        return f"Scope({self.name})"


class SymbolTable:
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope

    def enter_scope(self, name):
        new_scope = Scope(name, self.current_scope)
        self.current_scope = new_scope
        return new_scope

    def exit_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent

    def define(self, symbol):
        return self.current_scope.define(symbol)

    def resolve(self, name):
        return self.current_scope.resolve(name)

    def resolve_current(self, name):
        return self.current_scope.resolve_current(name)

    def is_global_scope(self):
        return self.current_scope == self.global_scope