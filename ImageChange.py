import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSlot

class ImagesDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImageChange")
        self.image = QLabel(self)

        self.cloud = QPixmap(os.path.join("Image_Examplar", "JPG_1.jpg")).scaledToHeight(900)
        self.plant = QPixmap(os.path.join("Image_Examplar", "JPG_2.jpg")).scaledToHeight(900)
        self.sun = QPixmap(os.path.join("Image_Examplar", "JPG_3.jpg")).scaledToHeight(900)

        self.showing_jpg = True
        
        # Intiate with cloud
        self.image.setPixmap(self.cloud)
        self.image.setFixedSize(self.cloud.size())
        self.setFixedSize(self.cloud.width(), self.cloud.height())

        self.cur_pic = "cloud"

        self.btn = QPushButton("CLICK TO CHANGE!!", self)
        self.btn.setStyleSheet("background-color: rgba(0, 0, 0, 50)")
        self.btn.setGeometry(0, 0, self.cloud.width(), 100)
        self.btn.clicked.connect(self.OnBtnClicked)
        
    @pyqtSlot()
    def OnBtnClicked(self):
        if self.cur_pic == "cloud":
            self.image.setPixmap(self.plant)
            self.image.setFixedSize(self.plant.size())
            self.btn.resize(self.plant.width(), 100)
            self.setFixedSize(self.plant.width(), self.plant.height())
            self.cur_pic = "plant"
        elif self.cur_pic == "plant":
            self.image.setPixmap(self.sun)
            self.image.setFixedSize(self.sun.size())
            self.btn.resize(self.sun.width(), 100)
            self.setFixedSize(self.sun.width(), self.sun.height())
            self.cur_pic = "sun"
        elif self.cur_pic == "sun":
            self.image.setPixmap(self.cloud)
            self.image.setFixedSize(self.cloud.size())
            self.btn.resize(self.cloud.width(), 100)
            self.setFixedSize(self.cloud.width(), self.cloud.height())
            self.cur_pic = "cloud"
            
app = QApplication([])

window = ImagesDisplay()
window.show()

sys.exit(app.exec())
