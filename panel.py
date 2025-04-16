from PyQt6.QtWidgets import (QWidget, QLabel, QGridLayout, QPushButton)

class Panel(QWidget):
    def __init__(self):
        super().__init__()
        self.botonAgregarUsuarios = QPushButton("Agregar Usuarios")
        self.botonVerUsuarios = QPushButton("Ver Usuarios")
        self.botonCitas = QPushButton("Citas")
        self.botonGestionarSeguros = QPushButton("Gestionar Seguros")
        self.botonReportes = QPushButton("Reportes")
        self.Configuracion = QPushButton("Configuración")

        organizacion = QGridLayout()
        organizacion.addWidget(self.botonAgregarUsuarios, 0,0)
        organizacion.addWidget(self.botonVerUsuarios, 0, 1)
        organizacion.addWidget(self.botonCitas, 1,0)
        organizacion.addWidget(self.botonGestionarSeguros, 1,1)
        organizacion.addWidget(self.botonReportes, 2, 0)
        organizacion.addWidget(self.Configuracion, 2, 1)
        self.setLayout(organizacion)

