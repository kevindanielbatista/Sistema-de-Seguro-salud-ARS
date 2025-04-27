from PyQt6.QtWidgets import (QWidget)

class AgregarCita(QWidget):
	def __init__(self):
		super().__init__()

		#colocar titulo
		self.setWindowTitle("Agregar cita")