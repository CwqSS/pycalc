from src.expression.ExpressionTree import ExpressionTree
from src.expression.ExpressionNode import ExpressionNode
from src.expression.OperatorNode import OperatorNode
from src.expression.NumberNode import NumberNode
from src.expression.constants import  OPERATORS, LOWEST_PRIORITY_OPERATORS, HIGHEST_PRIORITY_OPERATORS, GOD_PRIORITY_OPERATORS, OPERATORS_PRIORITY


class FakeParser:
    def __init__(self):
        self.tree = ExpressionTree()

    def parse(self, expression: str) -> ExpressionTree :
        new_expression = self.remake_expression(expression)
        self.tree.root = self.transform(new_expression)
        # self.tree.root = self.transform(expression)
        return self.tree

    def remake_expression(self, expression:str):
        new_expression = expression
        while "(" in new_expression:
            parentheses = self.find_parentheses(new_expression)
            item = parentheses[0]
            sub_expression = new_expression[item["start"]:item["end"]+1]
            node = self.transform(sub_expression[1:-1])
            new_expression = new_expression.replace(sub_expression, str(node.calculate()), 1)
        return new_expression

    def transform(self, expression:str, root = None):


        index = self.find_lowest_operator(expression)      
        if index > -1:
            node = OperatorNode(expression[index])
            node.left = self.transform(expression[0:index])
            node.right = self.transform(expression[index+1:])
            node.left.parent = node
            node.right.parent = node
            return node
        elif expression != "":
            return NumberNode(expression)
        else: 
            return None
    
    def find_parentheses(self, expression):
        stack = []
        indexes = []
        i = len(expression) - 1
        while i > -1:
            if expression[i] ==")":
                stack.append(i)
            elif expression[i] == "(":
                last = stack.pop()
                indexes.append({"start": i, "end": last})
            i -= 1

        indexes.sort(key=lambda c: c["end"] - c["start"], reverse=False)
        return indexes

    def find_some_parenthesis(self, expression):
        stack = []
        indexes = []
        i = len(expression) - 1
        while i > -1:
            if expression[i] ==")":
                stack.append(expression[i])
                if len(indexes) == 0:
                    indexes.append(i) 
            elif expression[i] == "(":
                stack.pop()
                if(len(stack) == 0):
                    indexes.append(i)
                    indexes.reverse()
                    return indexes
            i -= 1
        return indexes

    def resolve_parenthesis(self, expression):
        indexes = self.find_some_parenthesis(expression)
        if len(indexes) == 2:
            right_node:ExpressionNode = self.transform(expression[indexes[0] + 1 : indexes[1]])

            leftExpression  = expression[0: indexes[0]]
            left_index = self.find_last_operator(leftExpression)
            
            if(left_index == -1):
                return [right_node, indexes]

            node = OperatorNode(expression[left_index])
            node.right = right_node
            node.left = self.transform(expression[0:left_index])

            return [node, indexes]
        return None

    def find_last_operator(self, expression):
        index = len(expression) - 1
        while index > -1:
            if expression[index] in OPERATORS:
                return index
            index -=1
        return -1
    
    def find_first_operator(self, expression):
        index = 0
        while index < len(expression):
            if expression[index] in OPERATORS:
                print("INDEX:", expression[index])
                return index
            index +=1
        return -1

    def find_lowest_operator(self, expression: str) -> str:
        lists = [LOWEST_PRIORITY_OPERATORS, HIGHEST_PRIORITY_OPERATORS, GOD_PRIORITY_OPERATORS]
        for item in lists:
            index = self.find_in_list(expression, item)
            if(index != -1):
                return index
        return -1
    
    def find_in_list(self, expression, list):
        index = len(expression) - 1
        while index > -1:
            if expression[index] in list:
                return index
            index -= 1
        return -1