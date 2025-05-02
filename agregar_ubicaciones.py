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
import ver_ubicaciones as verubi
class AgregarUbicacion(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Agregar Ubicacion")

		#Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()

		#establecer organizacion de los elementos
		self.organizacion = QFormLayout()

		#Crear modelo de sql y consulta
		self.modelo = QSqlQueryModel()
		self.consulta = QSqlQuery(db = self.conectar)
		self.consulta.prepare(
			 """
			     INSERT INTO UBICACIONES_ARS(CIUDAD, PROVINCIA, PAIS, CODIGO_POSTAL)
			     VALUES(:ciudad, :provincia, :pais, :codigo)
			 """
			)
		#Crear elementos del formulario
		self.ciudad = QLineEdit()
		self.provincia = QLineEdit()
		self.pais = QLineEdit()
		regex = QRegularExpression("^\\d{1,10}$")
		self.codigo = QLineEdit()
		self.codigo.setValidator(QRegularExpressionValidator(regex))

		#agregar elementos al formulario
		self.organizacion.addRow(QLabel("Ciudad"), self.ciudad)
		self.organizacion.addRow(QLabel("Provincia"), self.provincia)
		self.organizacion.addRow(QLabel("Pais"), self.pais)
		self.organizacion.addRow(QLabel("Codigo"), self.codigo)

		#crear boton para enviar datos
		self.boton_enviar_cambios = QPushButton("Enviar cambios")
		self.boton_enviar_cambios.clicked.connect(self.insertar_datos)

		#crear boton para ver ubicaciones
		self.boton_ver_ubicaciones = QPushButton("Ver ubicaciones")
		self.boton_ver_ubicaciones.clicked.connect(self.__mostrar_ubicaciones)

		#ORganizar todos los elementos
		self.organizacion_elementos = QVBoxLayout()
		self.organizacion_elementos.addLayout(self.organizacion)
		self.organizacion_elementos.addWidget(self.boton_enviar_cambios)
		self.organizacion_elementos.addWidget(self.boton_ver_ubicaciones)
		self.setLayout(self.organizacion_elementos)

	def insertar_datos(self):
		ciudad = self.ciudad.text()
		provincia = self.provincia.text()
		pais = self.pais.text()
		codigo = self.codigo.text()

		self.consulta.bindValue(":ciudad", ciudad)
		self.consulta.bindValue(":provincia", provincia)
		self.consulta.bindValue(":pais", pais)
		self.consulta.bindValue(":codigo", codigo)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)
		self.limpiar_campos()

	def limpiar_campos(self):
		self.ciudad.clear()
		self.provincia.clear()
		self.pais.clear()
		self.codigo.clear()

	def __mostrar_ubicaciones(self):
		self.ventana = verubi.VerUbicaciones()
		self.ventana.show()
