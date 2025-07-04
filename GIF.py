import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QMovie, QPixmap

class GIFDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIF")
        self.label = QLabel(self)

        minion = QMovie(os.path.join("Image_Examplar", "GIF.gif"))
        minion.start() # Must put before the Fixed Size

        self.label.setMovie(minion)
        self.label.setFixedSize(minion.currentPixmap().size())

        self.setFixedSize(self.label.size())

app = QApplication([])

window = GIFDisplay()
window.show()

sys.exit(app.exec())
