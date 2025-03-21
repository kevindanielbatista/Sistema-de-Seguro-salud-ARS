import tkinter as graficas
from tkinter import ttk

class VentanaGestionarCitas(graficas.Toplevel):
	def __init__(self, master = None):
		super().__init__(master = master)
		self.title("Gestionar citas")