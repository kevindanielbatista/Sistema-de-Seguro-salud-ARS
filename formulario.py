from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton,QVBoxLayout,
	                         QLineEdit)
from PyQt6.QtCore import Qt
import panel as pn

class Formulario(QWidget):
	def __init__(self):
		super().__init__()
		#Etiqueta con el texto de bienvenida
		self.texto_inicio = QLabel("Iniciar Sesion")
		self.texto_inicio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Etiqueta con el nombre de usuario
		self.nombre_usuario = QLabel("Nombre Usuario")
		self.nombre_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #widget de insercion de texto para el usuario
		self.insertar_usuario = QLineEdit()

		#Etiqueta con la contraseña
		self.contrasena = QLabel("Contraseña")
		self.contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
		
		self.insertar_contrasena = QLineEdit()

		boton_inicio = QPushButton("Ingresar")
		boton_inicio.clicked.connect(self.mostrar_ventana_panel)

		#Objeto para organizar los elementos.
		organizacion = QVBoxLayout()
		self.setLayout(organizacion)

		organizacion.addWidget(self.texto_inicio)
		organizacion.addWidget(self.nombre_usuario)
		organizacion.addWidget(self.insertar_usuario)
		organizacion.addWidget(self.contrasena)
		organizacion.addWidget(self.insertar_contrasena)
		organizacion.addWidget(boton_inicio)

		#variable para sostener objeto panel
		self.panel_referencia = None

	def mostrar_ventana_panel(self):
	    if not self.panel_referencia:
	        self.panel_referencia = pn.Panel()
	    self.panel_referencia.show()
	    self.parent().parent().setCentralWidget(self.panel_referencia)

