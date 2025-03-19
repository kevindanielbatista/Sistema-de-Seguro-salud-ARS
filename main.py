"""
   Este archivo es el punto de entrada del programa, es decir, la ventana principal
"""

#Importa la libreria necesaria para interfaces graficas

import VentanaPrincipal as vp 

if __name__ == "__main__":
   ventanaInicial = vp.VentanaPrincipal() # Crear objeto ventana principal
   ventanaInicial.mainloop()

# #Crear boton de gestionar citas medicas
# citas = tk.Button(programaPrincipal, text = "Gestionar Citas")
# citas.pack()

# #Crear boton de gestionar seguros
# seguros = tk.Button(programaPrincipal, text = "Gestionar seguros")
# seguros.pack()

# #Crear boton de reportes
# reportes = tk.Button(programaPrincipal, text = "Reportes")
# reportes.pack()

# #Crear boton de configuracion
# configuracion = tk.Button(programaPrincipal, text = "Configuracion")
# configuracion.pack()



# programaPrincipal.mainloop()
