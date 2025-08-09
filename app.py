# type: ignore

import sys, os
from PyQt6.QtWidgets import QApplication # Element Frame
from PyQt6.QtCore import QUrl, QPoint, Qt # Calculation, Settings
from PyQt6.QtGui import QGuiApplication, QIcon # Visuals
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings

WIDTH = 800
HEIGHT = 800

os.environ["PROJECT_NAME"] = "NelsonAPP"
os.environ["ICON_PATH"] = os.path.join("assets", "images", "favicon-32x32.png")

class WebRenderer(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs) # super format: super(parent, obj)

        self.setWindowTitle(os.environ["PROJECT_NAME"])

        self.setWindowIcon(QIcon(os.environ["ICON_PATH"]))

        self.resize(WIDTH, HEIGHT)

        self.setUrl(QUrl("file:///C:/Users/User/Downloads/PythonProjects/Project_thing/assets/index.html"))
    
    def centralise(self):
        center = QGuiApplication.primaryScreen().availableGeometry().center() 
        #! self.move(center - QPoint(WIDTH//2, HEIGHT//2)) unsafe
        self.move(center - QPoint(self.width()//2, self.height()//2))
    
    def resize(self, w, h):
        if (self.width(), self.height()) == (w, h): return
        super().resize(w, h)
        self.centralise()
        self.show()

app = QApplication(sys.argv)

window = WebRenderer()
window.show()

sys.exit(app.exec())
