from PyQt6.QtWidgets import (QWidget,
	                         QLabel,
	                         QPushButton,
	                         QHBoxLayout)
import agregar_seguros as agseg
import agregar_hospitales as aghos
import agregar_ubicaciones as agub

class Configuracion(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Configuración")

		self.boton_agregar_Seguros = QPushButton("Agregar seguros")
		self.boton_agregar_Seguros.clicked.connect(self.mostrar_agregar_seguros)
		self.boton_agregar_ubicaciones = QPushButton("Agregar ubicaciones")
		self.boton_agregar_ubicaciones.clicked.connect(self.mostrar_agregar_ubicaciones)
		self.boton_agregar_hospitales = QPushButton("Agregar hospitales")
		self.boton_agregar_hospitales.clicked.connect(self.mostrar_agregar_hospitales)

		#establecer organizacion
		self.organizacion = QHBoxLayout()
		self.organizacion.addWidget(self.boton_agregar_Seguros)
		self.organizacion.addWidget(self.boton_agregar_ubicaciones)
		self.organizacion.addWidget(self.boton_agregar_hospitales)

		self.setAutoFillBackground(True)
		self.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 blue, stop:1 green);")

		self.setStyleSheet("""
			QPushButton {
		        background-color: #3498db;
		        font-weight: bold;
		    }
		    QPushButton:hover {
		        background-color: #2980b9;
		    }
			""")

		self.setLayout(self.organizacion)


	def mostrar_agregar_seguros(self):
		self.ventana = agseg.AgregarSeguro()
		self.ventana.show()

	def mostrar_agregar_ubicaciones(self):
		self.ventana = agub.AgregarUbicacion()
		self.ventana.show()

	def mostrar_agregar_hospitales(self):
	    self.ventana = aghos.AgregarHospital()
	    self.ventana.show()



