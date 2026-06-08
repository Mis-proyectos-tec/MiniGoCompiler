from dataclasses import dataclass, field


class MiniGoType:
    def __init__(self, name):
        self.name = name

    def is_error(self):
        return self.name == "error"

    def is_void(self):
        return self.name == "void"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, MiniGoType) and self.name == other.name


class PrimitiveType(MiniGoType):
    pass


@dataclass
class ArrayType(MiniGoType):
    size: int
    element_type: MiniGoType

    def __init__(self, size, element_type):
        super().__init__(f"[{size}]{element_type}")
        self.size = size
        self.element_type = element_type

    def __eq__(self, other):
        return (
            isinstance(other, ArrayType)
            and self.size == other.size
            and self.element_type == other.element_type
        )


@dataclass
class SliceType(MiniGoType):
    element_type: MiniGoType

    def __init__(self, element_type):
        super().__init__(f"[]{element_type}")
        self.element_type = element_type

    def __eq__(self, other):
        return (
            isinstance(other, SliceType)
            and self.element_type == other.element_type
        )


@dataclass
class StructType(MiniGoType):
    fields: dict = field(default_factory=dict)

    def __init__(self, name="struct", fields=None):
        super().__init__(name)
        self.fields = fields or {}

    def __eq__(self, other):
        return (
            isinstance(other, StructType)
            and self.name == other.name
        )

    def has_field(self, field_name):
        return field_name in self.fields

    def get_field_type(self, field_name):
        return self.fields.get(field_name, ERROR)


INT = PrimitiveType("int")
FLOAT64 = PrimitiveType("float64")
STRING = PrimitiveType("string")
RUNE = PrimitiveType("rune")
BOOL = PrimitiveType("bool")
VOID = PrimitiveType("void")
ERROR = PrimitiveType("error")
UNKNOWN = PrimitiveType("unknown")


def primitive_type_from_name(name):
    primitives = {
        "int": INT,
        "float64": FLOAT64,
        "string": STRING,
        "rune": RUNE,
        "bool": BOOL,
    }

    return primitives.get(name)


def is_primitive_type(minigo_type):
    return minigo_type in [INT, FLOAT64, STRING, RUNE, BOOL]


def is_numeric_type(minigo_type):
    return minigo_type in [INT, FLOAT64, RUNE]


def is_integer_type(minigo_type):
    return minigo_type in [INT, RUNE]


def is_simple_type(minigo_type):
    return is_primitive_type(minigo_type)