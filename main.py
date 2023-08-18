from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma super application")
        # Modification taille fenêtre: 
        # self.setFixedSize(valeur de la hauteur et de la largeur en pixels) = taille fixe 
        # self.setMinimumWidth(valeur de la largeur en pixels)
        # self.setMinimumHeight(valeur de la hauteur en pixels)
        # self.setMinimumSize(valeur de la hauteur et de la largeur en pixels)
        # self.resize(400,400) = valeurs de base de la fenêtre avec possibilité de la rétrécir#

        #Layouts
        #QVBoxLayout() = création layout vertical
        #QHBoxLayout() = création layout horizontal
        #QGridLayout() = création layout sous forme de grille
        main_layout = QHBoxLayout(self) #terme self pour que le main layout soit appelé dans la main window
        # left_layout = QVBoxLayout() #création de deux layouts imbriqués dans le principal 
        # right_layout = QVBoxLayout()
        # main_layout.addLayout(left_layout) # ajout des layouts au main layout 
        # main_layout.addLayout(right_layout)
        button = QPushButton("Click me")
        main_layout.addWidget(button)

        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Le bouton a bien été cliqué")
    #   for i in range(1,11):
    #        btn = QPushButton(str(i))
    #       left_layout.addWidget(btn)
    #   for i in range (11, 21):
    #        btn = QPushButton(str(i))
    #        right_layout.addWidget(btn)



app = QApplication()
main_window = MainWindow()
main_window.show()

app.exec()