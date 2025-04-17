from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QWidget,QPushButton, QHBoxLayout)
import imagen as img
import panel as pn

class Inicio_Sesion(QWidget):
    def __init__(self):
        super().__init__()

        #Imagen de el programa.
        logo = img.Imagen("imagenes/seguro.png", 656, 688)
        formulario = QWidget() #Widget con informacion del formulario
        boton_inicio = QPushButton("Iniciar sesion", formulario)
        boton_inicio.clicked.connect(self.mostrar_ventana_panel)

        #variable que maneje la organizacion de los widgets (de forma horizontal.)
        organizacion = QHBoxLayout()
        organizacion.setSpacing(0)
        organizacion.setContentsMargins(0,0,0,0)
        self.setLayout(organizacion)


        organizacion.addWidget(logo)
        organizacion.addWidget(formulario)

        #variable para sostener objeto panel
        self.panel_referencia = None

    def mostrar_ventana_panel(self):
        if not self.panel_referencia:
            self.panel_referencia = pn.Panel()
        self.panel_referencia.show()
        self.parent().setCentralWidget(self.panel_referencia)


