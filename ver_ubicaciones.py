from PyQt6.QtWidgets import (QWidget,
	                         QFormLayout,
	                         QLineEdit,
	                         QCalendarWidget,
	                         QComboBox,
	                         QLabel,
	                         QVBoxLayout,
	                         QPushButton,
	                         QTableView,
	                         QHeaderView)
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtSql import QSqlQuery, QSqlQueryModel
from PyQt6.QtCore import Qt
import conexion as cx
class VerUbicaciones(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Ver ubicaciones")

        #Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()
        

        #Crear tabla para visualizar datos
		self.tabla = QTableView()
		self.modelo = QSqlQueryModel()
		self.modelo.data = lambda index, role=Qt.ItemDataRole.DisplayRole: (
		    str(self.modelo.data(index, Qt.ItemDataRole.DisplayRole)) if role == Qt.ItemDataRole.ToolTipRole 
		    else QSqlQueryModel.data(self.modelo, index, role)) #Activar hover		
		self.tabla.setModel(self.modelo)

		#crear boton de busqueda
		self.buscar_ciudad = QLineEdit()
		self.buscar_ciudad.setPlaceholderText("Inserte la ciudad.....")
		self.buscar_ciudad.textChanged.connect(self.actualizar_consulta)

		#Preparar y crear consulta
		self.consulta = QSqlQuery(db = self.conectar)
		self.consulta.prepare(
			"""
			     SELECT * FROM UBICACIONES_ARS
			     WHERE CIUDAD LIKE '%'|| :ciudad ||'%';
			"""
		)
		self.actualizar_consulta()

		# Ajustar tabla a toda la pantalla
		cabecera = self.tabla.horizontalHeader()
		cabecera.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

		self.organizacion = QVBoxLayout()
		self.organizacion.addWidget(self.buscar_ciudad)
		self.organizacion.addWidget(self.tabla, stretch = 2)

		self.setLayout(self.organizacion)

	def actualizar_consulta(self):
		ciudad = self.buscar_ciudad.text()

		self.consulta.bindValue(":ciudad", ciudad)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)