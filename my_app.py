from second_win import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *

class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядить окно
        self.initUI() # создаём и настраеваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show() # старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # описание элементов
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
main_win = Mainwin()
main_win.initUI()
main_win.show()
app.exec_()
