"""
   Este archivo es el punto de entrada del programa, es decir, la ventana principal
"""

#Importa la libreria necesaria para interfaces graficas
from PyQt6.QtWidgets import (QApplication)
import VentanaPrincipal as vp 

if __name__ == "__main__":
   aplicacion = QApplication([])

   ventanaInicial = vp.VentanaPrincipal() # Crear objeto ventana principal
   ventanaInicial.show()

   aplicacion.exec()

