import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QMovie, QPixmap

#? GUI => Graphics User Interface
#? CLI => Command Line Interface

class ImageDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image")
        self.label = QLabel(self)

        space = QPixmap(os.path.join("Image_Examplar", "JPG.jpg"))
        self.label.setPixmap(space)
        self.label.setFixedSize(space.size())
        
        self.setFixedSize(self.label.size())

app = QApplication([])

window = ImageDisplay()
window.show()

sys.exit(app.exec())
