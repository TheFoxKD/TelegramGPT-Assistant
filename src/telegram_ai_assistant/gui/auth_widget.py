# src/telegram_ai_assistant/gui/auth_widget.py
from PySide6.QtWidgets import (QLabel, QLineEdit, QProgressBar, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, Signal, Slot


class AuthWidget(QWidget):
    auth_successful = Signal()

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Логотип
        logo_label = QLabel("Telegram AI Assistant")
        logo_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        # Поля ввода
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone number")
        layout.addWidget(self.phone_input)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Verification code")
        self.code_input.hide()
        layout.addWidget(self.code_input)

        # Кнопки
        self.send_code_btn = QPushButton("Send Code")
        self.send_code_btn.clicked.connect(self.send_verification_code)
        layout.addWidget(self.send_code_btn)

        self.verify_btn = QPushButton("Verify")
        self.verify_btn.clicked.connect(self.verify_code)
        self.verify_btn.hide()
        layout.addWidget(self.verify_btn)

        # Индикатор прогресса
        self.progress = QProgressBar()
        self.progress.hide()
        layout.addWidget(self.progress)

    def send_verification_code(self):
        """Отправка кода подтверждения"""
        phone = self.phone_input.text()
        # TODO: Интеграция с Telegram API
        self.code_input.show()
        self.verify_btn.show()
        self.send_code_btn.hide()

    def verify_code(self):
        """Проверка кода подтверждения"""
        code = self.code_input.text()
        # TODO: Проверка кода через Telegram API
        self.auth_successful.emit()