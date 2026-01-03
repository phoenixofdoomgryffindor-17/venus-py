from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class WritePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Author Studio")
        title.setObjectName("PageTitle")

        subtitle = QLabel("Manage your creative works.")
        subtitle.setObjectName("PageSubtitle")

        new_book_btn = QPushButton("Create New Book")
        new_book_btn.setObjectName("PrimaryButton")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(new_book_btn)
