from src.scanner.Scanner import Scanner
from src.parser.Parser import Parser

scanner = Scanner()
expression = "9 / 0".replace(" ", "")

scanner.scan(expression)

Tree = Parser().parse2(expression)

print("Expressão: ", end="")
Tree.display()
print("")
print("Resultado: ", Tree.calculate())




