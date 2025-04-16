from PyQt6.QtWidgets import (QMainWindow)
import panel as pn
import inicio_sesion as ini
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seguros ARS")

        test = ini.Inicio_Sesion()
        self.setCentralWidget(test)

