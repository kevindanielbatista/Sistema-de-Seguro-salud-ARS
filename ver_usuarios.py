from PyQt6.QtWidgets import (QWidget, 
	                         QTableView,
	                         QVBoxLayout,
	                         QHBoxLayout, 
	                         QLineEdit,
	                         QHeaderView,
	                         QLabel)
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtCore import Qt
import conexion as cx

class VerUsuarios(QWidget):
	def __init__(self):
		super().__init__()
		#ajustar tamaño ventana
		self.setWindowTitle("Ver usuarios")


        #Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()
        

        #Crear tabla para visualizar datos
		self.tabla = QTableView()
		self.modelo = QSqlQueryModel()
		self.tabla.setModel(self.modelo)


		#Crear botones de busqueda
		self.buscar_nombre = QLineEdit()
		self.buscar_nombre.setPlaceholderText("Buscar por nombre")
		self.buscar_nombre.textChanged.connect(self.actualizar_consulta)

		self.buscar_apellido = QLineEdit()
		self.buscar_apellido.setPlaceholderText("Buscar por apellido")
		self.buscar_apellido.textChanged.connect(self.actualizar_consulta)


		#Preparar y crear consulta
		self.consulta = QSqlQuery(db = self.conectar)
		self.consulta.prepare(
			"""
			     SELECT * FROM CLIENTES_ARS
			     WHERE NOMBRE LIKE '%'|| :nombre_persona ||'%' AND
			           APELLIDO LIKE '%'|| :apellido_persona ||'%';
			"""
		)
		self.actualizar_consulta()

		# Ajustar tabla a toda la pantalla
		cabecera = self.tabla.horizontalHeader()
		cabecera.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


		#Crear organizacion de elementos
		self.botones_busqueda = QHBoxLayout()
		self.botones_busqueda.addWidget(self.buscar_nombre)
		self.botones_busqueda.addWidget(self.buscar_apellido)

		self.organizacion = QVBoxLayout()
		self.organizacion.addLayout(self.botones_busqueda)
		self.organizacion.addWidget(self.tabla, stretch = 2)

		self.setLayout(self.organizacion)

	def actualizar_consulta(self):
		nombre = self.buscar_nombre.text() #No usar self en la declaracion para hacer que el alcance de esta variable se limite a esta funcion
		apellido = self.buscar_apellido.text() 

		self.consulta.bindValue(":nombre_persona", nombre)
		self.consulta.bindValue(":apellido_persona", apellido)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)

