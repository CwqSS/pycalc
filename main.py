from src.scanner.Scanner import Scanner
from src.parser.FakeParser import FakeParser

scanner = Scanner()
expression = "3 ^ 2 ^ 2".replace(" ", "")

scanner.scan(expression)

Tree = FakeParser().parse(expression)

print("Resultado: ", Tree.calculate())




