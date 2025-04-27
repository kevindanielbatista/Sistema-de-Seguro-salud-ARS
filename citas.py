from PyQt6.QtWidgets import (QWidget,
                             QTableView, 
                             QVBoxLayout, 
                             QHeaderView,
                             QLineEdit
                            )
from PyQt6.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
import conexion as cx

class Citas(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Citas")


        #Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()


		#establecer organizacion de elementos
		organizacion = QVBoxLayout()



		#crear tabla en la que mostrar los resultados
		self.tabla = QTableView()


		#Crear modelo de conexion para sql
		self.modelo = QSqlQueryModel()
		self.tabla.setModel(self.modelo)


		#Crear consulta
		consulta = QSqlQuery("""SELECT
							        CLIENTES_ARS.NOMBRE AS Nombre,
							        CLIENTES_ARS.APELLIDO AS Apellido,
								    CITAS.FECHA_CITA AS 'Fecha cita',
								    CITAS.HORA_CITA AS 'Hora cita',
								    CITAS.MOTIVO AS Motivo,
								    HOSPITALES.NOMBRE_HOSPITAL AS 'Nombre hospital',
									HOSPITALES.TIPO AS Tipo,
								    HOSPITALES.TELEFONO AS Telefono
								FROM CLIENTES_ARS
								INNER JOIN CITAS
								ON CLIENTES_ARS.ID_CLIENTE = CITAS.ID_CLIENTE
								INNER JOIN HOSPITALES
								ON CITAS.ID_HOSPITAL = HOSPITALES.ID_HOSPITAL;
							 """, db = self.conectar)
              



		#Realizar consulta
		self.modelo.setQuery(consulta)


		# Ajustar tabla a toda la pantalla
		cabecera = self.tabla.horizontalHeader()
		cabecera.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


		#Barra de busqueda
		self.busqueda = QLineEdit()
		self.busqueda.textChanged.connect(self.actualizar_filtro)


		#Agregar widget a la pantalla
		organizacion.addWidget(self.busqueda)
		organizacion.addWidget(self.tabla, stretch = 2)




		#establecer arreglo
		self.setLayout(organizacion)

	def actualizar_filtro(self, palabra):
	    filtro = f"""
	        SELECT
	            CLIENTES_ARS.NOMBRE AS Nombre,
	            CLIENTES_ARS.APELLIDO AS Apellido,
	            CITAS.FECHA_CITA AS 'Fecha cita',
	            CITAS.HORA_CITA AS 'Hora cita',
	            CITAS.MOTIVO AS Motivo,
	            HOSPITALES.NOMBRE_HOSPITAL AS 'Nombre hospital',
	            HOSPITALES.TIPO AS Tipo,
	            HOSPITALES.TELEFONO AS Telefono
	        FROM CLIENTES_ARS
	        INNER JOIN CITAS ON CLIENTES_ARS.ID_CLIENTE = CITAS.ID_CLIENTE
	        INNER JOIN HOSPITALES ON CITAS.ID_HOSPITAL = HOSPITALES.ID_HOSPITAL
	        WHERE CLIENTES_ARS.NOMBRE LIKE '%{palabra}%' 
	           OR CLIENTES_ARS.APELLIDO LIKE '%{palabra}%'
	           OR HOSPITALES.NOMBRE_HOSPITAL LIKE '%{palabra}%'
	    """
	    
	    # Crear nueva consulta con la conexión
	    consulta_filtrada = QSqlQuery(filtro, db=self.conectar)
	    self.modelo.setQuery(consulta_filtrada)
