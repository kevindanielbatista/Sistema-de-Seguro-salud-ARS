import customtkinter as grafica
import funciones_utilidad as utilidades
import panel
from PIL import Image

class InicioSesion(grafica.CTkFrame): # La clase inicio sesion hereda del widget Frame
    def __init__(self, master): # Constructor de la clase
        grafica.CTkFrame.__init__(self, master) #Llamar al constructor de la clase base

        #Crear variable para cambiar de cuadros
        self._cuadro = None

        #Dividir la pantalla en dos
        lado_izquierdo = grafica.CTkFrame(self)
        lado_izquierdo.grid(row = 1, column = 0, sticky = "nswe", padx = 2)
        lado_derecho = grafica.CTkFrame(self)
        lado_derecho.grid(row = 1, column = 1, sticky = "nswe", ipadx = 150)


        # Configurar el grid del lado derecho para centrar el botón
        lado_derecho.grid_rowconfigure(0, weight=1)  # Espacio arriba
        lado_derecho.grid_rowconfigure(1, weight=0)  # Fila del botón
        lado_derecho.grid_rowconfigure(2, weight=1)  # Espacio abajo
        lado_derecho.grid_columnconfigure(0, weight=1)  # Columna izquierda
        lado_derecho.grid_columnconfigure(1, weight=0)  # Columna del botón
        lado_derecho.grid_columnconfigure(2, weight=1)  # Columna derecha


        #Cargar imagen
        imagen = grafica.CTkImage(light_image = Image.open("imagenes/seguro.png"), size = (900, 700))
        seguro = grafica.CTkLabel(master = lado_izquierdo, image = imagen, text = "")
        seguro.grid(column = 0, row = 0)

        #Boton de iniciar sesion
        botonInicio = grafica.CTkButton(lado_derecho, text="Iniciar Sesion", #Botton para cambiar al cuadro de panel
                  command=lambda: master.cambiar_cuadro(panel.Panel))
        botonInicio.grid(column = 1, row = 1)
 
