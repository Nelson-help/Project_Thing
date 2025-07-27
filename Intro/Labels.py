import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MinecraftCreeper(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowFlags # Frameless Disable_Resize Trans_BG

        self.setWindowTitle("Minecraft Creeper")
        self.setStyleSheet("background-color: rgb(70, 137, 78)") # css
        self.setGeometry(0, 0, 320, 320)
        
        self.draw_features()
    
    def draw_features(self):
        blocks = [
            (64, 64, 64, 64),
            (192, 64, 64, 64),
            (96, 160, 32, 96),
            (128, 128, 64, 96),
            (192, 160, 32, 96)
        ]
        for x, y, w, h in blocks:
            block = QLabel(self)
            block.setGeometry(x, y, w, h)
            block.setStyleSheet("background-color: rgb(26, 22, 24)")

app = QApplication([])

window = MinecraftCreeper()
window.show()

sys.exit(app.exec())
