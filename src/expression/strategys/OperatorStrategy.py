from abc import ABC, abstractmethod
from src.expression.ExpressionNode import ExpressionNode

class OperatorStrategy(ABC):
    @abstractmethod
    def execute(self, node: ExpressionNode):
        pass

class AdditionStrategy(OperatorStrategy):
    def execute(self, node: ExpressionNode):
        return node.left.calculate() + node.right.calculate()

class SubtractionStrategy(OperatorStrategy):
    def execute(self, node: ExpressionNode):
        return node.left.calculate() - node.right.calculate()

class MultiplicationStrategy(OperatorStrategy):
    def execute(self, node: ExpressionNode):
        return node.left.calculate() * node.right.calculate()

class DivisionStrategy(OperatorStrategy):
    def execute(self, node: ExpressionNode):
        if(node.right.calculate() == 0):
            raise Exception("Não é possível dividir por 0")

        return node.left.calculate() / node.right.calculate()

