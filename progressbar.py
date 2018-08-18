import sys
import os
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon

class progressbar(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("Coder Programmer")
        path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'img.png')
        self.setWindowIcon(QIcon(path))
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 300, 25)

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(145, 80)
        self.btnStart.clicked.connect(self.startProgress)
        self.timer = QBasicTimer()
        self.step = 0

    def startProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnStart.setText('start')
        else:
            self.timer.start(100, self)
            self.btnStart.setText('Stop')

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btnStart.setText('Finished')
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)

app = QApplication(sys.argv)
#pprint("input parameters = " +str(sys.argv))
screen = progressbar()
screen.show()
sys.exit(app.exec_())
