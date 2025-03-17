"""
   Este archivo es el punto de entrada del programa, es decir, la ventana principal
"""

# Importa la libreria necesaria para interfaces graficas
import tkinter as tk

programaPrincipal = tk.Tk()
programaPrincipal.title("Seguros ARS")
agregar_usuario = tk.Button(programaPrincipal, text = "Agregar Usuario")
agregar_usuario.pack()
ver_usuarios = tk.Button(programaPrincipal, text = "Ver usuarios")
ver_usuarios.pack()



programaPrincipal.mainloop()
