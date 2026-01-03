from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox
)

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")
        title.setObjectName("PageTitle")

        notif_email = QCheckBox("Email Notifications")
        notif_push = QCheckBox("Push Notifications")

        save_btn = QPushButton("Save Settings")
        save_btn.setObjectName("PrimaryButton")

        layout.addWidget(title)
        layout.addWidget(notif_email)
        layout.addWidget(notif_push)
        layout.addWidget(save_btn)
