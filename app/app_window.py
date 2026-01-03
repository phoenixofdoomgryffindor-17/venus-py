from PySide6.QtWidgets import QMainWindow
from views.webview import WebView
from router import Router

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venus Library")
        self.resize(1280, 800)

        self.view = WebView()
        self.setCentralWidget(self.view)

        self.router = Router(self.view)
        self.router.go("home")
