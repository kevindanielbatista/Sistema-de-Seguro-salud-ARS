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
		self.id_ubicacion = QLineEdit()
		self.id_ubicacion.setValidator(QIntValidator())
