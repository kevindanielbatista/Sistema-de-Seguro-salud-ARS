import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QPushButton, QHBoxLayout, QLabel)
import panel as pn
import cuadros as cd
import inicio_sesion as ini
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seguros ARS")

        test = ini.Inicio_Sesion()
        self.setCentralWidget(test)

        #Referencia a la ventana Panel
        # self.panel_referencia = None

        #disposicion de los botones
        #arreglo = QHBoxLayout()
        #self.setLayout(arreglo)


        #Cargar logo
        # self.logo = QLabel(self)
        # pix = QPixmap("imagenes/seguro.png")
        # self.logo.setPixmap(pix)
        # self.logo.setScaledContents(True)
        #arreglo.addWidget(self.logo, 3)

        #Crear boton cambio
        #self.boton = QPushButton("Cambio test")
        #self.boton.clicked.connect(self.mostrar_ventana_panel)
        #arreglo.addWidget(self.boton, 1)

        # self.setCentralWidget(self.logo)


    # def mostrar_ventana_panel(self):
    #     if not self.panel_referencia:
    #         self.panel_referencia = pn.Panel()
    #     self.panel_referencia.show()
    #     self.hide()