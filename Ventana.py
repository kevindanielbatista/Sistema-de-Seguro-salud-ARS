import customtkinter as graficas

class Ventana(graficas.CTkToplevel):
	def __init__(self, titulo, master = None):
	    super().__init__(master = master)
	    self.title(titulo)
	    self.withdraw() #Evitar que la ventana se abra automaticamente
	    self.protocol("WM_DELETE_WINDOW", self.withdraw)

	def mostrar(self):
		"""Metodo que hace aparecer la ventana"""
		self.deiconify()
