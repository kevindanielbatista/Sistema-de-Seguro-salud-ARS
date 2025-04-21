from PyQt6.QtWidgets import (QWidget,
	                         QFormLayout,
	                         QLineEdit,
	                         QCalendarWidget,
	                         QLabel,
	                         QDataWidgetMapper,
	                         QPushButton,
	                         QHBoxLayout,
	                         QVBoxLayout)
from PyQt6.QtSql import QSqlTableModel
import conexion as cx

class AgregarUsuarios(QWidget):
	def __init__(self):
		super().__init__()
		#dar titulo a la ventana
		self.setWindowTitle("Agregar Usuarios")


		#establecer organizacion de elementos
		organizacion = QFormLayout()


        #Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()


		#crear aspectos del formulario
		self.nombre = QLineEdit()
		self.apellido = QLineEdit()
		self.nacimiento = QCalendarWidget()
		self.telefono = QLineEdit()
		self.correo = QLineEdit()
		self.direccion = QLineEdit()


		#Agregar elementos al formulario
		organizacion.addRow(QLabel("Nombre/s"), self.nombre)
		organizacion.addRow(QLabel("Apellido/s"), self.apellido)
		organizacion.addRow(QLabel("fecha de nacimiento"), self.nacimiento)
		organizacion.addRow(QLabel("Telefono"), self.telefono)
		organizacion.addRow(QLabel("Correo"), self.correo)
		organizacion.addRow(QLabel("Direccion"), self.direccion)


		#modelo de conexion a la base de datos
		self.modelo = QSqlTableModel(db = self.conectar)
		self.mapeado = QDataWidgetMapper()
		self.mapeado.setModel(self.modelo)


		#conectar cada boton a una columna
		self.mapeado.addMapping(self.nombre, 1)
		self.mapeado.addMapping(self.apellido, 2)
		self.mapeado.addMapping(self.nacimiento, 3)
		self.mapeado.addMapping(self.telefono, 4)
		self.mapeado.addMapping(self.correo, 5)
		self.mapeado.addMapping(self.direccion, 6)


		#conectar
		self.modelo.setTable("CLIENTES_ARS")
		self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
		self.modelo.select()


		#segunda organizacion para colocar boton de submision
		organizacion2 = QHBoxLayout()


		#Crear boton de submision
		boton_guardar_cambios = QPushButton("Guardar Cambios")
		boton_guardar_cambios.clicked.connect(self.guardar_cambios)
		organizacion2.addWidget(boton_guardar_cambios)


		#Unir ambas organizaciones
		organizaciones = QVBoxLayout()
		organizaciones.addLayout(organizacion)
		organizaciones.addLayout(organizacion2)


		#aplicar organizacion
		self.setLayout(organizaciones)

		self.agregar_fila()

	def agregar_fila(self):
		fila = self.modelo.rowCount()
		self.modelo.insertRow(fila)

		self.mapeado.setCurrentIndex(fila)
		self.nombre.setFocus()

	def guardar_cambios(self):
		fecha = self.nacimiento.selectedDate().toString("yyyy-MM-dd")
		self.modelo.setData(self.modelo.index(self.mapeado.currentIndex(), 3), fecha)

		self.modelo.submitAll()
		self.agregar_fila()









