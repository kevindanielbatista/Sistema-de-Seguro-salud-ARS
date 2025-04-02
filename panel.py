import customtkinter as grafica
import boton 
import funciones_utilidad as utilidades
import Ventana

class Panel(grafica.CTkFrame):
	def __init__(self, master):
	    grafica.CTkFrame.__init__(self, master)

	    self.grid(row=0, column=0, sticky="nsew")  # Sticky en todas direcciones

	    #Crear objetos de ventanas
	    self.registrarUsuarios = Ventana.Ventana(master = self, titulo = "Registrar Usuarios")
	    self.verUsuarios = Ventana.Ventana(master = self, titulo = "Ver usuarios")
	    self.citas = Ventana.Ventana(master = self, titulo = "Ver citas")
	    self.gestionarSeguros = Ventana.Ventana(master = self, titulo = "Gestionar Seguros")
	    self.reportes = Ventana.Ventana(master = self, titulo = "Reportes")
	    self.configuracion = Ventana.Ventana(master = self, titulo = "Configuracion")

	    #Crear botones pagina inicial
	    #Boton registrar usuarios
	    self.botonRegistrarUsuarios = boton.Boton(master = self, texto = "Agregar Usuario", command = self.registrarUsuarios.mostrar)
	    self.botonRegistrarUsuarios.grid(column = 0, row = 0, sticky="nsew")

	    #Boton ver usuarios
	    self.botonVerUsuarios = boton.Boton(master = self, texto = "Ver usuarios", command = self.verUsuarios.mostrar)
	    self.botonVerUsuarios.grid(column = 1, row = 0, sticky="nsew")

	    #boton de gestionar citas
	    self.botonCitas = boton.Boton(master = self, texto = "Citas", command = self.citas.mostrar)
	    self.botonCitas.grid(column = 0, row = 1, sticky="nsew")

	    #boton de gestionar seguros
	    self.botonGestionarSeguros = boton.Boton(master = self, texto  = "Gestionar Seguros", command = self.gestionarSeguros.mostrar)
	    self.botonGestionarSeguros.grid(column = 1, row = 1, sticky = "nsew")

	    #boton de reportes
	    self.botonReportes = boton.Boton(master = self, texto = "Reportes", command = self.reportes.mostrar)
	    self.botonReportes.grid(column = 0, row = 2, sticky = "nsew")

	    #Crear boton configuracion
	    self.botonConfiguracion = boton.Boton(master = self, texto = "Configuracion", command = self.configuracion.mostrar)
	    self.botonConfiguracion.grid(column = 1, row = 2, sticky = "nsew")



	    #configurar columnas
	    self.grid_columnconfigure(0, weight=1, uniform="group1")
	    self.grid_columnconfigure(1, weight=1, uniform="group1")
	    self.grid_rowconfigure(0, weight=1)
	    self.grid_rowconfigure(1, weight=1)
	    self.grid_rowconfigure(2, weight=1)

