import customtkinter as grafica
class Boton(grafica.CTkButton):
	def __init__(self, texto, master = None, *args, **kwargs):
		super().__init__(master = master, text = texto, *args, **kwargs)

	
		

