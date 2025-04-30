from PyQt6.QtWidgets import (QWidget,
	                         QFormLayout,
	                         QHBoxLayout,
	                         QVBoxLayout,
	                         QSpinBox,
	                         QLineEdit,
	                         QComboBox,
	                         QLabel,
	                         QDataWidgetMapper,
	                         QPushButton)
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
import conexion as cx

class GestionarSeguros(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Gestionar Seguros")

		#establecer conexion
		self.conectar = cx.Conexion()
		self.conectar.open()
		self.modelo = QSqlTableModel(db = self.conectar)

		#Crear organizacion elementos
		self.formulario = QFormLayout()
		self.botones = QHBoxLayout()
		self.organizacion = QVBoxLayout()

		#variables del formulario
		self.id_cliente = QSpinBox()
		self.id_cliente.setRange(0, 2147483647)
		self.id_cliente.setDisabled(True)
		self.compañia = QLineEdit()
		self.plan = QComboBox()
		self.plan.addItems(["HMO", #Organizaciones para el mantenimiento de la salud
			                "EPO", #Organizaciones de proveedores exclusivos
			                "POS", #Planes de punto de servicio
			                "PPO"])#Organizaciones de proveedores preferidos
		regex = QRegularExpression("^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$")
		self.fecha_inicio = QLineEdit()
		self.fecha_inicio.setValidator(QRegularExpressionValidator(regex))
		self.fecha_fin = QLineEdit()
		self.fecha_fin.setValidator(QRegularExpressionValidator(regex))

		#agregar elementos al formulario
		self.formulario.addRow(QLabel("ID cliente"), self.id_cliente)
		self.formulario.addRow(QLabel("Compañia"), self.compañia)
		self.formulario.addRow(QLabel("Plan"), self.plan)
		self.formulario.addRow(QLabel("Fecha inicio"), self.fecha_inicio)
		self.formulario.addRow(QLabel("Fecha fin"), self.fecha_fin)

		#Crear mapeado
		self.mapeado = QDataWidgetMapper()
		self.mapeado.setModel(self.modelo)
		self.mapeado.addMapping(self.id_cliente, 1)
		self.mapeado.addMapping(self.compañia, 2)
		self.mapeado.addMapping(self.plan, 3)
		self.mapeado.addMapping(self.fecha_inicio, 4)
		self.mapeado.addMapping(self.fecha_fin, 5)

		#seleccionar tabla y todas las filas
		self.modelo.setTable("SEGUROS")
		self.modelo.select()
		self.mapeado.toFirst()

		#Crear botones de navegacion
		self.boton_previo = QPushButton("Previo")
		self.boton_previo.clicked.connect(self.mapeado.toPrevious)

		self.boton_siguiente = QPushButton("Siguiente")
		self.boton_siguiente.clicked.connect(self.mapeado.toNext)

		self.boton_guardar_cambios = QPushButton("Guardar cambios")
		self.boton_guardar_cambios.clicked.connect(self.mapeado.submit)

		self.botones.addWidget(self.boton_previo)
		self.botones.addWidget(self.boton_guardar_cambios)
		self.botones.addWidget(self.boton_siguiente)

		self.organizacion.addLayout(self.formulario)
		self.organizacion.addLayout(self.botones)

		self.setLayout(self.organizacion)