import tkinter as graficas
from tkinter import ttk

class VentanaReportes(graficas.Toplevel):
	def __init__(self, master = None):
	    super().__init__(master = master)
	    self.title("Reportes")