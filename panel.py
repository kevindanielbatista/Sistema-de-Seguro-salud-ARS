from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton)
from PyQt6.QtCore import Qt
import AgregarUsuarios as agg
import ver_usuarios as verus
import citas
import configuracion
import gestionar_seguros as gestseg
import reportes

class Panel(QWidget):
    def __init__(self):
        super().__init__()

        self.bienvenida = QLabel("Bienvenido")
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.separador = QLabel()

        self.botonAgregarUsuarios = QPushButton("Agregar Usuarios")
        self.botonAgregarUsuarios.clicked.connect(self.mostrar_agregar_usuarios)

        self.botonVerUsuarios = QPushButton("Ver Usuarios")
        self.botonVerUsuarios.clicked.connect(self.mostrar_ver_usuarios)

        self.botonCitas = QPushButton("Citas")
        self.botonCitas.clicked.connect(self.mostrar_citas)

        self.botonGestionarSeguros = QPushButton("Gestionar Seguros")
        self.botonGestionarSeguros.clicked.connect(self.mostrar_seguros)

        self.botonReportes = QPushButton("Reportes")
        self.botonReportes.clicked.connect(self.mostrar_reportes)

        self.configuracion = QPushButton("Configuración")
        self.configuracion.clicked.connect(self.mostrar_configuracion)

        self.botonCerrarSesion = QPushButton("Cerrar sesión")

        organizacion = QVBoxLayout()
        organizacion.addWidget(self.bienvenida)
        organizacion.addWidget(self.separador)
        organizacion.addWidget(self.botonAgregarUsuarios)
        organizacion.addWidget(self.botonVerUsuarios)
        organizacion.addWidget(self.botonCitas)
        organizacion.addWidget(self.botonGestionarSeguros)
        organizacion.addWidget(self.botonReportes)
        organizacion.addWidget(self.configuracion)
        organizacion.addWidget(self.separador)
        organizacion.addWidget(self.botonCerrarSesion)
        self.setLayout(organizacion)

        self.setStyleSheet("""
            QPushButton{
                background-color: #40E0D0;
            }""")

        self.bienvenida.setStyleSheet("""
            QLabel{
                background-color: #40E0D0;
            }""")

    def mostrar_agregar_usuarios(self):
        self.ventana = agg.AgregarUsuarios()
        self.ventana.show()
    def mostrar_ver_usuarios(self):
        self.ventana = verus.VerUsuarios()
        self.ventana.show()
    def mostrar_citas(self):
        self.ventana = citas.Citas()
        self.ventana.show()
    def mostrar_configuracion(self):
        self.ventana = configuracion.Configuracion()
        self.ventana.show()
    def mostrar_seguros(self):
        self.ventana = gestseg.GestionarSeguros()
        self.ventana.show()
    def mostrar_reportes(self):
        self.ventana = reportes.Reportes()
        self.ventana.show()



