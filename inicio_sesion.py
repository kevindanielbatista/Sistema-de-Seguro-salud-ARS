import customtkinter as grafica
import boton as bt
import funciones_utilidad as utilidades
import panel

class InicioSesion(grafica.CTkFrame):
    def __init__(self, master):
        grafica.CTkFrame.__init__(self, master)
        grafica.CTkLabel(self, text="Inicio Sesion").grid()
        

        self._cuadro = None

        grafica.CTkButton(self, text="Iniciar Sesion",
                  command=lambda: master.cambiar_cuadro(panel.Panel)).grid()
 
