from src.expression.ExpressionNode import ExpressionNode

class NumberNode(ExpressionNode):
    def __init__(self, value):
        super().__init__(float(value))

    def calculate(self):
        return self.value
