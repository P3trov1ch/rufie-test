from instr import*
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.unitUI()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def unitUI(self):
        self.index=QLabel(txt_index)
        self.working=QLabel(txt_workheart)
        self.line=QVBoxLayout()
        self.index.addWidget(self.line)
        self.working.addWidget(self.line)
        self.setLayout(self.line)

app=QApplication([])
mw=FinalWin()
mw.set_appear()
mw.unitUI()

app.exec_()
