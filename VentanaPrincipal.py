import tkinter as grafica
from tkinter import ttk

#Crear clase VentanaPrincipal que hereda la clase Tk
class VentanaPrincipal(grafica.Tk):
    def __init__(self): # Declarar constructor
        super().__init__()

        #dar titulo a la ventana
        self.title("Seguros ARS")

        #Crear boton agregar usuarios
        self.botonAgregarUsuarios = ttk.Button(self, text = "Agregar Usuario")
        self.botonAgregarUsuarios.pack()

        #Crear boton de ver usuarios
        self.botonVerUsuarios = ttk.Button(self, text = "Ver usuarios") 
        self.botonVerUsuarios.pack()

        #Crear Boton de ver citas medicas
        self.botonCitas = ttk.Button(self, text = "Gestionar Citas")
        self.botonCitas.pack()

        #Crear boton de gestionar seguros
        self.botonGestionarSeguros = ttk.Button(self, text = "Gestionar Seguros")
        self.botonGestionarSeguros.pack()

        #Crear boton reportes
        self.reportes = ttk.Button(self, text = "Reportes")
        self.reportes.pack()

        #Crear boton configuracion
        self.configuracion = ttk.Button(self, text = "Configuracion")
        self.configuracion.pack()
