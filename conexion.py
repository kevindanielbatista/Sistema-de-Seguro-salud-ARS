from PyQt6.QtSql import QSqlDatabase

class Conexion(QSqlDatabase):
	def __init__(self):
		super().__init__("QSQLITE")
		self.setDatabaseName("seguros.db")