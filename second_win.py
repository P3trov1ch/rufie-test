from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from time import time, sleep
from instr import *
from final_win import FinalWin


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # Создание лейаутов
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        # Создание кнопок и полей для ввода
        self.btn_next = QPushButton("Отправить результаты")
        self.hintname = QLineEdit()
        self.hintage = QLineEdit()
        self.test1 = QPushButton("Начать первый тест")
        self.test2 = QPushButton("Начать делать приседания")
        self.test3 = QPushButton("Начать финальный тест")
        self.result1 = QLineEdit("0")
        self.result2 = QLineEdit("0")
        self.result3 = QLineEdit("0")
        self.text_timer = QLabel("00:00:00")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(17, 33, 105)")

        # Добавление кнопок, полей и текста
        # Имя пользователя
        self.l_line.addWidget(QLabel(txt_hintname), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hintname, alignment=Qt.AlignLeft)

        # Возраст пользователя
        self.l_line.addWidget(QLabel(txt_hintage), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hintage, alignment=Qt.AlignLeft)

        # Первый тест
        self.l_line.addWidget(QLabel(txt_test1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.result1, alignment=Qt.AlignLeft)

        # Второй тест
        self.l_line.addWidget(QLabel(txt_test2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment=Qt.AlignLeft)

        # Третий тест
        self.l_line.addWidget(QLabel(txt_test3), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment=Qt.AlignLeft)

        # Ввод пользоватетем результатов
        self.l_line.addWidget(self.result2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.result3, alignment=Qt.AlignLeft)

        # Кнопка для перехода на следующее окно.
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        # Таймер справа
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)

        # Объединение лейаутов (в горизонтальный)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.test1.clicked.connect(self.timer_event1)
        self.test2.clicked.connect(self.timer_sits)
        self.test3.clicked.connect(self.timer_event3)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()  # Создание следующего окна

    def timer_event1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_updater)
        self.timer.start(1000)
    
    def timer_event3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_updater)
        self.timer.start(1000)
    
    def timer_updater(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(17, 33, 105)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits():
        pass

def debug():
    debug_app = QApplication([])
    debug_win = TestWin()
    debug_win.show()
    debug_app.exec_()


if __name__ == "__main__":
    debug()
