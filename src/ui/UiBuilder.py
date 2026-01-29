from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QBoxLayout, QGridLayout
from PySide6.QtCore import Qt

class UiBuilder:
  def create_number_buttons(self) -> QGridLayout:
    # 0 to 9 buttons
    layout = QGridLayout()
    layout.setSpacing(0)
    layout.setContentsMargins(0,0,0,0)
    # layout.alignment(Qt.AlignmentFlag.AlignLeading)
    buttons = {
        7: (0, 0),
        8: (0, 1),
        9: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        1: (2, 0),
        2: (2, 1),
        3: (2, 2),
        0: (3, 1),
        ',': (3, 3) 
    }

    for number, (row, col) in buttons.items():
      btn = QPushButton(str(number))
      btn.setMaximumHeight(1000)
      btn.clicked.connect(self.on_number_clicked)
      layout.addWidget(btn, row, col)

    return layout
  
  def on_number_clicked(self):
    print("clicked...")

  def create_main_label(self) -> QLabel:
    label = QLabel()
    label.setText("Ayaya")
    font = label.font()
    font.setPointSize(25)
    label.setFont(font)
    label.setMaximumHeight(50)

    return label