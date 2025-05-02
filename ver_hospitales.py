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
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery, QSqlQueryModel
import conexion as cx
class VerHospitales(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Ver hospitales")

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
		self.buscar_hospital = QLineEdit()
		self.buscar_hospital.setPlaceholderText("Inserte el hospital....")
		self.buscar_hospital.textChanged.connect(self.actualizar_consulta)

		#Preparar y crear consulta
		self.consulta = QSqlQuery(db = self.conectar)
		self.consulta.prepare(
			"""
			     SELECT * FROM HOSPITALES
			     WHERE NOMBRE_HOSPITAL LIKE '%'|| :nombre_hospital ||'%';
			"""
		)
		self.actualizar_consulta()

		# Ajustar tabla a toda la pantalla
		cabecera = self.tabla.horizontalHeader()
		cabecera.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

		self.organizacion = QVBoxLayout()
		self.organizacion.addWidget(self.buscar_hospital)
		self.organizacion.addWidget(self.tabla, stretch = 2)

		self.setLayout(self.organizacion)

	def actualizar_consulta(self):
		nombre_hospital = self.buscar_hospital.text()

		self.consulta.bindValue(":nombre_hospital", nombre_hospital)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)



