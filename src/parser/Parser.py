from src.expression.ExpressionTree import ExpressionTree
from src.expression.ExpressionNode import ExpressionNode
from src.expression.OperatorNode import OperatorNode
from src.expression.NumberNode import NumberNode
from src.expression.constants import  OPERATORS, LOWEST_PRIORITY_OPERATORS, HIGHEST_PRIORITY_OPERATORS

class Parser:
    def __init__(self):
        self.tree = ExpressionTree()

    def parse(self, expression: str) -> ExpressionTree :
        self.tree.root = ExpressionNode(expression)
        self.depth = 0
        self.transform(self.tree.root)
        return self.tree

    def transform(self, root: ExpressionNode, depth = 0, left = False):
        expression = root.value
        index = self.find_lowest_operator(expression)
        if index > -1:
            root.left = ExpressionNode(expression[0:index])
            root.right = ExpressionNode(expression[index+1:])
            root.left.parent = root
            root.right.parent = root
            root.value = expression[index]
            self.transform(root.left, depth = depth + 1, left= True)
            self.transform(root.right, depth = depth + 1)

    def parse2(self, expression: str) -> ExpressionTree :
        self.tree.root = self.transform2(expression)
        return self.tree
    
        
    def transform2(self, expression):
        index = self.find_lowest_operator(expression)
        if index > -1:
            node = OperatorNode(expression[index])
            node.left = self.transform2(expression[0:index])
            node.right = self.transform2(expression[index+1:])
            node.left.parent = node
            node.right.parent = node
            return node
        else:
            return NumberNode(expression)

    def find_lowest_operator(self, expression: str) -> str:
        index = len(expression) - 1
        while index > -1:
            if expression[index] in LOWEST_PRIORITY_OPERATORS:
                return index
            index -= 1

        index = len(expression) - 1
        while index > -1:
            if expression[index] in HIGHEST_PRIORITY_OPERATORS:
                return index
            index -= 1

        return index