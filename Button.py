import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtCore import pyqtSlot

class ButtonDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button")

        self.btn = QPushButton(self)
        self.btn.setText("CLICK ME!!")
        self.btn.setGeometry(0, 0, 200, 100)
        self.btn.clicked.connect(self.OnBtnClicked)
        

    @pyqtSlot()
    def OnBtnClicked(self):
        print("Button Pressed")

app = QApplication([])

window = ButtonDisplay()
window.show()

sys.exit(app.exec())
