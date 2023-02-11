from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from final_win import FinalWin
from instr import *


class Experiment:
    def __init__(self, age, test1, test2, test3):
       self.age = int(age)
       self.t1 = int(test1)
       self.t2 = int(test2)
       self.t3 = int(test3)


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
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
        self.btn_next = QPushButton(txt_sendresults)
        self.line_name = QLineEdit("Ф.И.О.")
        self.line_age = QLineEdit("0")
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.text_timer = QLabel("00:00:00")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(17, 33, 105)")

        # Добавление кнопок, полей и текста
        # Имя пользователя
        self.l_line.addWidget(QLabel(txt_hintname), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft)

        # Возраст пользователя
        self.l_line.addWidget(QLabel(txt_hintage), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft)

        # Первый тест
        self.l_line.addWidget(QLabel(txt_test1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment=Qt.AlignLeft)

        # Второй тест
        self.l_line.addWidget(QLabel(txt_test2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)

        # Третий тест
        self.l_line.addWidget(QLabel(txt_test3), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment=Qt.AlignLeft)

        # Таймер справа
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)

        # Кнопка для перехода на следующее окно.
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        # Объединение лейаутов (в горизонтальный)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_event1)
        self.btn_test2.clicked.connect(self.timer_event2)
        self.btn_test3.clicked.connect(self.timer_event3)

    def timer_event1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_1_updater)
        self.timer.start(1000)
        
    def timer_event2(self):
       global time
       time = QTime(0, 0, 30)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer_2_updater)
       #одно приседание в 1.5 секунды
       self.timer.start(1500)
    
    def timer_event3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_3_updater)
        self.timer.start(1000)
    
    def timer_1_updater(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(17, 33, 105)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_2_updater(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("s"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(17, 33, 105)")
        if time.toString("s") == "0":
            self.timer.stop()
    
    def timer_3_updater(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.text_timer.setStyleSheet("color: rgb(17, 33, 105)")
            self.timer.stop()
        elif (45 <= int(time.toString("hh:mm:ss")[-2:]) <= 60) or (0 < int(time.toString("hh:mm:ss")[-2:]) <= 15):
            self.text_timer.setStyleSheet("color: rgb(10, 255, 10)")
        elif 15 < int(time.toString("hh:mm:ss")[-2:]) < 45:
            self.text_timer.setStyleSheet("color: rgb(10, 10, 10)")
        
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_test1.text(),
                              self.line_test2.text(), self.line_test3.text())
        self.fw = FinalWin(self.exp)  # Создание следующего окна


def debug():
    debug_app = QApplication([])
    debug_win = TestWin()
    debug_win.show()
    debug_app.exec_()


if __name__ == "__main__":
    debug()
