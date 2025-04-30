from PyQt6.QtWidgets import (QWidget,
	                         QLabel,
	                         QPushButton)
class AgregarHospital(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Agregar hospital")