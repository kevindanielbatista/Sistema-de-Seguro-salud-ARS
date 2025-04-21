from PyQt6.QtWidgets import (QWidget, 
	                         QTableView,
	                         QVBoxLayout, 
	                         QLineEdit,
	                         QHeaderView,
	                         QLabel)
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
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
		self.modelo = QSqlTableModel(db = self.conectar)
		self.tabla.setModel(self.modelo)
		self.modelo.setTable("CLIENTES_ARS")

		# Ajustar tabla a toda la pantalla
		cabecera = self.tabla.horizontalHeader()
		cabecera.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


		#cambiar nombres columnas
		self.modelo.setHeaderData(0, Qt.Orientation.Horizontal, "Id cliente")
		self.modelo.setHeaderData(1, Qt.Orientation.Horizontal, "Nombre/s")
		self.modelo.setHeaderData(2, Qt.Orientation.Horizontal, "Apellido/s")
		self.modelo.setHeaderData(3, Qt.Orientation.Horizontal, "Fecha de nacimiento")
		self.modelo.setHeaderData(4, Qt.Orientation.Horizontal, "Telefono")
		self.modelo.setHeaderData(5, Qt.Orientation.Horizontal, "Correo")
		self.modelo.setHeaderData(6, Qt.Orientation.Horizontal, "Dirección")


        #Realizar consulta de seleccion
		self.modelo.select()


		#Barra de busqueda
		self.busqueda = QLineEdit()
		self.busqueda.textChanged.connect(self.actualizar_filtro)


        #Organizar los elementos en la pantalla.
		arreglo = QVBoxLayout()
		arreglo.addWidget(self.busqueda)
		arreglo.addWidget(self.tabla, stretch = 2)
		self.setLayout(arreglo)

	def actualizar_filtro(self, palabra):
		filtro = 'NOMBRE LIKE "%{}%"'.format(palabra)
		self.modelo.setFilter(filtro)


