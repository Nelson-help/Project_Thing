import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QMovie
from PyQt6.QtCore import pyqtSlot

class JPGGIFDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MediaChange")
        self.media = QLabel(self)

        self.jpg = QPixmap(os.path.join("Image_Examplar", "JPG.jpg"))
        self.gif = QMovie(os.path.join("Image_Examplar", "GIF.gif"))
        self.showing_jpg = True
        
        # Intiate with JPG
        self.media.setPixmap(self.jpg)
        self.media.setFixedSize(self.jpg.size())
        self.setFixedSize(self.jpg.size())

        self.btn = QPushButton("CLICK TO CHANGE!!", self)
        self.btn.resize(self.jpg.width(), 100)
        self.btn.clicked.connect(self.OnBtnClicked)
        

    @pyqtSlot()
    def OnBtnClicked(self):
        # Change to Movie
        if self.showing_jpg:
            self.media.setMovie(self.gif)
            self.gif.start()
            self.media.setFixedSize(self.gif.currentPixmap().size())
            self.btn.resize(self.gif.currentPixmap().width(), 100)
            self.setFixedSize(self.gif.currentPixmap().size())
            self.showing_jpg = False
        # Change to JPG
        else:
            self.gif.stop()
            self.media.setPixmap(self.jpg)
            self.media.setFixedSize(self.jpg.size())
            self.btn.resize(self.jpg.width(), 100)
            self.setFixedSize(self.jpg.size())
            self.showing_jpg = True
            
app = QApplication([])

window = JPGGIFDisplay()
window.show()

sys.exit(app.exec())
