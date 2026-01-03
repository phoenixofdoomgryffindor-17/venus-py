from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, user=None):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setAlignment(Qt.AlignTop)

        welcome = QLabel(
            f"Welcome, {user.display_name}!"
            if user else
            "Welcome to the Marketplace"
        )
        welcome.setObjectName("PageTitle")

        subtitle = QLabel("Discover your next favorite book.")
        subtitle.setObjectName("PageSubtitle")

        layout.addWidget(welcome)
        layout.addWidget(subtitle)
