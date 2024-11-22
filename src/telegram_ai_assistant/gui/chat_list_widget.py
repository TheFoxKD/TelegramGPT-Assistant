# src/telegram_ai_assistant/gui/chat_list_widget.py
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class ChatListWidget(QWidget):
    chat_selected = Signal(int)  # chat_id

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Список чатов
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_chat_selected)
        layout.addWidget(self.list_widget)

    def load_chats(self):
        """Загрузка списка чатов"""
        # TODO: Получение списка чатов через Telegram API

    def on_chat_selected(self, item):
        """Обработчик выбора чата"""
        chat_id = item.data(Qt.UserRole)
        self.chat_selected.emit(chat_id)
