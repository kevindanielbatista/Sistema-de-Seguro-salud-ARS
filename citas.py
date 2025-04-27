from PyQt6.QtWidgets import (QWidget,
                             QTableView, 
                             QVBoxLayout, 
                             QHeaderView,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout
                            )
from PyQt6.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt
import conexion as cx
import agregar_cita as agct

class Citas(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Citas")


        #Crear conexion base de datos
		self.conectar = cx.Conexion()
		self.conectar.open()


		#establecer organizacion de elementos
		organizacion = QVBoxLayout()


		#crear tabla en la que mostrar los resultados y conectarla al modelo
		self.tabla = QTableView()
		self.modelo = QSqlQueryModel()
		self.modelo.data = lambda index, role=Qt.ItemDataRole.DisplayRole: (
		    str(self.modelo.data(index, Qt.ItemDataRole.DisplayRole)) if role == Qt.ItemDataRole.ToolTipRole 
		    else QSqlQueryModel.data(self.modelo, index, role)) #Activar hover
		self.tabla.setModel(self.modelo)


		self.consulta = QSqlQuery(db = self.conectar)
		self.consulta.prepare(
			"""
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
			        INNER JOIN CITAS
			        ON CLIENTES_ARS.ID_CLIENTE = CITAS.ID_CLIENTE
			        INNER JOIN HOSPITALES
			        ON CITAS.ID_HOSPITAL = HOSPITALES.ID_HOSPITAL
			   WHERE CLIENTES_ARS.APELLIDO LIKE '%'|| :apellido ||'%' AND
			         CITAS.MOTIVO LIKE '%'|| :motivo ||'%' AND
			         HOSPITALES.NOMBRE_HOSPITAL LIKE '%'|| :hospital ||'%';
		  """
		)
              

		#Barras de busqueda
		self.busqueda_apellido = QLineEdit()
		self.busqueda_apellido.setPlaceholderText("Buscar apellido....")
		self.busqueda_apellido.textChanged.connect(self.actualizar_consulta)

		self.busqueda_motivo = QLineEdit()
		self.busqueda_motivo.setPlaceholderText("Buscar motivo cita....")
		self.busqueda_motivo.textChanged.connect(self.actualizar_consulta)

		self.busqueda_hospital = QLineEdit()
		self.busqueda_hospital.setPlaceholderText("Buscar hospital....")
		self.busqueda_hospital.textChanged.connect(self.actualizar_consulta)

		self.botones_busqueda = QHBoxLayout()
		self.botones_busqueda.addWidget(self.busqueda_apellido)
		self.botones_busqueda.addWidget(self.busqueda_motivo)
		self.botones_busqueda.addWidget(self.busqueda_hospital)


		#Boton para agregar citas
		self.agregar_ct = QPushButton("Agregar citas")
		self.agregar_ct.clicked.connect(self.mostrar_agregar_citas)


		#Agregar widget a la pantalla
		organizacion.addLayout(self.botones_busqueda)
		organizacion.addWidget(self.tabla)
		organizacion.addWidget(self.agregar_ct)

		self.actualizar_consulta()

		# Ajustar tabla a toda la pantalla
		cabecera = self.tabla.horizontalHeader()
		cabecera.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)



		#establecer arreglo
		self.setLayout(organizacion)


	def actualizar_consulta(self):
		apellido = self.busqueda_apellido.text()
		motivo = self.busqueda_motivo.text()
		hospital = self.busqueda_hospital.text()

		self.consulta.bindValue(":apellido", apellido)
		self.consulta.bindValue(":motivo", motivo)
		self.consulta.bindValue(":hospital", hospital)

		self.consulta.exec()
		self.modelo.setQuery(self.consulta)


	def mostrar_agregar_citas(self):
	    self.ventana = agct.AgregarCita()
	    self.ventana.show()

	def data(self, index, role):
	    if role == Qt.ItemDataRole.ToolTipRole:
	        return str(self.modelo.data(index))
	    return super().data(index, role)
