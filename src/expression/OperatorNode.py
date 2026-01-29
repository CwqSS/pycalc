from src.expression.ExpressionNode import ExpressionNode
from src.expression.constants import OPERATORS


class OperatorNode(ExpressionNode):
    def __init__(self, operator):
        super().__init__(operator)
        if(operator not in OPERATORS):
            raise Exception("Operador não suportado")
        self.strategy = OPERATORS.get(operator)
    
    def calculate(self):
        return self.strategy.execute(self)
