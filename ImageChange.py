import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, pyqtSlot

class ImagesDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImageChange")
        
        # Create Widgets
        self.image = QLabel(self)
        self.btn = QPushButton("CLICK TO STOP", self)

        self.imagePaths = [os.path.join("Image_examplar", f"JPG_{i+1}.jpg") for i in range(3)]
        self.imagePixmaps = [QPixmap(path).scaledToHeight(900) for path in self.imagePaths]
        self.imageIndex = -1 # imageIndex starts at -1 to show the "zeroth" image
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.NextImage)
        self.timer.start(2500)  # Change image every 2.5 seconds

        self.btn.setStyleSheet("background-color: rgba(0, 0, 0, 50)")
        self.btn.setGeometry(0, 0, self.imagePixmaps[self.imageIndex].width(), 100)
        self.btn.clicked.connect(self.timer.stop())
        
    @pyqtSlot()
    def NextImage(self):
        # Cycle through images (add one to move through the list, remainder to cycle)
        self.imageIndex = (self.imageIndex + 1) % len(self.imagePixmaps)
        
        self.image.setPixmap(self.imagePixmaps[self.imageIndex])
        self.image.setFixedSize(self.imagePixmaps[self.imageIndex].size())
        self.btn.resize(self.imagePixmaps[self.imageIndex].width(), 100)
        self.setFixedSize(self.imagePixmaps[self.imageIndex].size())

app = QApplication([])

window = ImagesDisplay()
window.show()

sys.exit(app.exec())
