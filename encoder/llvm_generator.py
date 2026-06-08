import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = PROJECT_ROOT / "generated"

if str(GENERATED_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATED_DIR))

from MiniGoVisitor import MiniGoVisitor

from encoder.llvm_context import LLVMContext
from encoder.llvm_value import LLVMValue


class LLVMGenerationResult:
    def __init__(self, llvm_code):
        self.llvm_code = llvm_code


class MiniGoLLVMGenerator(MiniGoVisitor):
    def __init__(self):
        super().__init__()
        self.context = LLVMContext()
        self.current_function_return_type = None
        self.function_has_return = False
        self.functions = {}

    def generate(self, tree):
        self._register_all_functions(tree)
        self._emit_header()
        self.visit(tree)
        return LLVMGenerationResult(self.context.get_code())

    # =====================================================
    # Header LLVM
    # =====================================================

    def _emit_header(self):
        self.context.emit_global('@.fmt_int = private unnamed_addr constant [4 x i8] c"%d\\0A\\00"')
        self.context.emit_global('@.fmt_str = private unnamed_addr constant [4 x i8] c"%s\\0A\\00"')
        self.context.emit_global("")
        self.context.emit_global("declare i32 @printf(i8*, ...)")

    # =====================================================
    # Helpers
    # =====================================================

    def _llvm_type(self, minigo_type_name):
        if minigo_type_name == "int":
            return "i32"

        if minigo_type_name == "bool":
            return "i1"

        return "i32"

    def _emit_print_int(self, value):
        if isinstance(value, LLVMValue):
            value = self._emit_bool_to_int(value)
            raw_value = value.value
        else:
            raw_value = value

        self.context.emit(
            f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds '
            f'([4 x i8], [4 x i8]* @.fmt_int, i32 0, i32 0), i32 {raw_value})'
        )


    def _normalize_int_literal(self, text):
        text = text.replace("_", "")

        if text.startswith(("0x", "0X")):
            return str(int(text, 16))

        if text.startswith(("0b", "0B")):
            return str(int(text, 2))

        if text.startswith(("0o", "0O")):
            return str(int(text, 8))

        return text

    def _create_alloca(self, name, llvm_type, metadata=None):
        pointer = f"%{name}"
        self.context.emit(f"  {pointer} = alloca {llvm_type}")
        self.context.define_variable(name, pointer, llvm_type, metadata)
        return pointer

    def _store_value(self, pointer, llvm_type, value):
        self.context.emit(f"  store {llvm_type} {value}, {llvm_type}* {pointer}")

    def _load_variable(self, name):
        variable = self.context.get_variable(name)

        if variable is None:
            return LLVMValue("0", "i32")

        temp = self.context.new_temp()
        pointer = variable["pointer"]
        llvm_type = variable["type"]

        self.context.emit(f"  {temp} = load {llvm_type}, {llvm_type}* {pointer}")

        return LLVMValue(temp, llvm_type)

    def _get_lvalue_info(self, expression_ctx):
        """
        Soporta:

        x = 10;
        nums[0] = 10;
        """

        try:
            primary_ctx = expression_ctx.primaryExpression()
        except AttributeError:
            return None

        return self._get_lvalue_info_from_primary(primary_ctx)

    def _load_from_pointer(self, pointer, llvm_type):
        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = load {llvm_type}, {llvm_type}* {pointer}")
        return LLVMValue(temp, llvm_type)

    def _emit_binary_int_op(self, operator, left, right):
        temp = self.context.new_temp()

        if operator == "+":
            self.context.emit(f"  {temp} = add i32 {left.value}, {right.value}")
        elif operator == "-":
            self.context.emit(f"  {temp} = sub i32 {left.value}, {right.value}")
        elif operator == "*":
            self.context.emit(f"  {temp} = mul i32 {left.value}, {right.value}")
        elif operator == "/":
            self.context.emit(f"  {temp} = sdiv i32 {left.value}, {right.value}")
        elif operator == "%":
            self.context.emit(f"  {temp} = srem i32 {left.value}, {right.value}")
        else:
            self.context.emit(f"  {temp} = add i32 {left.value}, {right.value}")

        return LLVMValue(temp, "i32")

    def _label_ref(self, label):
        return f"%{label}"

    def _emit_compare_int(self, operator, left, right):
        temp = self.context.new_temp()

        op_map = {
            "==": "eq",
            "!=": "ne",
            "<": "slt",
            "<=": "sle",
            ">": "sgt",
            ">=": "sge",
        }

        llvm_op = op_map.get(operator)

        if llvm_op is None:
            return LLVMValue("0", "i1")

        self.context.emit(
            f"  {temp} = icmp {llvm_op} i32 {left.value}, {right.value}"
        )

        return LLVMValue(temp, "i1")

    def _emit_bool_to_int(self, value):
        if value.llvm_type != "i1":
            return value

        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = zext i1 {value.value} to i32")
        return LLVMValue(temp, "i32")


    def _decl_type_to_llvm(self, decl_type_ctx):
        if decl_type_ctx is None:
            return "void"

        type_text = decl_type_ctx.getText()

        if type_text == "int":
            return "i32"

        if type_text == "bool":
            return "i1"

        # Para esta etapa LLVM solo manejamos int/bool.
        # Otros tipos se pueden ampliar después.
        return "i32"

    def _get_function_return_type(self, front_ctx):
        if front_ctx.declType() is None:
            return "void"

        return self._decl_type_to_llvm(front_ctx.declType())

    def _get_function_parameters(self, front_ctx):
        params = []

        args_ctx = front_ctx.funcArgDecls()

        if args_ctx is None:
            return params

        for param_decl_ctx in args_ctx.singleVarDeclNoExps():
            param_type = self._decl_type_to_llvm(param_decl_ctx.declType())

            for identifier in param_decl_ctx.identifierList().IDENTIFIER():
                params.append({
                    "name": identifier.getText(),
                    "type": param_type
                })

        return params

    def _register_function_signature(self, func_ctx):
        front_ctx = func_ctx.funcFrontDecl()
        function_name = front_ctx.IDENTIFIER().getText()
        return_type = self._get_function_return_type(front_ctx)
        params = self._get_function_parameters(front_ctx)

        self.functions[function_name] = {
            "return_type": return_type,
            "params": params
        }

    def _register_all_functions(self, root_ctx):
        top_ctx = root_ctx.topDeclarationList()

        if top_ctx is None:
            return

        for func_ctx in top_ctx.funcDecl():
            self._register_function_signature(func_ctx)

    def _format_function_params_definition(self, params):
        formatted = []

        for param in params:
            formatted.append(f"{param['type']} %{param['name']}.arg")

        return ", ".join(formatted)

    def _format_function_params_call(self, argument_values):
        formatted = []

        for value in argument_values:
            formatted.append(f"{value.llvm_type} {value.value}")

        return ", ".join(formatted)

    def _get_decl_type_info(self, decl_type_ctx):
        """
        Devuelve información LLVM para tipos simples y arreglos.

        int      -> i32
        bool     -> i1
        [5]int   -> [5 x i32]
        """

        if decl_type_ctx is None:
            return {
                "kind": "simple",
                "llvm_type": "i32"
            }

        # Slice: []tipo
        if decl_type_ctx.sliceDeclType() is not None:
            slice_ctx = decl_type_ctx.sliceDeclType()
            element_info = self._get_decl_type_info(slice_ctx.declType())
            element_type = element_info["llvm_type"]

            return {
                "kind": "slice",
                "llvm_type": "slice",
                "element_type": element_type,
                "capacity": 100,
                "array_type": f"[100 x {element_type}]"
            }

        # Array: [n]tipo
        if decl_type_ctx.arrayDeclType() is not None:
            array_ctx = decl_type_ctx.arrayDeclType()
            size = int(self._normalize_int_literal(array_ctx.INTLITERAL().getText()))

            element_info = self._get_decl_type_info(array_ctx.declType())
            element_type = element_info["llvm_type"]

            return {
                "kind": "array",
                "llvm_type": f"[{size} x {element_type}]",
                "element_type": element_type,
                "size": size
            }

        type_text = decl_type_ctx.getText()

        if type_text == "bool":
            return {
                "kind": "simple",
                "llvm_type": "i1"
            }

        # Por ahora para LLVM tratamos int como i32.
        return {
            "kind": "simple",
            "llvm_type": "i32"
        }

    def _store_default_value(self, pointer, type_info):
        llvm_type = type_info["llvm_type"]

        if type_info["kind"] == "array":
            self.context.emit(
                f"  store {llvm_type} zeroinitializer, {llvm_type}* {pointer}"
            )
        elif llvm_type == "i1":
            self._store_value(pointer, llvm_type, "0")
        else:
            self._store_value(pointer, llvm_type, "0")

    def _get_simple_identifier_variable(self, expression_ctx):
        """
        Intenta obtener la variable si la expresión es solo un identificador:
        nums
        x
        """

        try:
            primary_ctx = expression_ctx.primaryExpression()
        except AttributeError:
            return None

        if primary_ctx is None:
            return None

        if primary_ctx.operand() is None:
            return None

        if len(primary_ctx.index()) > 0:
            return None

        if len(primary_ctx.selector()) > 0:
            return None

        if len(primary_ctx.arguments()) > 0:
            return None

        operand_ctx = primary_ctx.operand()

        if operand_ctx.IDENTIFIER() is None:
            return None

        name = operand_ctx.IDENTIFIER().getText()
        return self.context.get_variable(name)

    def _get_lvalue_info_from_primary(self, primary_ctx):
        if primary_ctx is None or primary_ctx.operand() is None:
            return None

        operand_ctx = primary_ctx.operand()

        if operand_ctx.IDENTIFIER() is None:
            return None

        name = operand_ctx.IDENTIFIER().getText()
        variable_info = self.context.get_variable(name)

        if variable_info is None:
            return None

        metadata = variable_info.get("metadata", {})

        # Variable simple: x
        if len(primary_ctx.index()) == 0:
            return variable_info

        # Array index: nums[0]
        if metadata.get("kind") == "array":
            return self._get_array_element_pointer(primary_ctx, variable_info)

        # Slice index: s[0]
        if metadata.get("kind") == "slice":
            return self._get_slice_element_pointer(primary_ctx, variable_info)

        return None

    def _decode_raw_string(self, text):
        """
        Recibe un raw string MiniGo con backticks:
        `Hola`

        Devuelve:
        Hola
        """
        if text.startswith("`") and text.endswith("`"):
            return text[1:-1]

        return text

    def _escape_llvm_string(self, text):
        """
        Convierte texto normal a formato válido para constante LLVM.
        """
        result = ""

        for char in text:
            code = ord(char)

            if char == "\\":
                result += "\\5C"
            elif char == '"':
                result += "\\22"
            elif char == "\n":
                result += "\\0A"
            elif char == "\r":
                result += "\\0D"
            elif char == "\t":
                result += "\\09"
            elif 32 <= code <= 126:
                result += char
            else:
                result += f"\\{code:02X}"

        # Agregamos salto de línea y cierre nulo.
        result += "\\0A\\00"

        return result

    def _create_global_string(self, raw_text):
        text = self._decode_raw_string(raw_text)
        escaped_text = self._escape_llvm_string(text)

        # Tamaño real: texto + salto línea + nulo.
        size = len(text.encode("utf-8")) + 2

        name = self.context.new_string_name()

        self.context.emit_global(
            f'{name} = private unnamed_addr constant [{size} x i8] c"{escaped_text}"'
        )

        return LLVMValue(
            value=f"getelementptr inbounds ([{size} x i8], [{size} x i8]* {name}, i32 0, i32 0)",
            llvm_type="i8*"
        )

    def _emit_print_string(self, value):
        self.context.emit(
            f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds '
            f'([4 x i8], [4 x i8]* @.fmt_str, i32 0, i32 0), i8* {value.value})'
        )

    def _create_slice_variable(self, name, type_info):
        """
        Representación simple para slices de int en LLVM:

        s.data -> [100 x i32]
        s.len  -> i32
        cap    -> 100
        """

        element_type = type_info["element_type"]
        capacity = type_info["capacity"]
        array_type = type_info["array_type"]

        data_pointer = f"%{name}.data"
        len_pointer = f"%{name}.len"

        self.context.emit(f"  {data_pointer} = alloca {array_type}")
        self.context.emit(f"  {len_pointer} = alloca i32")
        self.context.emit(f"  store i32 0, i32* {len_pointer}")

        self.context.define_variable(
            name,
            pointer=data_pointer,
            llvm_type="slice",
            metadata={
                "kind": "slice",
                "element_type": element_type,
                "capacity": capacity,
                "array_type": array_type,
                "data_pointer": data_pointer,
                "len_pointer": len_pointer
            }
        )

        return data_pointer

    # =====================================================
    # Visitors principales
    # =====================================================

    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    def visitFuncDecl(self, ctx):
        front_ctx = ctx.funcFrontDecl()
        function_name = front_ctx.IDENTIFIER().getText()

        signature = self.functions.get(function_name)

        if signature is None:
            return None

        return_type = signature["return_type"]
        params = signature["params"]

        # En LLVM, main debe retornar i32.
        llvm_function_return = return_type

        if function_name == "main":
            llvm_function_return = "i32"

        params_text = self._format_function_params_definition(params)

        self.context.emit(f"define {llvm_function_return} @{function_name}({params_text}) {{")

        self.context.enter_scope()

        previous_return_type = self.current_function_return_type
        previous_has_return = self.function_has_return

        self.current_function_return_type = llvm_function_return
        self.function_has_return = False

        # Guardar parámetros como variables locales.
        for param in params:
            pointer = self._create_alloca(param["name"], param["type"])
            self._store_value(pointer, param["type"], f"%{param['name']}.arg")

        self.visit(ctx.block().statementList())

        # Retorno por defecto si no hubo return explícito.
        if not self.function_has_return:
            if llvm_function_return == "void":
                self.context.emit("  ret void")
            else:
                self.context.emit("  ret i32 0")

        self.current_function_return_type = previous_return_type
        self.function_has_return = previous_has_return

        self.context.exit_scope()

        self.context.emit("}")
        self.context.emit("")

        return None

    def visitStatement(self, ctx):
        # println(expressionList?);
        if ctx.PRINTLN() is not None:
            if ctx.expressionList() is not None:
                for expression_ctx in ctx.expressionList().expression():
                    value = self.visit(expression_ctx)

                    if value.llvm_type == "i8*":
                        self._emit_print_string(value)
                    else:
                        self._emit_print_int(value)

            return None

        # return expression?;
        if ctx.RETURN() is not None:
            return self._generate_return_statement(ctx)

        return self.visitChildren(ctx)

    def _generate_return_statement(self, ctx):
        if ctx.expression() is None:
            self.context.emit("  ret void")
            self.function_has_return = True
            return None

        value = self.visit(ctx.expression())

        if self.current_function_return_type == "void":
            self.context.emit("  ret void")
        else:
            self.context.emit(f"  ret {value.llvm_type} {value.value}")

        self.function_has_return = True

        return None

    def visitVariableDecl(self, ctx):
        return self.visitChildren(ctx)

    def visitInnerVarDecls(self, ctx):
        return self.visitChildren(ctx)

    def visitSingleVarDeclNoExps(self, ctx):
        names = [identifier.getText() for identifier in ctx.identifierList().IDENTIFIER()]
        type_info = self._get_decl_type_info(ctx.declType())

        for name in names:
            if type_info["kind"] == "slice":
                self._create_slice_variable(name, type_info)
                continue

            llvm_type = type_info["llvm_type"]
            pointer = self._create_alloca(name, llvm_type, type_info)
            self._store_default_value(pointer, type_info)

        return None

    def visitSingleVarDecl(self, ctx):
        # Caso: var x int;
        # Caso: var nums [5]int;
        if ctx.singleVarDeclNoExps() is not None:
            return self.visit(ctx.singleVarDeclNoExps())

        names = [identifier.getText() for identifier in ctx.identifierList().IDENTIFIER()]

        expression_values = []

        if ctx.expressionList() is not None:
            for expression_ctx in ctx.expressionList().expression():
                expression_values.append(self.visit(expression_ctx))

        declared_type_info = None

        if ctx.declType() is not None:
            declared_type_info = self._get_decl_type_info(ctx.declType())

        for index, name in enumerate(names):
            if declared_type_info is not None:
                type_info = declared_type_info
            elif index < len(expression_values):
                type_info = {
                    "kind": "simple",
                    "llvm_type": expression_values[index].llvm_type
                }
            else:
                type_info = {
                    "kind": "simple",
                    "llvm_type": "i32"
                }

            if type_info["kind"] == "slice":
                self._create_slice_variable(name, type_info)
                continue

            llvm_type = type_info["llvm_type"]
            pointer = self._create_alloca(name, llvm_type, type_info)

            if index < len(expression_values) and type_info["kind"] == "simple":
                value = expression_values[index]
                self._store_value(pointer, llvm_type, value.value)
            else:
                self._store_default_value(pointer, type_info)

        return None

    # =====================================================
    # Expresiones mínimas
    # =====================================================

    def visitPrimaryExpressionOnly(self, ctx):
        return self.visit(ctx.primaryExpression())

    def visitPrimaryExpression(self, ctx):
        # append(...)
        if ctx.appendExpression() is not None:
            return self.visit(ctx.appendExpression())

        # len(...)
        if ctx.lengthExpression() is not None:
            return self.visit(ctx.lengthExpression())

        # cap(...)
        if ctx.capExpression() is not None:
            return self.visit(ctx.capExpression())

        # operand (selector | index | arguments)*
        if ctx.operand() is not None:
            if len(ctx.arguments()) > 0:
                return self._generate_function_call(ctx)

            if len(ctx.index()) > 0:
                element_info = self._get_lvalue_info_from_primary(ctx)

                if element_info is None:
                    return LLVMValue("0", "i32")

                return self._load_from_pointer(
                    element_info["pointer"],
                    element_info["type"]
                )

            return self.visit(ctx.operand())

        return LLVMValue("0", "i32")

    def visitOperand(self, ctx):
        if ctx.literal() is not None:
            return self.visit(ctx.literal())

        if ctx.IDENTIFIER() is not None:
            name = ctx.IDENTIFIER().getText()

            if name == "true":
                return LLVMValue("1", "i1")

            if name == "false":
                return LLVMValue("0", "i1")

            return self._load_variable(name)

        if ctx.expression() is not None:
            return self.visit(ctx.expression())

        return LLVMValue("0", "i32")

    def visitLiteral(self, ctx):
        if ctx.INTLITERAL() is not None:
            value = self._normalize_int_literal(ctx.INTLITERAL().getText())
            return LLVMValue(value, "i32")

        if ctx.RAWSTRINGLITERAL() is not None:
            return self._create_global_string(ctx.RAWSTRINGLITERAL().getText())

        return LLVMValue("0", "i32")

        return LLVMValue("0", "i32")

    def visitUnaryPlusExpression(self, ctx):
        return self.visit(ctx.expression())

    def visitUnaryMinusExpression(self, ctx):
        value = self.visit(ctx.expression())
        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = sub i32 0, {value.value}")
        return LLVMValue(temp, "i32")

    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.additiveOp().getText()

        temp = self.context.new_temp()

        if operator == "+":
            self.context.emit(f"  {temp} = add i32 {left.value}, {right.value}")
        elif operator == "-":
            self.context.emit(f"  {temp} = sub i32 {left.value}, {right.value}")
        else:
            self.context.emit(f"  {temp} = add i32 {left.value}, {right.value}")

        return LLVMValue(temp, "i32")

    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.multiplicativeOp().getText()

        temp = self.context.new_temp()

        if operator == "*":
            self.context.emit(f"  {temp} = mul i32 {left.value}, {right.value}")
        elif operator == "/":
            self.context.emit(f"  {temp} = sdiv i32 {left.value}, {right.value}")
        elif operator == "%":
            self.context.emit(f"  {temp} = srem i32 {left.value}, {right.value}")
        else:
            self.context.emit(f"  {temp} = mul i32 {left.value}, {right.value}")

        return LLVMValue(temp, "i32")

    def visitLengthExpression(self, ctx):
        variable_info = self._get_simple_identifier_variable(ctx.expression())

        if variable_info is None:
            return LLVMValue("0", "i32")

        metadata = variable_info.get("metadata", {})

        if metadata.get("kind") == "array":
            return LLVMValue(str(metadata["size"]), "i32")

        if metadata.get("kind") == "slice":
            len_pointer = metadata["len_pointer"]
            return self._load_from_pointer(len_pointer, "i32")

        return LLVMValue("0", "i32")

    def visitNonEmptySimpleStatement(self, ctx):
        # assignmentStatement
        if ctx.assignmentStatement() is not None:
            return self.visit(ctx.assignmentStatement())

        # expressionList := expressionList
        # Para LLVM lo tratamos como declaración local inferida int.
        if ctx.DECLARE_ASSIGN() is not None:
            return self._generate_short_variable_declaration(ctx)

        # x++ / x--
        if ctx.INC() is not None or ctx.DEC() is not None:
            return self._generate_increment_decrement(ctx)

        # expression como statement, por ejemplo llamada a función.
        if ctx.expression() is not None:
            return self.visit(ctx.expression())

        return None

    def visitCapExpression(self, ctx):
        variable_info = self._get_simple_identifier_variable(ctx.expression())

        if variable_info is None:
            return LLVMValue("0", "i32")

        metadata = variable_info.get("metadata", {})

        if metadata.get("kind") == "array":
            return LLVMValue(str(metadata["size"]), "i32")

        if metadata.get("kind") == "slice":
            return LLVMValue(str(metadata["capacity"]), "i32")

        return LLVMValue("0", "i32")

    def visitAppendExpression(self, ctx):
        variable_info = self._get_simple_identifier_variable(ctx.expression(0))

        if variable_info is None:
            return LLVMValue("0", "slice")

        metadata = variable_info.get("metadata", {})

        if metadata.get("kind") != "slice":
            return LLVMValue("0", "slice")

        value = self.visit(ctx.expression(1))

        len_pointer = metadata["len_pointer"]
        data_pointer = metadata["data_pointer"]
        array_type = metadata["array_type"]
        element_type = metadata["element_type"]

        current_len = self._load_from_pointer(len_pointer, "i32")

        element_pointer = self.context.new_temp()

        self.context.emit(
            f"  {element_pointer} = getelementptr inbounds "
            f"{array_type}, {array_type}* {data_pointer}, "
            f"i32 0, i32 {current_len.value}"
        )

        self.context.emit(
            f"  store {element_type} {value.value}, {element_type}* {element_pointer}"
        )

        new_len = self.context.new_temp()
        self.context.emit(f"  {new_len} = add i32 {current_len.value}, 1")
        self.context.emit(f"  store i32 {new_len}, i32* {len_pointer}")

        return LLVMValue(variable_info["pointer"], "slice")

    def _generate_short_variable_declaration(self, ctx):
        left_expressions = ctx.expressionList(0).expression()
        right_expressions = ctx.expressionList(1).expression()

        for index, left_expr in enumerate(left_expressions):
            primary_ctx = left_expr.primaryExpression()
            name = primary_ctx.operand().IDENTIFIER().getText()

            value = self.visit(right_expressions[index])

            pointer = self._create_alloca(name, value.llvm_type)
            self._store_value(pointer, value.llvm_type, value.value)

        return None

    def _generate_increment_decrement(self, ctx):
        variable_info = self._get_lvalue_info(ctx.expression())

        if variable_info is None:
            return None

        pointer = variable_info["pointer"]
        llvm_type = variable_info["type"]

        old_value = self._load_from_pointer(pointer, llvm_type)

        temp = self.context.new_temp()

        if ctx.INC() is not None:
            self.context.emit(f"  {temp} = add {llvm_type} {old_value.value}, 1")
        else:
            self.context.emit(f"  {temp} = sub {llvm_type} {old_value.value}, 1")

        self._store_value(pointer, llvm_type, temp)

        return None

    def visitAssignmentStatement(self, ctx):
        # expressionList = expressionList
        if ctx.ASSIGN() is not None:
            return self._generate_normal_assignment(ctx)

        # expression += expression, expression -= expression, etc.
        return self._generate_compound_assignment(ctx)

    def _generate_normal_assignment(self, ctx):
        left_expressions = ctx.expressionList(0).expression()
        right_expressions = ctx.expressionList(1).expression()

        for index, left_expr in enumerate(left_expressions):
            variable_info = self._get_lvalue_info(left_expr)

            if variable_info is None:
                continue

            pointer = variable_info["pointer"]
            llvm_type = variable_info["type"]

            value = self.visit(right_expressions[index])

            # Caso: s = append(s, 10)
            # append ya modifica el slice internamente.
            if value.llvm_type == "slice":
                continue

            self._store_value(pointer, llvm_type, value.value)

        return None

    def _generate_compound_assignment(self, ctx):
        variable_info = self._get_lvalue_info(ctx.expression(0))

        if variable_info is None:
            return None

        pointer = variable_info["pointer"]
        llvm_type = variable_info["type"]

        current_value = self._load_from_pointer(pointer, llvm_type)
        right_value = self.visit(ctx.expression(1))

        operator = ctx.assignmentOp().getText()

        if operator == "+=":
            result = self._emit_binary_int_op("+", current_value, right_value)
        elif operator == "-=":
            result = self._emit_binary_int_op("-", current_value, right_value)
        elif operator == "*=":
            result = self._emit_binary_int_op("*", current_value, right_value)
        elif operator == "/=":
            result = self._emit_binary_int_op("/", current_value, right_value)
        elif operator == "%=":
            result = self._emit_binary_int_op("%", current_value, right_value)
        else:
            # Operadores bitwise los dejamos para después.
            result = current_value

        self._store_value(pointer, llvm_type, result.value)

        return None

    def visitRelationalExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.relationalOp().getText()

        return self._emit_compare_int(operator, left, right)

    def visitUnaryNotExpression(self, ctx):
        value = self.visit(ctx.expression())

        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = xor i1 {value.value}, true")

        return LLVMValue(temp, "i1")

    def visitLogicalAndExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = and i1 {left.value}, {right.value}")

        return LLVMValue(temp, "i1")

    def visitLogicalOrExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = or i1 {left.value}, {right.value}")

        return LLVMValue(temp, "i1")

    def visitIfStatement(self, ctx):
        """
        Genera LLVM para:

        if condition { ... };
        if condition { ... } else { ... };
        if condition { ... } else if ...;
        """

        self.context.enter_scope()

        if ctx.nonEmptySimpleStatement() is not None:
            self.visit(ctx.nonEmptySimpleStatement())

        condition = self.visit(ctx.expression())

        then_label = self.context.new_label("if_then")
        else_label = self.context.new_label("if_else")
        end_label = self.context.new_label("if_end")

        self.context.emit(
            f"  br i1 {condition.value}, "
            f"label {self._label_ref(then_label)}, "
            f"label {self._label_ref(else_label)}"
        )

        # THEN
        self.context.emit(f"{then_label}:")
        self.context.enter_scope()
        self.visit(ctx.block(0).statementList())
        self.context.exit_scope()
        self.context.emit(f"  br label {self._label_ref(end_label)}")

        # ELSE
        self.context.emit(f"{else_label}:")
        self.context.enter_scope()

        if ctx.ifStatement() is not None:
            self.visit(ctx.ifStatement())
        elif len(ctx.block()) > 1:
            self.visit(ctx.block(1).statementList())

        self.context.exit_scope()
        self.context.emit(f"  br label {self._label_ref(end_label)}")

        # END
        self.context.emit(f"{end_label}:")

        self.context.exit_scope()

        return None

    def _branch_to(self, label):
        self.context.emit(f"  br label {self._label_ref(label)}")

    def _emit_label(self, label):
        self.context.emit(f"{label}:")

    def _get_loop_simple_statements(self, ctx):
        """
        En la gramática, el for puede tener hasta dos simple statements:
        for init; condition; update { ... }
        """
        statements = ctx.nonEmptySimpleStatement()

        if statements is None:
            return []

        # ANTLR normalmente devuelve lista cuando hay varias ocurrencias.
        if isinstance(statements, list):
            return statements

        return [statements]

    def visitLoop(self, ctx):
        """
        Genera LLVM para:

        for { ... }
        for condition { ... }
        for init; condition; update { ... }

        Nota: break y continue no se generan en esta etapa.
        """

        self.context.enter_scope()

        simple_statements = self._get_loop_simple_statements(ctx)

        # Caso 1:
        # for { ... }
        if ctx.expression() is None and len(simple_statements) == 0:
            start_label = self.context.new_label("for_start")
            body_label = self.context.new_label("for_body")

            self._branch_to(start_label)

            self._emit_label(start_label)
            self._branch_to(body_label)

            self._emit_label(body_label)
            self.context.enter_scope()
            self.visit(ctx.block().statementList())
            self.context.exit_scope()
            self._branch_to(start_label)

            self.context.exit_scope()
            return None

        # Caso 2:
        # for condition { ... }
        if ctx.expression() is not None and len(simple_statements) == 0:
            condition_label = self.context.new_label("for_cond")
            body_label = self.context.new_label("for_body")
            end_label = self.context.new_label("for_end")

            self._branch_to(condition_label)

            self._emit_label(condition_label)
            condition = self.visit(ctx.expression())
            self.context.emit(
                f"  br i1 {condition.value}, "
                f"label {self._label_ref(body_label)}, "
                f"label {self._label_ref(end_label)}"
            )

            self._emit_label(body_label)
            self.context.enter_scope()
            self.visit(ctx.block().statementList())
            self.context.exit_scope()
            self._branch_to(condition_label)

            self._emit_label(end_label)

            self.context.exit_scope()
            return None

        # Caso 3:
        # for init; condition; update { ... }
        init_stmt = simple_statements[0] if len(simple_statements) >= 1 else None
        update_stmt = simple_statements[1] if len(simple_statements) >= 2 else None

        condition_label = self.context.new_label("for_cond")
        body_label = self.context.new_label("for_body")
        update_label = self.context.new_label("for_update")
        end_label = self.context.new_label("for_end")

        # init
        if init_stmt is not None:
            self.visit(init_stmt)

        self._branch_to(condition_label)

        # condition
        self._emit_label(condition_label)

        if ctx.expression() is not None:
            condition = self.visit(ctx.expression())
            self.context.emit(
                f"  br i1 {condition.value}, "
                f"label {self._label_ref(body_label)}, "
                f"label {self._label_ref(end_label)}"
            )
        else:
            # for init; ; update { ... } se toma como condición true
            self._branch_to(body_label)

        # body
        self._emit_label(body_label)
        self.context.enter_scope()
        self.visit(ctx.block().statementList())
        self.context.exit_scope()
        self._branch_to(update_label)

        # update
        self._emit_label(update_label)

        if update_stmt is not None:
            self.visit(update_stmt)

        self._branch_to(condition_label)

        # end
        self._emit_label(end_label)

        self.context.exit_scope()
        return None

    def _get_primary_identifier_name(self, primary_ctx):
        operand_ctx = primary_ctx.operand()

        if operand_ctx is None:
            return None

        if operand_ctx.IDENTIFIER() is None:
            return None

        return operand_ctx.IDENTIFIER().getText()

    def _generate_function_call(self, primary_ctx):
        function_name = self._get_primary_identifier_name(primary_ctx)

        if function_name is None:
            return LLVMValue("0", "i32")

        signature = self.functions.get(function_name)

        if signature is None:
            return LLVMValue("0", "i32")

        return_type = signature["return_type"]
        arguments_ctx = primary_ctx.arguments(0)

        argument_values = []

        if arguments_ctx.expressionList() is not None:
            for expression_ctx in arguments_ctx.expressionList().expression():
                argument_values.append(self.visit(expression_ctx))

        params_text = self._format_function_params_call(argument_values)

        # Procedimiento sin retorno
        if return_type == "void":
            self.context.emit(f"  call void @{function_name}({params_text})")
            return LLVMValue("0", "void")

        # Función con retorno
        temp = self.context.new_temp()
        self.context.emit(f"  {temp} = call {return_type} @{function_name}({params_text})")

        return LLVMValue(temp, return_type)

    def _get_array_element_pointer(self, primary_ctx, variable_info):
        metadata = variable_info.get("metadata", {})

        if metadata.get("kind") != "array":
            return None

        # Por ahora soportamos un índice: nums[0]
        index_ctx = primary_ctx.index(0)
        index_value = self.visit(index_ctx.expression())

        array_type = variable_info["type"]
        array_pointer = variable_info["pointer"]
        element_type = metadata["element_type"]

        element_pointer = self.context.new_temp()

        self.context.emit(
            f"  {element_pointer} = getelementptr inbounds "
            f"{array_type}, {array_type}* {array_pointer}, "
            f"i32 0, i32 {index_value.value}"
        )

        return {
            "pointer": element_pointer,
            "type": element_type,
            "metadata": {
                "kind": "simple"
            }
        }

    def _get_slice_element_pointer(self, primary_ctx, variable_info):
        metadata = variable_info.get("metadata", {})

        if metadata.get("kind") != "slice":
            return None

        index_ctx = primary_ctx.index(0)
        index_value = self.visit(index_ctx.expression())

        array_type = metadata["array_type"]
        data_pointer = metadata["data_pointer"]
        element_type = metadata["element_type"]

        element_pointer = self.context.new_temp()

        self.context.emit(
            f"  {element_pointer} = getelementptr inbounds "
            f"{array_type}, {array_type}* {data_pointer}, "
            f"i32 0, i32 {index_value.value}"
        )

        return {
            "pointer": element_pointer,
            "type": element_type,
            "metadata": {
                "kind": "simple"
            }
        }