from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class MarketplacePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Marketplace")
        title.setObjectName("PageTitle")

        subtitle = QLabel("Browse books from the community.")
        subtitle.setObjectName("PageSubtitle")

        self.book_list = QListWidget()
        self.book_list.addItem("Example Book 1")
        self.book_list.addItem("Example Book 2")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.book_list)
