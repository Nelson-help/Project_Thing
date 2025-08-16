# type: ignore
import sys, os
from PyQt6.QtWidgets import QApplication # Element Frame
from PyQt6.QtCore import QEvent, QObject, QUrl, QPoint, Qt # Calculation, Settings
from PyQt6.QtGui import QCloseEvent, QGuiApplication, QIcon # Visuals
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings

import threading
import waitress

from server import app as server

from server import getRandPort

WIDTH = 800
HEIGHT = 800

os.environ["PROJECT_NAME"] = "NelsonAPP"
os.environ["ICON_PATH"] = os.path.join("assets", "images", "favicon-32x32.png")

class WebRenderer(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs) # super format: super(parent, obj)

        self.setWindowTitle(os.environ["PROJECT_NAME"])
        self.setWindowIcon(QIcon(os.environ["ICON_PATH"]))

        settings = self.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True) # Plugin = Mods
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True) # WebGl = 3D
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True) #! Javascript = Conect with python (ESSENTIAL)
        settings.setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True) # Accelerated2dCanvas = Faster 2d render
        settings.setAttribute(QWebEngineSettings.WebAttribute.AutoLoadImages, True) # AutoloadImages = Load images faster

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.page().setBackgroundColor(Qt.GlobalColor.transparent) # GlobalColor = Color presets

        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowMinMaxButtonsHint)

        self.setAutoFillBackground(False)

        QApplication.instance().installEventFilter(self)
        self.setMouseTracking(True)
        
        self.resize(WIDTH, HEIGHT)

        self.setUrl(QUrl("file:///C:/Users/User/Downloads/PythonProjects/Project_thing/assets/index.html"))
    
    def eventFilter(self, obj, event):
        # if obj.parent() == self and event.type() == ...:
        #     pass
        return False
    
    def closeEvent(self, event):
        super().closeEvent(event)
        return sys.exit(0)
    
    def show(self):
        if self.windowState() == Qt.WindowState.WindowMinimized:
            self.setWindowState(Qt.WindowState.WindowNoState)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint) # Without flags == reset flags
        super().show()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)
        super().show()
        
    def centralise(self):
        center = QGuiApplication.primaryScreen().availableGeometry().center() 
        #! self.move(center - QPoint(WIDTH//2, HEIGHT//2)) unsafe
        self.move(center - QPoint(self.width()//2, self.height()//2))
    
    def resize(self, w, h):
        if (self.width(), self.height()) == (w, h): return
        super().resize(w, h)
        self.centralise()
        self.show()

def run():
    host = "localHost"
    port = getRandPort()
    if "--server" in sys.argv: # python app.py --server
        return server.run(debug=True, host=host, port=port, threaded=True)
    
    threading.Thread(
        target=waitress.serve,
        daemon=True,
        kwargs={
            "app": server,
            "host": host,
            "port": port,
            "threads": 8,
        },
    ).start()

    app = QApplication(sys.argv)

    window = WebRenderer()
    window.show()
    
    sys.exit(app.exec())

run()