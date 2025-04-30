from PyQt6.QtWidgets import (QWidget,
	                         QLabel,
	                         QPushButton)

class Configuracion(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Configuración")

		self.boton_agregar_Seguros = QPushButton("Agregar seguros")
		self.boton_agregar_ubicaciones = QPushButton("Agregar ubicaciones")
		self.boton_agregar_hospitales = QPushButton("Agregar hospitales")

		

