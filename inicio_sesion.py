import customtkinter as grafica
import boton as bt
import funciones_utilidad as utilidades
import panel

class InicioSesion(grafica.CTkFrame): # La clase inicio sesion hereda del widget Frame
    def __init__(self, master): # Constructor de la clase
        grafica.CTkFrame.__init__(self, master) #Llamar al constructor de la clase base

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        #configurar peso columnas
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        #
        grafica.CTkLabel(self, text="Inicio Sesion").grid(row = 0, column = 0, columnspan = 2) #Crear etiqueta de inicio

        #Crear variable para cmabiar de cuadros
        self._cuadro = None

        #Dividir la pantalla en dos
        lado_izquierdo = grafica.CTkFrame(self)
        lado_izquierdo.grid(row = 1, column = 0, sticky = "nswe", ipadx = 300, ipady = 300, padx = 10)
        lado_derecho = grafica.CTkFrame(self)
        lado_derecho.grid(row = 1, column = 1, sticky = "nswe", ipadx = 155, ipady = 300, padx = 10)

        grafica.CTkButton(lado_derecho, text="Iniciar Sesion", #Botton para cambiar al cuadro de panel
                  command=lambda: master.cambiar_cuadro(panel.Panel)).grid()
 
