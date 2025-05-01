from PyQt6.QtWidgets import (QWidget,
	                         QFormLayout,
	                         QLineEdit,
	                         QCalendarWidget,
	                         QComboBox,
	                         QLabel,
	                         QVBoxLayout,
	                         QPushButton)
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtSql import QSqlQuery, QSqlQueryModel
import conexion as cx
class AgregarHospital(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Agregar hospital")

		#establecer organizacion de los elementos
		self.organizacion = QFormLayout()


        #Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()

		#Crear modelo de sql y consulta
		self.modelo = QSqlQueryModel()
		self.consulta = QSqlQuery(db = self.conectar)
		self.consulta.prepare(
			"""
			   INSERT INTO HOSPITALES(NOMBRE_HOSPITAL, TIPO, ID_UBICACION, TELEFONO)
			   VALUES(:nombre, :tipo, :ubicacionid, :telefono)
			"""
			)
		#Crear elementos del formulario
		self.nombre_hospital = QLineEdit()
		self.tipo = QComboBox()
		self.tipo.addItems(["Hospital", "Clinica"])
		self.tipo.setCurrentIndex(0)
		self.id_ubicacion = QLineEdit()
		self.id_ubicacion.setValidator(QIntValidator())
		self.telefono = QLineEdit()
		regex = QRegularExpression("^\\d{3}-\\d{3}-\\d{4}$")
		self.telefono.setValidator(QRegularExpressionValidator(regex))

		#agregar elementos al formulario
		self.organizacion.addRow(QLabel("Nombre hospital"), self.nombre_hospital)
		self.organizacion.addRow(QLabel("Tipo"), self.tipo)
		self.organizacion.addRow(QLabel("Ubicacion ID"), self.id_ubicacion)
		self.organizacion.addRow(QLabel("Telefono"), self.telefono)

		#crear boton para enviar datos
		self.boton_enviar_cambios = QPushButton("Enviar cambios")
		self.boton_enviar_cambios.clicked.connect(self.insertar_datos)

		#Organizar todos los elementos
		self.organizacion_elementos = QVBoxLayout()
		self.organizacion_elementos.addLayout(self.organizacion)
		self.organizacion_elementos.addWidget(self.boton_enviar_cambios)
		self.setLayout(self.organizacion_elementos)

	def insertar_datos(self):
		nombre = self.nombre_hospital.text()
		tipo = self.tipo.currentText()
		id_ubicacion = self.id_ubicacion.text()
		telefono = self.telefono.text()

		self.consulta.bindValue(":nombre", nombre)
		self.consulta.bindValue(":tipo", tipo)
		self.consulta.bindValue(":ubicacionid", id_ubicacion)
		self.consulta.bindValue(":telefono", telefono)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)
		self.limpiar_campos()
	def limpiar_campos(self):
		self.nombre_hospital.clear()
		self.id_ubicacion.clear()
		self.telefono.clear()

