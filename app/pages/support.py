from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class SupportPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Support Center")
        title.setObjectName("PageTitle")

        message = QTextEdit()
        message.setPlaceholderText("Describe your issue...")

        send_btn = QPushButton("Send Message")
        send_btn.setObjectName("PrimaryButton")

        layout.addWidget(title)
        layout.addWidget(message)
        layout.addWidget(send_btn)
