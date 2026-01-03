from PySide6.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    def load_html(self, html: str):
        self.setHtml(html)
