class LLVMContext:
    def __init__(self):
        self.lines = []
        self.global_lines = []
        self.temp_counter = 0
        self.label_counter = 0
        self.string_counter = 0
        self.scopes = [{}]

    def emit(self, line=""):
        self.lines.append(line)

    def new_temp(self):
        self.temp_counter += 1
        return f"%t{self.temp_counter}"

    def new_label(self, base="label"):
        self.label_counter += 1
        return f"{base}{self.label_counter}"

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def define_variable(self, name, pointer, llvm_type, metadata=None):
        self.scopes[-1][name] = {
            "pointer": pointer,
            "type": llvm_type,
            "metadata": metadata or {}
        }

    def get_variable(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]

        return None

    def get_code(self):
        return "\n".join(self.lines)

    def emit_global(self, line=""):
        self.global_lines.append(line)

    def new_string_name(self):
        self.string_counter += 1
        return f"@.str{self.string_counter}"

    def get_code(self):
        return "\n".join(self.global_lines + [""] + self.lines)