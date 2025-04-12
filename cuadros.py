import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QPushButton, QGridLayout, QLabel, QVBoxLayout)
from PyQt6.QtWidgets import QSizePolicy


"""
   EL proposito de esta clase es poder crear "cuadros"
   que dividan la disposicion de un programa.
"""
class Cuadros(QWidget):
    def __init__(self, imagen = None):
        super().__init__()
        self.imagen = imagen
        self.logo = QLabel()
       # self.arreglo = QVBoxLayout(self)
       # self.arreglo.addWidget(self.logo)
        self.arreglo.setContentsMargins(0, 0, 0, 0)
        self.arreglo.setSpacing(0)
       # self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
       # self.logo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #self.logo.setScaledContents(True)  # Hace que la imagen se escale al tamaño del QLabel
        self.crear_etiqueta()
        # self.imagen = imagen
        # self.logo = None
        # self.arreglo = QVBoxLayout(self)


    def crear_etiqueta(self):
        if self.imagen:
            pixmap = QPixmap(self.imagen)
            if not pixmap.isNull():
                self.logo.setPixmap(pixmap)
    # def crear_etiqueta(self):
    #     if self.imagen is not None:
    #         self.logo = QLabel("") 
    #         pix = QPixmap(self.imagen)
    #         self.arreglo.addWidget(self.logo)
    #         self.logo.setScaledContents(True)

    #         if not pix.isNull():
    #             proporcional_pix = pix.scaled(Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    #             self.logo.setPixmap(proporcional_pix)
    #             self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    #             self.arreglo.addWidget(self.logo)

