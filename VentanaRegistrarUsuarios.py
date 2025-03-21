import tkinter as graficas
from tkinter import ttk

class VentanaRegistrarUsuarios(graficas.Toplevel): #Esta clase hereda el widget Toplevel, utilizado para crear ventanas superpuestas
	def __init__(self, master = None): #El constructor recibira La ventana sobre la que se deba superponer
		super().__init__(master = master) #Aqui se hace uso del constructor de la clase de la cual se heredo
		self.title("Registrar Usuarios")