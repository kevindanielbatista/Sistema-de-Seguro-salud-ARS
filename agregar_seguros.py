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
class AgregarSeguro(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Agregar seguros")

		#Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()

		#Crear modelo de sql y consulta
		self.modelo = QSqlQueryModel()
		self.consulta = QSqlQuery(db = self.conectar)