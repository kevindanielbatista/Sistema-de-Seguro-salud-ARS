from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout,
                             QLineEdit, QMessageBox)
from PyQt6.QtCore import Qt
import panel as pn
import sqlite3
import hashlib  
class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.texto_inicio = QLabel("Iniciar Sesión")
        self.texto_inicio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.nombre_usuario = QLabel("Nombre Usuario")
        self.nombre_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.insertar_usuario = QLineEdit()
        
        self.contrasena = QLabel("Contraseña")
        self.contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.insertar_contrasena = QLineEdit()
        self.insertar_contrasena.setEchoMode(QLineEdit.EchoMode.Password)  
        
        boton_inicio = QPushButton("Ingresar")
        boton_inicio.clicked.connect(self.validar_usuario) 
        

        organizacion = QVBoxLayout()
        self.setLayout(organizacion)
        organizacion.addWidget(self.texto_inicio)
        organizacion.addWidget(self.nombre_usuario)
        organizacion.addWidget(self.insertar_usuario)
        organizacion.addWidget(self.contrasena)
        organizacion.addWidget(self.insertar_contrasena)
        organizacion.addWidget(boton_inicio)
        
        self.panel_referencia = None
        
        boton_inicio.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        self.setStyleSheet("""
            QLabel{
                background-color: #40E0D0;
                font-weight: bold;
                font-size: 20 px;
            }
            QLineEdit{
                background-color: #ffffff;
            }
        """)
    
    def conectar_db(self):
        try:
            conn = sqlite3.connect('seguros.db')
            return conn
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar a la base de datos: {e}")
            return None
    
    def validar_usuario(self):
        usuario = self.insertar_usuario.text()
        contrasena = self.insertar_contrasena.text()
        
        if not usuario or not contrasena:
            QMessageBox.warning(self, "Campos vacíos", "Por favor complete todos los campos")
            return
        
        conn = self.conectar_db()
        if conn:
            try:
                cursor = conn.cursor()
                
                cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=?", 
                             (usuario, contrasena))
                
                
                if cursor.fetchone():  # Si encuentra un usuario válido
                    self.mostrar_panel_principal()
                else:
                    QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Error al consultar la base de datos: {e}")
            finally:
                conn.close()
    
    def verificar_hash(self, contrasena_plana, hash_almacenado):
        return hashlib.sha256(contrasena_plana.encode()).hexdigest() == hash_almacenado
    
    def mostrar_panel_principal(self):
        if not self.panel_referencia:
            self.panel_referencia = pn.Panel()
        self.panel_referencia.show()
        self.parent().parent().setCentralWidget(self.panel_referencia)
        QMessageBox.information(self, "Éxito", "Inicio de sesión correcto")

