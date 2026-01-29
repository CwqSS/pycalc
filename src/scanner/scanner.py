from src.scanner.ParenthesesStack import ParenthesesStack as PStack
from src.expression.constants import OPERATORS

class Scanner:
    def __init__(self):
        self.stack = PStack()

    def scan(self, char_expression: str) -> list[str]:
        index = 0
        length = len(char_expression)

        new_expression = char_expression

        print("Expression: ", char_expression)
        print("length: ", length)

        while index < length:
            text = char_expression[index]

            if text == "(" or text == ")":
                if (index != 0 and text == "(" and char_expression[index - 1].isnumeric()) or (index != length - 1 and text == ")" and char_expression[index + 1].isnumeric()):
                    raise Exception("Deve haver um operador entre parentêses e um número fora dele.")

                self.stack.push(text)
                index += 1 
            elif self.isAnOperator(text):
                if text == "*" and char_expression[index + 1] == "-":
                    pass
                elif(self.isAnOperator(char_expression[index + 1])):
                    raise Exception("Erro: operador demais")
                index += 1
                continue
            elif text.isnumeric():
                index += 1
                while (index < length) and (char_expression[index].isnumeric() or char_expression[index] == "."):
                    text += char_expression[index]
                    index += 1
            else:
                raise Exception("Caracter não aceito: ", text)

        if(not self.stack.isEmpty()):
            raise Exception("Má formatação de parentêses.")

        return True

    def isAnOperator(self, text):
        return text in OPERATORS