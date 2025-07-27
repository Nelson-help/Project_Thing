import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 800, 600)

        self.setWindowTitle("Browser")

        self.webview = QWebEngineView()

        central = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.webview)
        central.setLayout(layout)

        self.setCentralWidget(central)

        self.webview.setUrl(QUrl("http://127.0.0.1:5000"))
        
app = QApplication(sys.argv)

window = Browser()
window.show()

sys.exit(app.exec())
