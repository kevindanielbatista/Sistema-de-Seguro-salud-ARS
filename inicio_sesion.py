from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QWidget,QPushButton,
                             QHBoxLayout, QLabel)
import imagen as img
import formulario as form

class Inicio_Sesion(QWidget):
    def __init__(self):
        super().__init__()

        #Imagen de el programa
        logo = img.Imagen("imagenes/seguro.png", 656, 688)
        datos = form.Formulario() #Widget con informacion del formulario

        #variable que maneje la organizacion de los widgets (de forma horizontal.)
        organizacion = QHBoxLayout()
        organizacion.setSpacing(0)
        organizacion.setContentsMargins(0,0,0,0)
        self.setLayout(organizacion)


        organizacion.addWidget(logo)
        organizacion.addWidget(datos)





    


