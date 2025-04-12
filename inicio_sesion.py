from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QWidget,QPushButton, QHBoxLayout, QLabel)
import imagen as img

class Inicio_Sesion(QWidget):
    def __init__(self):
        super().__init__()

        #declarar objetos de prueba
        objeto1 = img.Imagen("imagenes/seguro.png", 656, 685)
        objeto2 = img.Imagen("imagenes/seguro.png", 656, 685)

        #variable que maneje la organizacion de los widgets
        organizacion = QHBoxLayout()
        organizacion.setSpacing(0)
        organizacion.setContentsMargins(0,0,0,0)
        self.setLayout(organizacion)


        organizacion.addWidget(objeto1)
        organizacion.addWidget(objeto2)
        
