from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QLabel)
from PyQt6.QtCore import Qt

class Imagen(QLabel):
	def __init__(self, ruta_imagen, ancho, alto):
		super().__init__()
		#cargar imagen
		pix = QPixmap(ruta_imagen)
		pix = pix.scaled(ancho, alto)
		self.setPixmap(pix)

