import customtkinter as grafica
import Ventana
import boton
import inicio_sesion as inicio
import funciones_utilidad as utilidad


# Crear clase VentanaPrincipal que hereda la clase Tk
class VentanaPrincipal(grafica.CTk):
    def __init__(self):  # Declarar constructor
        super().__init__()

        # dar tamaño a la ventana
        self.geometry('400x400')

        # Dar titulos
        self.wm_title("Seguros ARS")

        #
        self._cuadro = None


        self.cambiar_cuadro(clase_cuadro = inicio.InicioSesion)

        # Configurar el peso de las filas y columnas
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def cambiar_cuadro(self, clase_cuadro):
        nuevo_cuadro = clase_cuadro(self)
        if self._cuadro is not None:
            self._cuadro.destroy()
        self._cuadro = nuevo_cuadro
        self._cuadro.grid()
