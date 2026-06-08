class LLVMValue:
    def __init__(self, value, llvm_type):
        self.value = value
        self.llvm_type = llvm_type

    def __str__(self):
        return self.value