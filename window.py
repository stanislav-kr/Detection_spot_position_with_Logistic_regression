"""Ten plik służy do wyświetlenia okna dla komunikacji z użytkownikiem"""

import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QScrollArea)
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from model import LogisticRegression, model  # import wytrenowanego modelu regresji logistycznej

# Maksymalne i minimalne wartości dla normalizacji
max_elem = 1351
min_elem = 2


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.example_data = [
            [350, 351, 356, 352],
            [956, 987, 234, 254],
            [234, 256, 244, 249],
            [345, 354, 367, 376]
        ]
        self.example_index = 0

        # Obszar obrazu (etkieta graficzna)
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(500, 350)
        self.image_label.setStyleSheet("border: 2px dashed gray;")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignBottom | Qt.AlignCenter)

        # Ustawienia głównego okna
        self.setWindowTitle("Okno graficzne")
        self.setFixedSize(700, 520)

        self.label = QLabel()
        self.label.move(100, 100)

        # Pola wejściowe do wpisania wartości ciśnień
        self.line1 = QLineEdit(self)
        self.line1.move(10, 10)
        self.line1.setFixedWidth(200)
        self.line1.setPlaceholderText("Wpisz wartość ciśnienia 1")

        self.line2 = QLineEdit(self)
        self.line2.move(10, 40)
        self.line2.setFixedWidth(200)
        self.line2.setPlaceholderText("Wpisz wartość ciśnienia 2")

        self.line3 = QLineEdit(self)
        self.line3.move(10, 70)
        self.line3.setFixedWidth(200)
        self.line3.setPlaceholderText("Wpisz wartość ciśnienia 3")

        self.line4 = QLineEdit(self)
        self.line4.move(10, 100)
        self.line4.setFixedWidth(200)
        self.line4.setPlaceholderText("Wpisz wartość ciśnienia 4")

        # Pole wyjściowe do wyświetlenia wyniku
        self.wynik = QLineEdit(self)
        self.wynik.move(450, 10)
        self.wynik.setFixedWidth(200)
        self.wynik.setPlaceholderText("Wynik")

        # Przycisk do wykonania predykcji
        self.button = QPushButton("Oblicz", self)
        self.button.move(220, 10)
        self.button.setFixedWidth(100)
        self.button.clicked.connect(self.button_click)

        # Przycisk do demonstracji przykładowych danych
        self.button_examp = QPushButton("Przykładowe obliczenia", self)
        self.button_examp.move(220, 40)
        self.button_examp.setFixedWidth(200)
        self.button_examp.clicked.connect(self.button_examp_click)

    """Funkcja dla obslugi przycisku Oblicz"""

    def button_click(self):
        try:
            x1 = float(self.line1.text())
            x2 = float(self.line2.text())
            x3 = float(self.line3.text())
            x4 = float(self.line4.text())
            self.machine_calculate(x1, x2, x3, x4)
            print(x1, x2, x3, x4)
        except ValueError:
            self.label.setText("Error")

    """Normalizacja danych wejściowych (0–1)"""

    def normalization(self, x_norm):
        return [(x - min_elem) / (max_elem - min_elem) for x in x_norm]

    """Funkcja wpisująca przykładowy tekst — możesz rozbudować"""

    def button_examp_click(self):
        example = self.example_data[self.example_index]

        self.line1.setText(str(example[0]))
        self.line2.setText(str(example[1]))
        self.line3.setText(str(example[2]))
        self.line4.setText(str(example[3]))

        self.example_index = (self.example_index + 1) % len(self.example_data)  # Wpisywania gotowych liczb

    """Obliczenia predykcji i aktualizacja interfejsu graficznego"""

    def machine_calculate(self, x1, x2, x3, x4):
        try:
            X_new = np.array([[x1, x2, x3, x4]])  # Nowe dane jako tablica
            X_new = self.normalization(X_new)  # Normalizacja i wyciągnięcie z tablicy
            y_pred = model.predict(X_new)  # Predykcja modelu
            print(X_new)
            print("Predict:", y_pred[0])
            if y_pred[0] == True:
                # Obrazek z rotacją w przypadku "robot na schodach"
                self.pixmap = QPixmap("images/large_removebg.png")
                self.transform = QTransform().rotate(-30)
                self.pixmap = self.pixmap.transformed(self.transform, mode=1)
                self.scaled = self.pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_label.setPixmap(self.scaled)
                self.wynik.setText("Robot na schodach")
            else:
                # Obrazek bez rotacji
                self.pixmap = QPixmap("images/large_removebg.png")
                self.scaled = self.pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_label.setPixmap(self.scaled)
                self.wynik.setText("Robot na powierzchni")
        except ValueError:
            self.label.setText("Error")


app = QApplication([])
window = Window()
window.show()
app.exec_()
