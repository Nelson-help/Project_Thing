import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer, pyqtSlot, Qt
from PyQt6.QtGui import QFont

class LoadingBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Bar")
        self.setGeometry(460, 515, 1000, 50)

        self.bar = QLabel(self)
        self.bar.setGeometry(0, 0, self.width(), self.height())
        self.bar.setStyleSheet("background-color: rgba(10, 10, 10, 80); border-radius: 20px")

        self.current = QLabel(self)
        self.current.setGeometry(0, 0, 50, self.height())
        self.current.setStyleSheet("background-color: #FF8800; border-radius: 20px")

        self.percentage = QLabel("0%", self)
        self.percentage.setGeometry(450, 0, 25*(len(self.percentage.text()) + 1), 50)
        self.percentage.setStyleSheet("color: rgba(0, 0, 0, 85)")
        self.percentage.setFont(QFont("Cascadia Code", int(self.percentage.height() * 0.5)))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(randint(100, 300))

    @pyqtSlot()
    def update_label(self):
        new_width = self.current.width() + randint(-10, 50)
        # or self.current.width() * (1 + randint(-10, 50)/100) for nonlinear growth

        self.current.setGeometry(0, 0, min(new_width, self.width()), self.height())

        self.percentage.setText(f"{int(self.current.width()/self.width() * 100)} %")

        if self.current.width() == self.width():
           self.timer.stop()
           self.percentage.setText("DONE")

app = QApplication([])
window = LoadingBar()
window.show()
sys.exit(app.exec())
