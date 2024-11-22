import sys

from PySide6.QtWidgets import QApplication

from src.telegram_ai_assistant.gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    # Установка стиля приложения
    app.setStyle("Fusion")

    # Создание и отображение главного окна
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()