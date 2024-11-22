# src/telegram_ai_assistant/gui/chat_view_widget.py
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class ChatViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # История сообщений
        self.message_view = QTextEdit()
        self.message_view.setReadOnly(True)
        layout.addWidget(self.message_view)

        # Поле ввода сообщения
        self.message_input = QLineEdit()
        layout.addWidget(self.message_input)

        # Кнопка отправки
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

    @Slot(int)
    def load_chat(self, chat_id):
        """Загрузка истории чата"""
        # TODO: Загрузка истории через Telegram API

    def send_message(self):
        """Отправка сообщения"""
        message = self.message_input.text()
        if message:
            # TODO: Отправка сообщения через Telegram API
            self.message_input.clear()
