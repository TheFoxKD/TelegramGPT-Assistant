# src/telegram_ai_assistant/gui/main_window.py
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QWidget

from .auth_widget import AuthWidget
from .chat_list_widget import ChatListWidget
from .chat_view_widget import ChatViewWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telegram AI Assistant")
        self.setMinimumSize(1200, 800)

        # Главный виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        # Стек виджетов для переключения между авторизацией и основным интерфейсом
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Создаем виджеты
        self.auth_widget = AuthWidget()
        self.main_interface = QWidget()

        # Добавляем виджеты в стек
        self.stacked_widget.addWidget(self.auth_widget)
        self.stacked_widget.addWidget(self.main_interface)

        # Настраиваем основной интерфейс
        self.setup_main_interface()

        # Подключаем сигналы
        self.auth_widget.auth_successful.connect(self.on_auth_successful)

    def setup_main_interface(self):
        """Настройка основного интерфейса приложения"""
        layout = QHBoxLayout(self.main_interface)

        # Список чатов слева
        self.chat_list = ChatListWidget()
        layout.addWidget(self.chat_list, 1)

        # Просмотр чата справа
        self.chat_view = ChatViewWidget()
        layout.addWidget(self.chat_view, 2)

        # Связываем выбор чата с отображением
        self.chat_list.chat_selected.connect(self.chat_view.load_chat)

    @Slot()
    def on_auth_successful(self):
        """Обработчик успешной авторизации"""
        self.stacked_widget.setCurrentIndex(1)
        self.load_chats()

    def load_chats(self):
        """Загрузка списка чатов"""
        self.chat_list.load_chats()
