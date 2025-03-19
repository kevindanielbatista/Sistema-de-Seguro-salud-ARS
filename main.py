"""
   Este archivo es el punto de entrada del programa, es decir, la ventana principal
"""

# Importa la libreria necesaria para interfaces graficas
import tkinter as tk

#Iniciar la ventana principal del programa
programaPrincipal = tk.Tk()
programaPrincipal.title("Seguros ARS") # agregar titulo a la ventana

#Crear boton de agregar usuario
agregar_usuario = tk.Button(programaPrincipal, text = "Registrar Usuario")
agregar_usuario.pack()

#Crear boton de ver usuarios
ver_usuarios = tk.Button(programaPrincipal, text = "Ver usuarios")
ver_usuarios.pack()

#Crear boton de gestionar citas medicas
citas = tk.Button(programaPrincipal, text = "Gestionar Citas")
citas.pack()

#Crear boton de gestionar seguros
seguros = tk.Button(programaPrincipal, text = "Gestionar seguros")
seguros.pack()

#Crear boton de reportes
reportes = tk.Button(programaPrincipal, text = "Reportes")
reportes.pack()

#Crear boton de configuracion
configuracion = tk.Button(programaPrincipal, text = "Configuracion")
configuracion.pack()



programaPrincipal.mainloop()
