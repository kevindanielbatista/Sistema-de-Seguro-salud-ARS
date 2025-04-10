import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QPushButton, QVBoxLayout, QLabel)
import panel as pn

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seguros ARS")

        #Referencia a la ventana Panel
        self.panel_referencia = None

        #disposicion de los botones
        self.arreglo = QVBoxLayout()

        #Boton de cambio de pantalla
        self.boton = QPushButton("Cambio test")
        self.boton.clicked.connect(self.mostrar_ventana_panel)
        self.setCentralWidget(self.boton)


    def mostrar_ventana_panel(self):
        if not self.panel_referencia:
            self.panel_referencia = pn.Panel()
        self.panel_referencia.show()
        self.hide()