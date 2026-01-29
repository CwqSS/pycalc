class ExpressionNode():
    def __init__(self, value):
        self.left: ExpressionNode = None
        self.right: ExpressionNode = None
        self.parent: ExpressionNode = None
        self.value = value

    def calculate(self):
        pass
    
    def display(self):
        print(self.value, end="")