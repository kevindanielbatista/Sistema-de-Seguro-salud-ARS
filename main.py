"""
   Este archivo es el punto de entrada del programa, es decir, la ventana principal
"""

#Importa la libreria necesaria para interfaces graficas

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QPushButton, QVBoxLayout, QLabel)
import VentanaPrincipal as vp 

if __name__ == "__main__":
   aplicacion = QApplication([])

   ventanaInicial = vp.VentanaPrincipal() # Crear objeto ventana principal
   ventanaInicial.show()

   aplicacion.exec()

