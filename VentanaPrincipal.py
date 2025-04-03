import customtkinter as grafica
import inicio_sesion as inicio
import funciones_utilidad as utilidad


# Crear clase VentanaPrincipal que hereda la clase Tk. TK representa el punto de entrada, solo puede haber una.
class VentanaPrincipal(grafica.CTk):
    #self es un parametro obligatorio que se refiere al objeto siendo creado.
    def __init__(self):  # Declarar constructor
        #invocar al constructor de una clase madre a partir de una clase hija
        super().__init__()

        # dar tamaño a la ventana
        self.geometry('400x400')

        # Dar titulos
        self.wm_title("Seguros ARS")

        #Crea una variable que almacene el cuadro. None cuando no exista
        self._cuadro = None

        self.cambiar_cuadro(clase_cuadro = inicio.InicioSesion)

    def cambiar_cuadro(self, clase_cuadro: grafica.CTkFrame):
        """
           Función que destruye un cuadro (Clase Frame) y 
           crea otro cuadro para reemplazarlo.

           args:
                 clase_cuadro: Clase CTkFrame/TkFrame
           devuelve:

           excepciones:
        """
        #Crea un nuevo cuadro a partir de la clase cuadro
        nuevo_cuadro = clase_cuadro(self)
        #Si ya existe un cuadro, este es destruido y reemplazado por el nuevo
        if self._cuadro is not None:
            self._cuadro.destroy()
        #reemplazar el cuadro destruido por el nuevo cuadro
        self._cuadro = nuevo_cuadro
        #Colocar el cuadro en la pantalla
        self._cuadro.grid()
