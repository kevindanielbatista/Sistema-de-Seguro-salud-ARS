from PyQt6.QtWidgets import (QMainWindow)
import panel as pn
import inicio_sesion as ini
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seguros ARS")

        test = ini.Inicio_Sesion()
        self.setCentralWidget(test)

        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 blue, stop:1 green);")




        #self.setStyleSheet("background-image: linear-gradient(red, yellow)")

