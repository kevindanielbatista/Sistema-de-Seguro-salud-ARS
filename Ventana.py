import tkinter as graficas
from tkinter import ttk

class Ventana(graficas.Toplevel):
	def __init__(self, titulo, master = None):
	    super().__init__(master = master)
	    self.title(titulo)
	    self.withdraw() #Evitar que la ventana se abra automaticamente

	def mostrar(self):
		"""Metodo que hace aparecer la ventana"""
		self.deiconify()