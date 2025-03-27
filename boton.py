import tkinter as graficas
from tkinter import ttk

class Boton(ttk.Button):
	def __init__(self, texto, master = None):
		super().__init__(master = master, text = texto)
