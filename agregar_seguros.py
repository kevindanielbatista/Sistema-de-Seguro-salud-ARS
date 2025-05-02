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
			   INSERT INTO SEGUROS(ID_CLIENTE, COMPAÑIA_SEGURO, PLAN, FECHA_INICIO, FECHA_FIN)
			   VALUES(:idcliente, :compania, :plan, :fecha_inicio, :fecha_fin)
			""")
		#Crear elementos del formulario
		self.id_cliente = QLineEdit()
		self.id_cliente.setValidator(QIntValidator())
		self.compania = QLineEdit()
		self.plan = QComboBox()
		self.plan.addItems(["HMO", #Organizaciones para el Mantenimiento de la Salud
			                "PPO", #Organizaciones de Proveedor de Preferencia
			                "POS", #Planes de Punto-de-Servicio
			                "EPO" #Organizaciones de Proveedores Exclusivos
			               ])
		self.fecha_inicio = QCalendarWidget()
		self.fecha_fin = QCalendarWidget()

		#Agregar elementos al formulario
		self.organizacion.addRow(QLabel("Id cliente"), self.id_cliente)
		self.organizacion.addRow(QLabel("Compañia"), self.compania)
		self.organizacion.addRow(QLabel("Plan"), self.plan)
		self.organizacion.addRow(QLabel("Fecha Inicio"), self.fecha_inicio)
		self.organizacion.addRow(QLabel("Fecha fin"), self.fecha_fin)

		#crear boton para enviar datos
		self.boton_enviar_cambios = QPushButton("Enviar cambios")
		self.boton_enviar_cambios.clicked.connect(self.insertar_datos)

		#Organizar todos los elementos
		self.organizacion_elementos = QVBoxLayout()
		self.organizacion_elementos.addLayout(self.organizacion)
		self.organizacion_elementos.addWidget(self.boton_enviar_cambios)
		self.setLayout(self.organizacion_elementos)

	def insertar_datos(self):
		idcliente = self.id_cliente.text()
		compania = self.compania.text()
		plan = self.plan.currentText()
		fecha_inicio = self.fecha_inicio.selectedDate().toString("yyyy-MM-dd")
		fecha_fin = self.fecha_fin.selectedDate().toString("yyyy-MM-dd")

		self.consulta.bindValue(":idcliente", idcliente)
		self.consulta.bindValue(":compania", compania)
		self.consulta.bindValue(":plan", plan)
		self.consulta.bindValue(":fecha_inicio", fecha_inicio)
		self.consulta.bindValue(":fecha_fin", fecha_fin)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)
		self.limpiar_campos()

	def limpiar_campos(self):
		self.id_cliente.clear()
		self.compania.clear()
