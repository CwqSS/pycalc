from src.scanner.Scanner import Scanner
from src.parser.FakeParser import FakeParser

scanner = Scanner()
expression = "-8 * 9".replace(" ", "")

scanner.scan(expression)

Tree = FakeParser().parse(expression)

print("Resultado: ", Tree.calculate())




