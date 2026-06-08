from dataclasses import dataclass, field


@dataclass
class Symbol:
    name: str
    minigo_type: object
    line: int = 0
    column: int = 0


@dataclass
class VariableSymbol(Symbol):
    pass


@dataclass
class TypeSymbol(Symbol):
    pass


@dataclass
class FunctionSymbol(Symbol):
    parameters: list = field(default_factory=list)
    return_type: object = None