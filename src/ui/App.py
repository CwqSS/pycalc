from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton, QWidget, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy
import re
from src.scanner.scanner import Scanner
from src.parser.FakeParser import FakeParser


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Pycalc")
    self.setFixedSize(325, 500)

    self.label_layout = self.create_main_label()
    self.buttons_layout = self.create_number_buttons()

    final_layout = QVBoxLayout()
    final_layout.addLayout(self.label_layout, stretch=3)
    final_layout.addLayout(self.buttons_layout, stretch=7)


    container = QWidget()
    container.setLayout(final_layout)
    container.setContentsMargins(0,0,0,0)
    self.setContentsMargins(0,0,0,0)
    self.setCentralWidget(container)

  def create_number_buttons(self) -> QGridLayout:
    # 0 to 9 buttons
    layout = QGridLayout()
    layout.setSpacing(0)
    layout.setContentsMargins(0,0,0,0)
    layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
    buttons = {
      '7': (1, 0),
      '8': (1, 1),
      '9': (1, 2),
      '4': (2, 0),
      '5': (2, 1),
      '6': (2, 2),
      '1': (3, 0),
      '2': (3, 1),
      '3': (3, 2),
      '+/-': (4,0),
      '0': (4, 1),
      ',': (4, 2),
      '=': (4, 3),
      '+': (3, 3),
      '-': (2, 3),
      '*': (1, 3),
      'C': (0,1),
      '/': (0,2),
      '⌫': (0,3)

    }

    for number, (row, col) in buttons.items():
      btn = QPushButton(str(number))
      btn.setMaximumHeight(85)
      btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
      btn_font = btn.font()
      btn_font.setPointSize(20)
      btn.setFont(btn_font)
      btn.clicked.connect(self.on_number_clicked)
      if btn.text() == '=': btn.setStyleSheet("background-color: aqua; color: black;")
      elif btn.text() == '⌫' or btn.text() == 'C': 
        btn.setStyleSheet("background-color: red; color: white;")
      layout.addWidget(btn, row, col)

    return layout
  
  def on_number_clicked(self):
    btn = self.sender()
    txt = self.label.text()
    newText = self.treat_calculator_string(txt, btn.text())
    self.label.setText(newText)
    self.small_label.setText(newText)
    print(newText)

  def create_main_label(self) -> QLabel:
    self.label = QLabel()
    self.errorLabel = QLabel()
    self.label.setText("0")
    font = self.label.font()
    font.setPointSize(25)
    self.label.setFont(font)
    # self.label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.label.setAlignment(Qt.AlignmentFlag.AlignRight)

    self.small_label = QLabel()
    self.small_label.setText("0")
    font = self.small_label.font()
    font.setPointSize(12)
    self.small_label.setFont(font)
    self.small_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.small_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
    self.small_label.setWordWrap(True)

    errorfont = self.errorLabel.font()
    errorfont.setPointSize(12)
    self.errorLabel.setFont(errorfont)
    self.errorLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
    self.errorLabel.setWordWrap(True)


    layout = QVBoxLayout()
    layout.addWidget(self.small_label)
    layout.addWidget(self.errorLabel)
    layout.addWidget(self.label)

    return layout
  
  def treat_calculator_string(self, txt: str, btn_txt: str) -> str:

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['-', '+', '*', '/', '(', ')']

    resultado = None

    if btn_txt == '+/-':
      if txt.startswith('-'): return txt[1:]
      if txt == '': return '- 0'  
      else: return '-' + txt

    if btn_txt in numbers:  
      if btn_txt != ',' and txt == '0': return btn_txt # substitui o primeiro 0
      if len(txt) == 0: return btn_txt
      if txt[-1] in operators: return txt + ' ' + btn_txt
      return txt + btn_txt # add oq passar
    
    if btn_txt == ',':
      pedacos = re.split(r"([+\-*/])", txt)
      print(pedacos)
      if len(txt) == 0: return '0,'
      if ',' in pedacos[-1]: return txt # ignora mais de uma virgula por pedaço
      if txt[-1] in operators: return txt + '0' + btn_txt
      return txt + btn_txt
    
    if btn_txt in operators:
      if txt[-1] == "/" or txt[-1] == '*' and btn_txt == '-': return txt + " " + btn_txt
      if txt.endswith(',') or len(txt) == 0: return txt + '0 ' + btn_txt
      if txt[-1] in operators: return txt[0:-1] + btn_txt
      return txt + " " + btn_txt
    
    if btn_txt == '⌫':
      return txt[:-1]
    
    if btn_txt == 'C':
      return "0"
    
    if btn_txt == '=':
      try:
          self.errorLabel.setText("")
          calc = Scanner()
          formatted_text = txt.replace(' ', '')
          try: 
            isOk = calc.scan(formatted_text.replace(",", "."))
          except Exception as e:
            raise Exception("conta mal escrita")
          if isOk:
            parser = FakeParser()
            return str(parser.parse(formatted_text.replace(",", ".")).calculate()).replace(".", ",")
      except Exception as e:
          self.errorLabel.setText(str(e))
          return txt
    print("fora...")
    return txt + btn_txt


  









# You need one (and only one) QApplication instance per application.
app = QApplication([])
window = MainWindow()
window.show()
app.exec()