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

class AgregarCita(QWidget):
	def __init__(self):
		super().__init__()

		#colocar titulo
		self.setWindowTitle("Agregar cita")


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
			      INSERT INTO CITAS (ID_CLIENTE, ID_HOSPITAL, FECHA_CITA, HORA_CITA, MOTIVO)
			      VALUES(:cliente, :hospital, :fecha, :hora, :motivo)
			  """
			)

		#Crear elementos del formulario.
		self.id_cliente = QLineEdit()
		self.id_cliente.setValidator(QIntValidator())
		self.id_hospital = QLineEdit()
		self.id_hospital.setValidator(QIntValidator())
		self.fecha_cita = QCalendarWidget()

		regex = QRegularExpression("^([01]?[0-9]|2[0-3]):[0-5][0-9]$") #expresion regular para darle formato a la hora
		self.hora = QLineEdit()
		self.hora.setValidator(QRegularExpressionValidator(regex))
		self.motivo = QComboBox()
		self.motivo.addItems(["Consulta de atención primaria",
			                    "Consulta con especialista",
			                    "Consulta de control y seguimiento",
			                    "Consulta preventiva",
			                    "Consulta pediátrica",
			                    "Consulta ginecológica",
			                    "Consulta urológica",
			                    "Consulta geriátrica"])
		self.motivo.setCurrentIndex(0)


		#Agregar elementos a la pantalla principal
		self.organizacion.addRow(QLabel("ID cliente"), self.id_cliente)
		self.organizacion.addRow(QLabel("ID hospital"), self.id_hospital)
		self.organizacion.addRow(QLabel("Fecha cita"), self.fecha_cita)
		self.organizacion.addRow(QLabel("Hora cita"), self.hora)
		self.organizacion.addRow(QLabel("Motivo cita"), self.motivo)

		#crear boton para agregar filas
		self.boton_enviar_cambios = QPushButton("Enviar cambios")
		self.boton_enviar_cambios.clicked.connect(self.insertar_datos)
		self.ordenar_elementos = QVBoxLayout()
		self.ordenar_elementos.addLayout(self.organizacion)
		self.ordenar_elementos.addWidget(self.boton_enviar_cambios)

		self.setLayout(self.ordenar_elementos)

	def insertar_datos(self):
	    cliente = self.id_cliente.text()
	    hospital = self.id_hospital.text()
	    fecha = self.fecha_cita.selectedDate().toString("yyyy-MM-dd")
	    hora = self.hora.text()
	    motivo = self.motivo.currentText()  

	    self.consulta.bindValue(":cliente", cliente)
	    self.consulta.bindValue(":hospital", hospital)
	    self.consulta.bindValue(":fecha", fecha)
	    self.consulta.bindValue(":hora", hora)
	    self.consulta.bindValue(":motivo", motivo)

	    self.consulta.exec()
	    self.modelo.setQuery(self.consulta)
	    self.limpiar_campos()

	def limpiar_campos(self):
		self.id_cliente.clear()
		self.id_hospital.clear()
		self.hora.clear()
		
	






