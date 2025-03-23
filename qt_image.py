from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image Display')
        self.setGeometry(100, 100, 400, 400)

        # Створюємо QLabel для показу зображення
        self.label = QLabel(self)

        # Завантажуємо зображення з файлу
        self.pixmap = QPixmap('large.png')  # Замість 'your_image.png' вставте шлях до вашого зображення

        # Масштабуємо зображення до розмірів вікна
        self.pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Встановлюємо зображення в QLabel
        self.label.setPixmap(self.pixmap)

        # Встановлюємо вирівнювання зображення в центрі вікна
        self.label.setAlignment(Qt.AlignCenter)

    def resizeEvent(self, event):
        # Масштабуємо зображення при зміні розміру вікна
        self.pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)


def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
