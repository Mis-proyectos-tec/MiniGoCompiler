import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = PROJECT_ROOT / "generated"

if str(GENERATED_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATED_DIR))

from MiniGoVisitor import MiniGoVisitor

from typechecker.type_error import TypeErrorInfo
from typechecker.symbol_table import SymbolTable
from typechecker.symbols import VariableSymbol, FunctionSymbol, TypeSymbol
from typechecker.types import (
    INT,
    FLOAT64,
    STRING,
    RUNE,
    BOOL,
    VOID,
    ERROR,
    UNKNOWN,
    ArrayType,
    SliceType,
    StructType,
    primitive_type_from_name,
    is_primitive_type,
    is_numeric_type,
    is_integer_type,
    is_simple_type,
)


class TypeCheckResult:
    def __init__(self, success, errors=None, symbol_table=None):
        self.success = success
        self.errors = errors or []
        self.symbol_table = symbol_table

    def has_errors(self):
        return not self.success

    def print_errors(self):
        for error in self.errors:
            print(error)


class MiniGoTypeChecker(MiniGoVisitor):
    def __init__(self, debug=False):
        super().__init__()
        self.errors = []
        self.symbol_table = SymbolTable()
        self.debug = debug
        self.current_function = None

        self.loop_depth = 0
        self.switch_depth = 0
        self.return_found_stack = []
        self.predeclared_functions = set()
        self.allow_void_function_call_depth = 0

        self._define_builtin_types()
        self._define_builtin_constants()
        self._define_builtin_functions()

    def check(self, tree):
        self.visit(tree)

        if self.errors:
            return TypeCheckResult(False, self.errors, self.symbol_table)

        return TypeCheckResult(True, [], self.symbol_table)

    # =====================================================
    # Configuración inicial
    # =====================================================

    def _define_builtin_types(self):
        self.symbol_table.define(TypeSymbol("int", INT))
        self.symbol_table.define(TypeSymbol("float64", FLOAT64))
        self.symbol_table.define(TypeSymbol("string", STRING))
        self.symbol_table.define(TypeSymbol("rune", RUNE))
        self.symbol_table.define(TypeSymbol("bool", BOOL))

    def _define_builtin_constants(self):
        self.symbol_table.define(VariableSymbol("true", BOOL))
        self.symbol_table.define(VariableSymbol("false", BOOL))

    def _define_builtin_functions(self):
        self.symbol_table.define(FunctionSymbol("print", VOID, return_type=VOID))
        self.symbol_table.define(FunctionSymbol("println", VOID, return_type=VOID))
        self.symbol_table.define(FunctionSymbol("len", INT, return_type=INT))
        self.symbol_table.define(FunctionSymbol("cap", INT, return_type=INT))
        self.symbol_table.define(FunctionSymbol("append", UNKNOWN, return_type=UNKNOWN))

    # =====================================================
    # Manejo de errores
    # =====================================================

    def add_error(self, ctx, message):
        token = ctx.start
        self.errors.append(
            TypeErrorInfo(token.line, token.column, message)
        )

    def _debug(self, message):
        if self.debug:
            print(message)

    # =====================================================
    # Helpers
    # =====================================================

    def _get_identifier_names(self, identifier_list_ctx):
        return [identifier.getText() for identifier in identifier_list_ctx.IDENTIFIER()]

    def _define_symbol(self, ctx, symbol):
        if not self.symbol_table.define(symbol):
            self.add_error(
                ctx,
                f"El identificador '{symbol.name}' ya fue declarado en este ámbito."
            )

    def _build_struct_type(self, struct_ctx):
        fields = {}

        mems_ctx = struct_ctx.structMemDecls()

        if mems_ctx is None:
            return StructType("anonymous_struct", fields)

        for field_decl_ctx in mems_ctx.singleVarDeclNoExps():
            field_names = self._get_identifier_names(field_decl_ctx.identifierList())
            field_type = self._get_decl_type(field_decl_ctx.declType())

            for field_name in field_names:
                if field_name in fields:
                    self.add_error(
                        field_decl_ctx,
                        f"El campo '{field_name}' ya fue declarado en este struct."
                    )
                else:
                    fields[field_name] = field_type

        return StructType("anonymous_struct", fields)

    def _get_decl_type(self, ctx):
        if ctx is None:
            return UNKNOWN

        # Caso: ( tipo )
        if hasattr(ctx, "declType") and ctx.declType() is not None:
            inner = ctx.declType()
            if inner is not None:
                return self._get_decl_type(inner)

        # Caso: IDENTIFIER
        if ctx.IDENTIFIER() is not None:
            type_name = ctx.IDENTIFIER().getText()

            primitive = primitive_type_from_name(type_name)
            if primitive is not None:
                return primitive

            symbol = self.symbol_table.resolve(type_name)

            if isinstance(symbol, TypeSymbol):
                return symbol.minigo_type

            self.add_error(ctx, f"El tipo '{type_name}' no ha sido declarado.")
            return ERROR

        # Caso: []tipo
        if ctx.sliceDeclType() is not None:
            element_type = self._get_decl_type(ctx.sliceDeclType().declType())
            return SliceType(element_type)

        # Caso: [n]tipo
        if ctx.arrayDeclType() is not None:
            array_ctx = ctx.arrayDeclType()
            size = int(array_ctx.INTLITERAL().getText())
            element_type = self._get_decl_type(array_ctx.declType())
            return ArrayType(size, element_type)

        # Caso: struct { ... }
        if ctx.structDeclType() is not None:
            return self._build_struct_type(ctx.structDeclType())

        return UNKNOWN

    def _get_literal_type(self, ctx):
        if ctx.INTLITERAL() is not None:
            return INT

        if ctx.FLOATLITERAL() is not None:
            return FLOAT64

        if ctx.RAWSTRINGLITERAL() is not None:
            return STRING

        if ctx.INTERPRETEDSTRINGLITERAL() is not None:
            return STRING

        if ctx.RUNELITERAL() is not None:
            return RUNE

        return UNKNOWN

    def _is_error_pair(self, left_type, right_type):
        return left_type.is_error() or right_type.is_error()

    def _same_type(self, left_type, right_type):
        return left_type == right_type

    def _is_comparable_type(self, minigo_type):
        return minigo_type in [INT, FLOAT64, STRING, RUNE, BOOL]

    def _is_ordered_type(self, minigo_type):
        return minigo_type in [INT, FLOAT64, STRING, RUNE]

    def _get_operator_text(self, op_ctx):
        return op_ctx.getText()

    def _is_void_function_call_allowed(self):
        return self.allow_void_function_call_depth > 0

    def _visit_expression_as_statement(self, expression_ctx):
        """
        Permite llamadas a procedimientos como statement:

        imprimir();

        Pero no permite usar procedimientos como valor en:
        var x int = imprimir();
        return imprimir();
        x = imprimir();
        """
        self.allow_void_function_call_depth += 1
        result_type = self.visit(expression_ctx)
        self.allow_void_function_call_depth -= 1
        return result_type

    def _is_array_or_slice(self, minigo_type):
        return isinstance(minigo_type, (ArrayType, SliceType))

    def _get_element_type(self, minigo_type):
        if isinstance(minigo_type, (ArrayType, SliceType)):
            return minigo_type.element_type

        return ERROR

    def _types_are_assignable(self, target_type, value_type):
        """
        Regla central para asignaciones.
        MiniGo exige tipos compatibles.
        """

        if target_type.is_error() or value_type.is_error():
            return True

        # Tipos iguales: int=int, string=string, []int=[]int, Persona=Persona
        if target_type == value_type:
            return True

        return False

    def _is_struct(self, minigo_type):
        return isinstance(minigo_type, StructType)

    def _validate_identifier_expression_count(self, ctx, names, expression_types):
        if len(names) != len(expression_types):
            self.add_error(
                ctx,
                f"La cantidad de identificadores ({len(names)}) no coincide "
                f"con la cantidad de expresiones ({len(expression_types)})."
            )
            return False

        return True

    def _validate_inferred_type(self, ctx, name, inferred_type):
        if inferred_type.is_error():
            return inferred_type

        if not is_primitive_type(inferred_type):
            self.add_error(
                ctx,
                f"MiniGo solo permite inferencia de tipos primitivos; "
                f"no se puede inferir '{inferred_type}' para la variable '{name}'."
            )

        return inferred_type

    # =====================================================
    # Visitor principal
    # =====================================================

    def visitRoot(self, ctx):
        self._debug("Visitando root")

        self._predeclare_functions(ctx)

        return self.visitChildren(ctx)

    # =====================================================
    # Declaraciones de tipo
    # =====================================================

    def visitSingleTypeDecl(self, ctx):
        type_name = ctx.IDENTIFIER().getText()
        minigo_type = self._get_decl_type(ctx.declType())

        if isinstance(minigo_type, StructType):
            minigo_type.name = type_name

        symbol = TypeSymbol(
            name=type_name,
            minigo_type=minigo_type,
            line=ctx.start.line,
            column=ctx.start.column
        )

        self._define_symbol(ctx, symbol)

        return minigo_type
    # =====================================================
    # Declaraciones de funciones
    # =====================================================

    def visitFuncDecl(self, ctx):
        front_ctx = ctx.funcFrontDecl()
        function_name = front_ctx.IDENTIFIER().getText()

        function_symbol = self.symbol_table.global_scope.resolve_current(function_name)

        if not isinstance(function_symbol, FunctionSymbol):
            return_type = VOID

            if front_ctx.declType() is not None:
                return_type = self._get_decl_type(front_ctx.declType())

            parameters = self._get_function_parameters(front_ctx)

            function_symbol = FunctionSymbol(
                name=function_name,
                minigo_type=return_type,
                line=front_ctx.start.line,
                column=front_ctx.start.column,
                parameters=parameters,
                return_type=return_type
            )

            self._define_symbol(front_ctx, function_symbol)

        previous_function = self.current_function
        self.current_function = function_symbol

        self.return_found_stack.append(False)

        self.symbol_table.enter_scope(f"function {function_name}")

        for parameter in function_symbol.parameters:
            self._define_symbol(front_ctx, parameter)

        self.visit(ctx.block().statementList())

        self.symbol_table.exit_scope()

        found_return = self.return_found_stack.pop()

        if function_symbol.return_type != VOID and not found_return:
            self.add_error(
                front_ctx,
                f"La función '{function_name}' debe retornar un valor de tipo '{function_symbol.return_type}'."
            )

        self.current_function = previous_function

        return function_symbol.return_type

    def _get_function_parameters(self, front_ctx):
        parameters = []

        args_ctx = front_ctx.funcArgDecls()

        if args_ctx is None:
            return parameters

        for param_ctx in args_ctx.singleVarDeclNoExps():
            names = self._get_identifier_names(param_ctx.identifierList())
            param_type = self._get_decl_type(param_ctx.declType())

            for name in names:
                parameters.append(
                    VariableSymbol(
                        name=name,
                        minigo_type=param_type,
                        line=param_ctx.start.line,
                        column=param_ctx.start.column
                    )
                )

        return parameters

    def _predeclare_functions(self, root_ctx):
        top_ctx = root_ctx.topDeclarationList()

        if top_ctx is None:
            return

        for func_ctx in top_ctx.funcDecl():
            front_ctx = func_ctx.funcFrontDecl()
            function_name = front_ctx.IDENTIFIER().getText()

            return_type = VOID

            if front_ctx.declType() is not None:
                return_type = self._get_decl_type(front_ctx.declType())

            parameters = self._get_function_parameters(front_ctx)

            function_symbol = FunctionSymbol(
                name=function_name,
                minigo_type=return_type,
                line=front_ctx.start.line,
                column=front_ctx.start.column,
                parameters=parameters,
                return_type=return_type
            )

            if not self.symbol_table.define(function_symbol):
                self.add_error(
                    front_ctx,
                    f"La función '{function_name}' ya fue declarada en este ámbito."
                )
            else:
                self.predeclared_functions.add(function_name)

    # =====================================================
    # Bloques y ámbitos
    # =====================================================

    def visitBlock(self, ctx):
        self.symbol_table.enter_scope("block")
        result = self.visit(ctx.statementList())
        self.symbol_table.exit_scope()
        return result

    # =====================================================
    # Declaraciones de variables
    # =====================================================

    def visitSingleVarDeclNoExps(self, ctx):
        names = self._get_identifier_names(ctx.identifierList())
        declared_type = self._get_decl_type(ctx.declType())

        for name in names:
            symbol = VariableSymbol(
                name=name,
                minigo_type=declared_type,
                line=ctx.start.line,
                column=ctx.start.column
            )

            self._define_symbol(ctx, symbol)

        return declared_type

    def visitSingleVarDecl(self, ctx):
        """
        Casos de la gramática:

        identifierList declType = expressionList
        identifierList = expressionList
        singleVarDeclNoExps
        """

        # Caso: identifierList declType
        if ctx.singleVarDeclNoExps() is not None:
            return self.visit(ctx.singleVarDeclNoExps())

        names = self._get_identifier_names(ctx.identifierList())

        declared_type = UNKNOWN

        if ctx.declType() is not None:
            declared_type = self._get_decl_type(ctx.declType())

        expression_types = []

        if ctx.expressionList() is not None:
            expression_types = self._get_expression_list_types(ctx.expressionList())

        self._validate_identifier_expression_count(ctx, names, expression_types)

        for index, name in enumerate(names):
            variable_type = declared_type

            if index >= len(expression_types):
                variable_type = ERROR
            else:
                expression_type = expression_types[index]

                # Caso: var x = 10;
                if declared_type == UNKNOWN:
                    variable_type = self._validate_inferred_type(
                        ctx,
                        name,
                        expression_type
                    )

                # Caso: var x int = 10;
                else:
                    variable_type = declared_type

                    if not self._types_are_assignable(declared_type, expression_type):
                        self.add_error(
                            ctx,
                            f"No se puede asignar una expresión de tipo '{expression_type}' "
                            f"a la variable '{name}' de tipo '{declared_type}'."
                        )

            symbol = VariableSymbol(
                name=name,
                minigo_type=variable_type,
                line=ctx.start.line,
                column=ctx.start.column
            )

            self._define_symbol(ctx, symbol)

        return declared_type

    # =====================================================
    # Declaraciones múltiples
    # =====================================================

    def visitVariableDecl(self, ctx):
        return self.visitChildren(ctx)

    def visitInnerVarDecls(self, ctx):
        return self.visitChildren(ctx)

    def visitTypeDecl(self, ctx):
        return self.visitChildren(ctx)

    def visitInnerTypeDecls(self, ctx):
        return self.visitChildren(ctx)

    # =====================================================
    # Statements
    # =====================================================

    def visitStatement(self, ctx):
        if ctx.PRINT() is not None:
            return self._check_print_statement(ctx, "print")

        if ctx.PRINTLN() is not None:
            return self._check_print_statement(ctx, "println")

        if ctx.RETURN() is not None:
            return self._check_return_statement(ctx)

        if ctx.BREAK() is not None:
            if self.loop_depth == 0 and self.switch_depth == 0:
                self.add_error(ctx, "La instrucción 'break' solo puede usarse dentro de un for o switch.")
            return VOID

        if ctx.CONTINUE() is not None:
            if self.loop_depth == 0:
                self.add_error(ctx, "La instrucción 'continue' solo puede usarse dentro de un for.")
            return VOID

        return self.visitChildren(ctx)

    def _check_print_statement(self, ctx, name):
        if ctx.expressionList() is not None:
            expression_types = self._get_expression_list_types(ctx.expressionList())

            for expression_type in expression_types:
                if not is_simple_type(expression_type) and not expression_type.is_error():
                    self.add_error(
                        ctx,
                        f"La función '{name}' solo puede imprimir tipos simples."
                    )

        return VOID

    def _check_return_statement(self, ctx):
        if self.current_function is None:
            self.add_error(ctx, "No se puede usar 'return' fuera de una función.")
            return ERROR

        if self.return_found_stack:
            self.return_found_stack[-1] = True

        expected_type = self.current_function.return_type

        # return;
        if ctx.expression() is None:
            if expected_type != VOID:
                self.add_error(
                    ctx,
                    f"La función '{self.current_function.name}' debe retornar un valor de tipo '{expected_type}'."
                )
            return VOID

        # return expresión;
        expression_type = self.visit(ctx.expression())

        if expected_type == VOID:
            self.add_error(
                ctx,
                f"La función '{self.current_function.name}' no debe retornar un valor."
            )
            return ERROR

        if expression_type != expected_type and not expression_type.is_error():
            self.add_error(
                ctx,
                f"El tipo de retorno es '{expression_type}', pero la función "
                f"'{self.current_function.name}' debe retornar '{expected_type}'."
            )
            return ERROR

        return expression_type

    # =====================================================
    # Simple statements y asignaciones
    # =====================================================

    def visitNonEmptySimpleStatement(self, ctx):
        # assignmentStatement
        if ctx.assignmentStatement() is not None:
            return self.visit(ctx.assignmentStatement())

        # expressionList := expressionList
        if ctx.DECLARE_ASSIGN() is not None:
            return self._check_short_variable_declaration(ctx)

        # expression ++ / expression --
        if ctx.INC() is not None or ctx.DEC() is not None:
            expression_type = self.visit(ctx.expression())

            if expression_type not in [INT, FLOAT64] and not expression_type.is_error():
                self.add_error(
                    ctx,
                    "Los operadores '++' y '--' solo se pueden aplicar a valores numéricos."
                )

            return expression_type

        # expression como statement.
        # Aquí permitimos llamadas void como: imprimir();
        if ctx.expression() is not None:
            return self._visit_expression_as_statement(ctx.expression())

        return VOID

    def _check_short_variable_declaration(self, ctx):
        left_expressions = ctx.expressionList(0).expression()
        right_expressions = ctx.expressionList(1).expression()

        if len(left_expressions) != len(right_expressions):
            self.add_error(
                ctx,
                f"La cantidad de identificadores ({len(left_expressions)}) no coincide "
                f"con la cantidad de expresiones ({len(right_expressions)}) en ':='."
            )
            return ERROR

        new_variable_found = False

        for index, left_expr in enumerate(left_expressions):
            name = self._expression_as_identifier(left_expr)

            if name is None:
                self.add_error(
                    left_expr,
                    "El lado izquierdo de ':=' debe ser un identificador simple."
                )
                continue

            expression_type = self.visit(right_expressions[index])
            current_symbol = self.symbol_table.resolve_current(name)

            # Si no existe en el ámbito actual, se declara una variable nueva.
            if current_symbol is None:
                inferred_type = self._validate_inferred_type(
                    left_expr,
                    name,
                    expression_type
                )

                symbol = VariableSymbol(
                    name=name,
                    minigo_type=inferred_type,
                    line=left_expr.start.line,
                    column=left_expr.start.column
                )

                self._define_symbol(left_expr, symbol)
                new_variable_found = True

            else:
                if not isinstance(current_symbol, VariableSymbol):
                    self.add_error(
                        left_expr,
                        f"El identificador '{name}' ya existe en este ámbito y no es una variable."
                    )
                    continue

                if not self._types_are_assignable(current_symbol.minigo_type, expression_type):
                    self.add_error(
                        left_expr,
                        f"No se puede reasignar '{name}' con tipo '{expression_type}', "
                        f"porque ya fue declarado como '{current_symbol.minigo_type}'."
                    )

        if not new_variable_found:
            self.add_error(
                ctx,
                "La declaración corta ':=' debe declarar al menos una variable nueva en el ámbito actual."
            )

        return VOID

    def visitAssignmentStatement(self, ctx):
        # expressionList = expressionList
        if ctx.ASSIGN() is not None:
            return self._check_normal_assignment(ctx)

        # expression += expression, expression -= expression, etc.
        return self._check_compound_assignment(ctx)

    def _check_normal_assignment(self, ctx):
        left_expressions = ctx.expressionList(0).expression()
        right_expressions = ctx.expressionList(1).expression()

        if len(left_expressions) != len(right_expressions):
            self.add_error(
                ctx,
                "La cantidad de elementos del lado izquierdo no coincide con la del lado derecho."
            )
            return ERROR

        for index, left_expr in enumerate(left_expressions):
            left_type = self._check_assignable_expression(left_expr)
            right_type = self.visit(right_expressions[index])

            if not self._types_are_assignable(left_type, right_type):
                self.add_error(
                    ctx,
                    f"No se puede asignar un valor de tipo '{right_type}' a una variable de tipo '{left_type}'."
                )

        return VOID

    def _check_compound_assignment(self, ctx):
        left_type = self._check_assignable_expression(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = self._get_operator_text(ctx.assignmentOp())

        if self._is_error_pair(left_type, right_type):
            return ERROR

        if left_type != right_type:
            self.add_error(
                ctx,
                f"Asignación compuesta inválida entre tipos '{left_type}' y '{right_type}'."
            )
            return ERROR

        if operator in ["+=", "-=", "*=", "/="]:
            if operator == "+=" and left_type == STRING:
                return VOID

            if not is_numeric_type(left_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere una variable numérica."
                )
                return ERROR

            return VOID

        if operator == "%=":
            if not is_integer_type(left_type):
                self.add_error(
                    ctx,
                    "El operador '%=' requiere una variable entera."
                )
                return ERROR

            return VOID

        if operator in ["&=", "|=", "^=", "<<=", ">>=", "&^="]:
            if not is_integer_type(left_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere una variable entera."
                )
                return ERROR

            return VOID

        return VOID

    def _check_assignable_expression(self, expression_ctx):
        """
        Valida expresiones que pueden estar al lado izquierdo de una asignación.

        Casos aceptados por ahora:
        x = 10
        nums[0] = 10
        persona.edad = 20
        """

        try:
            primary_ctx = expression_ctx.primaryExpression()
        except AttributeError:
            self.add_error(
                expression_ctx,
                "El lado izquierdo de una asignación debe ser una variable válida."
            )
            return ERROR

        if primary_ctx is None or primary_ctx.operand() is None:
            self.add_error(
                expression_ctx,
                "El lado izquierdo de una asignación debe ser una variable válida."
            )
            return ERROR

        operand_ctx = primary_ctx.operand()

        if operand_ctx.IDENTIFIER() is None:
            self.add_error(
                expression_ctx,
                "El lado izquierdo de una asignación debe iniciar con un identificador."
            )
            return ERROR

        name = operand_ctx.IDENTIFIER().getText()
        symbol = self.symbol_table.resolve(name)

        if symbol is None:
            self.add_error(
                expression_ctx,
                f"El identificador '{name}' no ha sido declarado."
            )
            return ERROR

        current_type = symbol.minigo_type

        # Aplicar índices: nums[0]
        if len(primary_ctx.index()) > 0:
            current_type = self._check_index_access(primary_ctx, current_type)

        # Aplicar selectores: persona.edad
        if len(primary_ctx.selector()) > 0:
            current_type = self._check_selector_access(primary_ctx, current_type)

        # No permitimos asignar a una llamada: f() = 10
        if len(primary_ctx.arguments()) > 0:
            self.add_error(
                expression_ctx,
                "No se puede asignar a una llamada de función."
            )
            return ERROR

        return current_type

    def _expression_as_identifier(self, expression_ctx):
        """
        Por ahora solo permitimos asignar directamente a identificadores simples.
        Después se puede ampliar para arreglos, selectors y structs:
        x = 10
        arr[0] = 10
        persona.edad = 20
        """

        try:
            primary_ctx = expression_ctx.primaryExpression()
        except AttributeError:
            return None

        if primary_ctx is None:
            return None

        # Si tiene selector, index o arguments, no es identificador simple.
        if len(primary_ctx.selector()) > 0:
            return None

        if len(primary_ctx.index()) > 0:
            return None

        if len(primary_ctx.arguments()) > 0:
            return None

        operand_ctx = primary_ctx.operand()

        if operand_ctx is None:
            return None

        if operand_ctx.IDENTIFIER() is None:
            return None

        return operand_ctx.IDENTIFIER().getText()

    # =====================================================
    # IF y FOR
    # =====================================================

    def visitIfStatement(self, ctx):
        """
        Valida las formas:

        if expression block
        if expression block else block
        if expression block else ifStatement
        if simpleStatement; expression block
        """

        self.symbol_table.enter_scope("if")

        # if simpleStatement; expression { ... }
        if ctx.nonEmptySimpleStatement() is not None:
            self.visit(ctx.nonEmptySimpleStatement())

        condition_type = self.visit(ctx.expression())

        if condition_type != BOOL and not condition_type.is_error():
            self.add_error(
                ctx,
                f"La condición del 'if' debe ser de tipo bool, no '{condition_type}'."
            )

        # Bloque principal del if
        self.visit(ctx.block(0))

        # else if
        if ctx.ifStatement() is not None:
            self.visit(ctx.ifStatement())

        # else block
        if len(ctx.block()) > 1:
            self.visit(ctx.block(1))

        self.symbol_table.exit_scope()

        return VOID

    def visitLoop(self, ctx):
        """
        Valida las formas:

        for block
        for expression block
        for init; condition; update block
        for init; ; update block
        """

        self.loop_depth += 1
        self.symbol_table.enter_scope("for")

        simple_statements = ctx.nonEmptySimpleStatement()

        # for { ... }
        if ctx.expression() is None and len(simple_statements) == 0:
            self.visit(ctx.block())

            self.symbol_table.exit_scope()
            self.loop_depth -= 1
            return VOID

        # for expression { ... }
        if ctx.expression() is not None and len(simple_statements) == 0:
            condition_type = self.visit(ctx.expression())

            if condition_type != BOOL and not condition_type.is_error():
                self.add_error(
                    ctx,
                    f"La condición del 'for' debe ser de tipo bool, no '{condition_type}'."
                )

            self.visit(ctx.block())

            self.symbol_table.exit_scope()
            self.loop_depth -= 1
            return VOID

        # for init; condition; update { ... }
        if len(simple_statements) >= 1:
            self.visit(simple_statements[0])

        if ctx.expression() is not None:
            condition_type = self.visit(ctx.expression())

            if condition_type != BOOL and not condition_type.is_error():
                self.add_error(
                    ctx,
                    f"La condición del 'for' debe ser de tipo bool, no '{condition_type}'."
                )

        if len(simple_statements) >= 2:
            self.visit(simple_statements[1])

        self.visit(ctx.block())

        self.symbol_table.exit_scope()
        self.loop_depth -= 1

        return VOID

    def visitSwitchStmt(self, ctx):
        """
        Valida las formas:

        switch expression { case ... }
        switch simpleStatement; expression { case ... }
        switch simpleStatement; { case ... }
        switch { case ... }

        Si el switch no tiene expresión, se comporta como switch true,
        por lo tanto los case deben ser bool.
        """

        self.switch_depth += 1
        self.symbol_table.enter_scope("switch")

        # switch simpleStatement; ...
        if ctx.nonEmptySimpleStatement() is not None:
            self.visit(ctx.nonEmptySimpleStatement())

        has_switch_expression = ctx.expression() is not None

        if has_switch_expression:
            switch_type = self.visit(ctx.expression())
        else:
            switch_type = BOOL

        default_count = 0

        clause_list_ctx = ctx.expressionCaseClauseList()

        if clause_list_ctx is not None:
            for clause_ctx in clause_list_ctx.expressionCaseClause():
                self.symbol_table.enter_scope("switch_case")

                switch_case_ctx = clause_ctx.expressionSwitchCase()

                # default:
                if switch_case_ctx.DEFAULT() is not None:
                    default_count += 1

                    if default_count > 1:
                        self.add_error(
                            switch_case_ctx,
                            "Un switch no puede tener más de un caso default."
                        )

                # case expressionList:
                else:
                    case_types = self._get_expression_list_types(
                        switch_case_ctx.expressionList()
                    )

                    for case_type in case_types:
                        if has_switch_expression:
                            if (
                                    case_type != switch_type
                                    and not case_type.is_error()
                                    and not switch_type.is_error()
                            ):
                                self.add_error(
                                    switch_case_ctx,
                                    f"El caso del switch tiene tipo '{case_type}', "
                                    f"pero se esperaba '{switch_type}'."
                                )
                        else:
                            if case_type != BOOL and not case_type.is_error():
                                self.add_error(
                                    switch_case_ctx,
                                    f"En un switch sin expresión, los case deben ser bool, "
                                    f"no '{case_type}'."
                                )

                self.visit(clause_ctx.statementList())

                self.symbol_table.exit_scope()

        self.symbol_table.exit_scope()
        self.switch_depth -= 1

        return VOID

    # =====================================================
    # Expresiones básicas
    # =====================================================

    def _get_expression_list_types(self, expression_list_ctx):
        types = []

        for expression_ctx in expression_list_ctx.expression():
            expression_type = self.visit(expression_ctx)
            types.append(expression_type)

        return types

    def visitPrimaryExpressionOnly(self, ctx):
        return self.visit(ctx.primaryExpression())

    def visitPrimaryExpression(self, ctx):
        # append(exp, exp)
        if ctx.appendExpression() is not None:
            return self.visit(ctx.appendExpression())

        # len(exp)
        if ctx.lengthExpression() is not None:
            return self.visit(ctx.lengthExpression())

        # cap(exp)
        if ctx.capExpression() is not None:
            return self.visit(ctx.capExpression())

        # operand (selector | index | arguments)*
        if ctx.operand() is not None:
            base_type = self.visit(ctx.operand())

            # llamada a función: nombre(...)
            if len(ctx.arguments()) > 0:
                return self._check_function_call_from_primary(ctx)

            # acceso a arreglo: arr[0]
            if len(ctx.index()) > 0:
                return self._check_index_access(ctx, base_type)

            # selector: persona.nombre
            if len(ctx.selector()) > 0:
                return self._check_selector_access(ctx, base_type)

            return base_type

        return UNKNOWN

    # =====================================================
    # Llamadas a funciones y expresiones predefinidas
    # =====================================================

    def _check_function_call_from_primary(self, ctx):
        function_name = self._get_primary_identifier_name(ctx)

        if function_name is None:
            self.add_error(ctx, "Solo se permiten llamadas directas a funciones por identificador.")
            return ERROR

        symbol = self.symbol_table.resolve(function_name)

        if symbol is None:
            self.add_error(ctx, f"La función '{function_name}' no ha sido declarada.")
            return ERROR

        if not isinstance(symbol, FunctionSymbol):
            self.add_error(ctx, f"El identificador '{function_name}' no es una función.")
            return ERROR

        arguments_ctx = ctx.arguments(0)
        argument_types = self._get_argument_types(arguments_ctx)

        expected_parameters = symbol.parameters

        if len(argument_types) != len(expected_parameters):
            self.add_error(
                ctx,
                f"La función '{function_name}' espera {len(expected_parameters)} argumento(s), "
                f"pero recibió {len(argument_types)}."
            )

            if symbol.return_type == VOID:
                return VOID

            return symbol.return_type

        for index, arg_type in enumerate(argument_types):
            expected_type = expected_parameters[index].minigo_type

            if arg_type != expected_type and not arg_type.is_error():
                self.add_error(
                    ctx,
                    f"El argumento {index + 1} de la función '{function_name}' debe ser "
                    f"de tipo '{expected_type}', pero se recibió '{arg_type}'."
                )

        if symbol.return_type == VOID and not self._is_void_function_call_allowed():
            self.add_error(
                ctx,
                f"La función '{function_name}' no retorna ningún valor y no puede usarse como expresión."
            )
            return ERROR

        return symbol.return_type

    def _get_primary_identifier_name(self, primary_ctx):
        operand_ctx = primary_ctx.operand()

        if operand_ctx is None:
            return None

        if operand_ctx.IDENTIFIER() is None:
            return None

        return operand_ctx.IDENTIFIER().getText()

    def _get_argument_types(self, arguments_ctx):
        if arguments_ctx.expressionList() is None:
            return []

        return self._get_expression_list_types(arguments_ctx.expressionList())

    def visitLengthExpression(self, ctx):
        expression_type = self.visit(ctx.expression())

        if not self._is_array_or_slice(expression_type) and not expression_type.is_error():
            self.add_error(
                ctx,
                f"La función 'len' solo se puede aplicar a arreglos o slices, no a '{expression_type}'."
            )

        return INT

    def visitCapExpression(self, ctx):
        expression_type = self.visit(ctx.expression())

        if not self._is_array_or_slice(expression_type) and not expression_type.is_error():
            self.add_error(
                ctx,
                f"La función 'cap' solo se puede aplicar a arreglos o slices, no a '{expression_type}'."
            )

        return INT

    def visitAppendExpression(self, ctx):
        slice_type = self.visit(ctx.expression(0))
        value_type = self.visit(ctx.expression(1))

        if not isinstance(slice_type, SliceType):
            if not slice_type.is_error():
                self.add_error(
                    ctx,
                    f"La función 'append' requiere que el primer argumento sea un slice, no '{slice_type}'."
                )
            return ERROR

        expected_type = slice_type.element_type

        if not self._types_are_assignable(expected_type, value_type):
            self.add_error(
                ctx,
                f"No se puede agregar un valor de tipo '{value_type}' "
                f"a un slice de tipo '{expected_type}'."
            )
            return ERROR

        return slice_type

    # =====================================================
    # Index y selector
    # =====================================================

    def _check_index_access(self, ctx, base_type):
        current_type = base_type

        for index_ctx in ctx.index():
            index_type = self.visit(index_ctx.expression())

            if index_type != INT and not index_type.is_error():
                self.add_error(index_ctx, "El índice de un arreglo o slice debe ser de tipo int.")

            if isinstance(current_type, ArrayType):
                current_type = current_type.element_type
            elif isinstance(current_type, SliceType):
                current_type = current_type.element_type
            else:
                if not current_type.is_error():
                    self.add_error(index_ctx, "Solo se puede indexar un arreglo o slice.")
                return ERROR

        return current_type

    def _check_selector_access(self, ctx, base_type):
        current_type = base_type

        for selector_ctx in ctx.selector():
            field_name = selector_ctx.IDENTIFIER().getText()

            if not isinstance(current_type, StructType):
                if not current_type.is_error():
                    self.add_error(
                        selector_ctx,
                        f"No se puede acceder al campo '{field_name}' porque '{current_type}' no es un struct."
                    )
                return ERROR

            if not current_type.has_field(field_name):
                self.add_error(
                    selector_ctx,
                    f"El campo '{field_name}' no existe en el struct '{current_type}'."
                )
                return ERROR

            current_type = current_type.get_field_type(field_name)

        return current_type

    def visitOperand(self, ctx):
        if ctx.literal() is not None:
            return self.visit(ctx.literal())

        if ctx.IDENTIFIER() is not None:
            name = ctx.IDENTIFIER().getText()
            symbol = self.symbol_table.resolve(name)

            if symbol is None:
                self.add_error(ctx, f"El identificador '{name}' no ha sido declarado.")
                return ERROR

            return symbol.minigo_type

        if ctx.expression() is not None:
            return self.visit(ctx.expression())

        return UNKNOWN

    def visitLiteral(self, ctx):
        return self._get_literal_type(ctx)

    def visitUnaryPlusExpression(self, ctx):
        expression_type = self.visit(ctx.expression())

        if not is_numeric_type(expression_type) and not expression_type.is_error():
            self.add_error(
                ctx,
                f"El operador '+' unario solo se puede aplicar a tipos numéricos, no a '{expression_type}'."
            )
            return ERROR

        return expression_type

    def visitUnaryMinusExpression(self, ctx):
        expression_type = self.visit(ctx.expression())

        if not is_numeric_type(expression_type) and not expression_type.is_error():
            self.add_error(
                ctx,
                f"El operador '-' unario solo se puede aplicar a tipos numéricos, no a '{expression_type}'."
            )
            return ERROR

        return expression_type

    def visitUnaryBitNotExpression(self, ctx):
        expression_type = self.visit(ctx.expression())

        if not is_integer_type(expression_type) and not expression_type.is_error():
            self.add_error(
                ctx,
                f"El operador '^' unario solo se puede aplicar a tipos enteros, no a '{expression_type}'."
            )
            return ERROR

        return expression_type

    def visitMultiplicativeExpression(self, ctx):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = self._get_operator_text(ctx.multiplicativeOp())

        if self._is_error_pair(left_type, right_type):
            return ERROR

        if operator in ["*", "/"]:
            if not is_numeric_type(left_type) or not is_numeric_type(right_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere operandos numéricos."
                )
                return ERROR

            if left_type != right_type:
                self.add_error(
                    ctx,
                    f"El operador '{operator}' no puede aplicarse entre '{left_type}' y '{right_type}'."
                )
                return ERROR

            return left_type

        if operator == "%":
            if not is_integer_type(left_type) or not is_integer_type(right_type):
                self.add_error(
                    ctx,
                    "El operador '%' requiere operandos enteros."
                )
                return ERROR

            if left_type != right_type:
                self.add_error(
                    ctx,
                    f"El operador '%' no puede aplicarse entre '{left_type}' y '{right_type}'."
                )
                return ERROR

            return left_type

        if operator in ["<<", ">>", "&", "&^"]:
            if not is_integer_type(left_type) or not is_integer_type(right_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere operandos enteros."
                )
                return ERROR

            return left_type

        return ERROR

    def visitAdditiveExpression(self, ctx):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = self._get_operator_text(ctx.additiveOp())

        if self._is_error_pair(left_type, right_type):
            return ERROR

        if operator in ["+", "-"]:
            # Permitimos string + string solo para concatenación.
            if operator == "+" and left_type == STRING and right_type == STRING:
                return STRING

            if not is_numeric_type(left_type) or not is_numeric_type(right_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere operandos numéricos."
                )
                return ERROR

            if left_type != right_type:
                self.add_error(
                    ctx,
                    f"El operador '{operator}' no puede aplicarse entre '{left_type}' y '{right_type}'."
                )
                return ERROR

            return left_type

        if operator in ["|", "^"]:
            if not is_integer_type(left_type) or not is_integer_type(right_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere operandos enteros."
                )
                return ERROR

            if left_type != right_type:
                self.add_error(
                    ctx,
                    f"El operador '{operator}' no puede aplicarse entre '{left_type}' y '{right_type}'."
                )
                return ERROR

            return left_type

        return ERROR

    def visitRelationalExpression(self, ctx):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = self._get_operator_text(ctx.relationalOp())

        if self._is_error_pair(left_type, right_type):
            return ERROR

        if left_type != right_type:
            self.add_error(
                ctx,
                f"El operador '{operator}' no puede comparar '{left_type}' con '{right_type}'."
            )
            return ERROR

        if operator in ["==", "!="]:
            if not self._is_comparable_type(left_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' no puede aplicarse al tipo '{left_type}'."
                )
                return ERROR

            return BOOL

        if operator in ["<", "<=", ">", ">="]:
            if not self._is_ordered_type(left_type):
                self.add_error(
                    ctx,
                    f"El operador '{operator}' requiere tipos ordenables."
                )
                return ERROR

            return BOOL

        return ERROR

    def visitLogicalAndExpression(self, ctx):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))

        if left_type != BOOL or right_type != BOOL:
            self.add_error(ctx, "El operador '&&' requiere expresiones booleanas.")
            return ERROR

        return BOOL

    def visitLogicalOrExpression(self, ctx):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))

        if left_type != BOOL or right_type != BOOL:
            self.add_error(ctx, "El operador '||' requiere expresiones booleanas.")
            return ERROR

        return BOOL