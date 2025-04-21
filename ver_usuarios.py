from PyQt6.QtWidgets import QWidget, QTableView, QVBoxLayout
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
import conexion as cx

class VerUsuarios(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Ver usuarios")

		self.conectar = cx.Conexion()
		self.conectar.open()

		self.tabla = QTableView()
		self.modelo = QSqlTableModel(db = self.conectar)


		self.tabla.setModel(self.modelo)
		self.modelo.setTable("CLIENTES_ARS")
		self.modelo.select()

		arreglo = QVBoxLayout()
		arreglo.addWidget(self.tabla)

		self.setLayout(arreglo)

