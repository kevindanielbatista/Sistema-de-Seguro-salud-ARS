import tkinter as grafica
from tkinter import ttk
import VentanaRegistrarUsuarios as registrar
import VentanaVerUsuarios as ver
import VentanaGestionarSeguros as seguros
import VentanaReportes as reportes
import VentanaGestionarCitas as citas
import VentanaConfiguracion as configuracion


#Crear clase VentanaPrincipal que hereda la clase Tk
class VentanaPrincipal(grafica.Tk):
    def __init__(self): # Declarar constructor
        super().__init__()

        #dar titulo y tamaño a la ventana
        self.title("Seguros ARS")
        self.geometry('400x400')

        #Crear boton agregar usuarios
        self.botonAgregarUsuarios = ttk.Button(self, text = "Agregar Usuario")
        self.botonAgregarUsuarios.bind("<Button>", lambda e: registrar.VentanaRegistrarUsuarios(self))
        self.botonAgregarUsuarios.grid(column = 0, row = 0, sticky="nsew")

        #Crear boton ver usuarios
        self.botonVerUsuarios = ttk.Button(self, text = "Ver usuarios")
        self.botonVerUsuarios.bind("<Button>", lambda e: ver.VentanaVerUsuarios(self))
        self.botonVerUsuarios.grid(column = 1, row = 0, sticky="nsew")

        #Crear boton de gestionar citas
        self.botonCitas = ttk.Button(self, text = "Gestionar Citas")
        self.botonCitas.bind("<Button>", lambda e: citas.VentanaGestionarCitas(self))
        self.botonCitas.grid(column = 0, row = 1, sticky="nsew")

        #Crear boton de gestionar seguros
        self.botonGestionarSeguros = ttk.Button(self, text = "Gestionar Seguros")
        self.botonGestionarSeguros.bind("<Button>", lambda e: seguros.VentanaGestionarSeguros(self))
        self.botonGestionarSeguros.grid(column = 1, row = 1, sticky = "nsew")

        #Crear boton de reportes
        self.reportes = ttk.Button(self, text = "Reportes")
        self.reportes.bind("<Button>", lambda e: reportes.VentanaReportes(self))
        self.reportes.grid(column = 0, row = 2, sticky = "nsew")

        #Crear boton configuracion
        self.configuracion = ttk.Button(self, text = "Configuracion")
        self.configuracion.bind("<Button>", lambda e: configuracion.VentanaConfiguracion(self))
        self.configuracion.grid(column = 1, row = 2, sticky = "nsew")


        #configurar columnas
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)


        