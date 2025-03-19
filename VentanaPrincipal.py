import tkinter as grafica
from tkinter import ttk

#Crear clase VentanaPrincipal que hereda la clase Tk
class VentanaPrincipal(grafica.Tk):
    def __init__(self): # Declarar constructor
        super().__init__()

        #dar titulo y tamaño a la ventana
        self.title("Seguros ARS")
        self.geometry('400x400')

        #Crear botones
        self.botonAgregarUsuarios = ttk.Button(self, text = "Agregar Usuario").grid(column = 0, row = 0, sticky="nsew")
        self.botonVerUsuarios = ttk.Button(self, text = "Ver usuarios").grid(column = 1, row = 0, sticky="nsew")
        self.botonCitas = ttk.Button(self, text = "Gestionar Citas").grid(column = 0, row = 1, sticky="nsew")
        self.botonGestionarSeguros = ttk.Button(self, text = "Gestionar Seguros").grid(column = 1, row = 1, sticky = "nsew")
        self.reportes = ttk.Button(self, text = "Reportes").grid(column = 0, row = 2, sticky = "nsew")
        self.configuracion = ttk.Button(self, text = "Configuracion").grid(column = 1, row = 2, sticky = "nsew")


        #configurar columnas
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)


        