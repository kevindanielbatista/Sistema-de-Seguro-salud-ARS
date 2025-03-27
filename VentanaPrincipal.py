import tkinter as grafica
from tkinter import ttk
import Ventana
import boton


#Crear clase VentanaPrincipal que hereda la clase Tk
class VentanaPrincipal(grafica.Tk):
    def __init__(self): # Declarar constructor
        super().__init__()

        #Crear objeto de estilizacion
        estilo = ttk.Style()
        estilo.theme_use("alt")

        #dar tamaño a la ventana
        self.geometry('400x400')

        #Dar titulos
        self.wm_title("Seguros ARS")

        #Crear objetos de ventanas
        self.registrarUsuarios = Ventana.Ventana(master = self, titulo = "Registrar Usuarios")
        self.verUsuarios = Ventana.Ventana(master = self, titulo = "Ver usuarios")
        self.citas = Ventana.Ventana(master = self, titulo = "Ver citas")
        self.gestionarSeguros = Ventana.Ventana(master = self, titulo = "Gestionar Seguros")
        self.reportes = Ventana.Ventana(master = self, titulo = "Reportes")
        self.configuracion = Ventana.Ventana(master = self, titulo = "Configuracion")

        #Crear botones pagina inicial
        #Boton registrar usuarios
        self.botonRegistrarUsuarios = boton.Boton(master = self, texto = "Agregar Usuario")
        self.botonRegistrarUsuarios.bind("<Button>", lambda e: self.registrarUsuarios.mostrar()) #Bind ata el boton a una funcion
        self.botonRegistrarUsuarios.grid(column = 0, row = 0, sticky="nsew")

        #Boton ver usuarios
        self.botonVerUsuarios = boton.Boton(master = self, texto = "Ver usuarios")
        self.botonVerUsuarios.bind("<Button>", lambda e: self.verUsuarios.mostrar())
        self.botonVerUsuarios.grid(column = 1, row = 0, sticky="nsew")

        #boton de gestionar citas
        self.botonCitas = boton.Boton(master = self, texto = "Citas")
        self.botonCitas.bind("<Button>", lambda e: self.citas.mostrar())
        self.botonCitas.grid(column = 0, row = 1, sticky="nsew")

        #boton de gestionar seguros
        self.botonGestionarSeguros = boton.Boton(master = self, texto  = "Gestionar Seguros")
        self.botonGestionarSeguros.bind("<Button>", lambda e: self.gestionarSeguros.mostrar())
        self.botonGestionarSeguros.grid(column = 1, row = 1, sticky = "nsew")

        #boton de reportes
        self.botonReportes = boton.Boton(master = self, texto = "Reportes")
        self.botonReportes.bind("<Button>", lambda e: self.reportes.mostrar())
        self.botonReportes.grid(column = 0, row = 2, sticky = "nsew")

        #Crear boton configuracion
        self.botonConfiguracion = boton.Boton(master = self, texto = "Configuracion")
        self.botonConfiguracion.bind("<Button>", lambda e: self.configuracion.mostrar())
        self.botonConfiguracion.grid(column = 1, row = 2, sticky = "nsew")

        #configurar columnas
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)


        