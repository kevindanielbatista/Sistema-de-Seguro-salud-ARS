"""
   Este archivo es el punto de entrada del programa, es decir, la ventana principal
"""

#Importa la libreria necesaria para interfaces graficas

import VentanaPrincipal as vp 

if __name__ == "__main__":
   ventanaInicial = vp.VentanaPrincipal() # Crear objeto ventana principal
   ventanaInicial.mainloop()
