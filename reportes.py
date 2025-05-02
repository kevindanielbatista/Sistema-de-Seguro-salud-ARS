from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
                            QLabel, QSizePolicy)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

class Reportes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reportes")
        self.resize(1000, 700)
        
        # Conexión a la base de datos
        self.conn = sqlite3.connect('seguros.db')
        
        # Configuración del layout principal
        layout_principal = QVBoxLayout()
        self.setLayout(layout_principal)
        
        # Crear pestañas para los diferentes reportes
        pestana = QTabWidget()
        layout_principal.addWidget(pestana)
        
        # Gráfico 1: Citas por Hospital
        tab1 = QWidget()
        self.grafica1(tab1)
        pestana.addTab(tab1, "Citas por Hospital")
        
        # Gráfico 2: Tipos de Hospital
        tab2 = QWidget()
        self.grafica2(tab2)
        pestana.addTab(tab2, "Tipos de Hospital")
        
        # Gráfico 3: Tendencia Mensual
        tab3 = QWidget()
        self.grafica3(tab3)
        pestana.addTab(tab3, "Tendencia Mensual")
        
        # Gráfico 4: Distribución Geográfica
        tab4 = QWidget()
        self.grafica4(tab4)
        pestana.addTab(tab4, "Distribución Geográfica")
        
        # Gráfico 5: Clientes por Aseguradora
        tab5 = QWidget()
        self.grafica5(tab5)
        pestana.addTab(tab5, "Clientes por Aseguradora")
        
        # Gráfico 6: Motivos de Cita
        tab6 = QWidget()
        self.grafica6(tab6)
        pestana.addTab(tab6, "Motivos de Cita")
    
    def hacer_consulta(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    
    def grafica1(self, parent):
        """Citas por Hospital (Gráfico de Barras)"""
        layout = QVBoxLayout(parent)
        
        # Consulta SQL
        query = """
        SELECT H.NOMBRE_HOSPITAL, COUNT(C.ID_CITA) as CANTIDAD_CITAS
        FROM HOSPITALES H
        LEFT JOIN CITAS C ON H.ID_HOSPITAL = C.ID_HOSPITAL
        GROUP BY H.NOMBRE_HOSPITAL
        ORDER BY CANTIDAD_CITAS DESC;
        """
        data = self.hacer_consulta(query)
        
        # Preparar datos para el gráfico
        hospitales = [item[0] for item in data]
        citas = [item[1] for item in data]
        
        # Crear figura de matplotlib
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Personalizar el gráfico
        ax.barh(hospitales, citas, color='skyblue')
        ax.set_title('Citas por Hospital', pad=20)
        ax.set_xlabel('Número de Citas')
        ax.set_ylabel('Hospital')
        
        # Añadir valores a las barras
        for i, v in enumerate(citas):
            ax.text(v + 0.5, i, str(v), color='black', va='center')
        
        # Integrar con PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
    
    def grafica2(self, parent):
        layout = QVBoxLayout(parent)
        
        # Consulta SQL
        query = """
        SELECT H.TIPO, COUNT(C.ID_CITA) as CANTIDAD
        FROM HOSPITALES H
        JOIN CITAS C ON H.ID_HOSPITAL = C.ID_HOSPITAL
        GROUP BY H.TIPO;
        """
        data = self.hacer_consulta(query)
        
        # Preparar datos
        tipos = [item[0] for item in data]
        cantidades = [item[1] for item in data]
        
        # Crear figura
        fig = Figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        
        # Personalizar gráfico
        ax.pie(cantidades, labels=tipos, autopct='%1.1f%%', 
              startangle=90, colors=plt.cm.Pastel1.colors)
        ax.set_title('Distribución de Citas por Tipo de Hospital', pad=20)
        ax.axis('equal')  # Para que sea un círculo perfecto
        
        # Integrar con PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
    
    def grafica3(self, parent):
        layout = QVBoxLayout(parent)
        
        # Consulta SQL
        query = """
        SELECT strftime('%Y-%m', FECHA_CITA) as MES, COUNT(ID_CITA) as CANTIDAD
        FROM CITAS
        WHERE FECHA_CITA IS NOT NULL
        GROUP BY MES
        ORDER BY MES;
        """
        data = self.hacer_consulta(query)
        
        # Preparar datos
        meses = [datetime.strptime(item[0], '%Y-%m') for item in data]
        cantidades = [item[1] for item in data]
        
        # Crear figura
        fig = Figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        
        # Personalizar gráfico
        ax.plot(meses, cantidades, marker='o', linestyle='-', color='teal')
        ax.set_title('Tendencia Mensual de Citas', pad=20)
        ax.set_xlabel('Mes')
        ax.set_ylabel('Número de Citas')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Formatear fechas en el eje X
        fig.autofmt_xdate()
        
        # Integrar con PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
    
    def grafica4(self, parent):
        layout = QVBoxLayout(parent)
        
        # Consulta SQL
        query = """
        SELECT U.PROVINCIA, COUNT(C.ID_CITA) as CANTIDAD
        FROM UBICACIONES_ARS U
        JOIN HOSPITALES H ON U.ID_UBICACION = H.ID_UBICACION
        JOIN CITAS C ON H.ID_HOSPITAL = C.ID_HOSPITAL
        GROUP BY U.PROVINCIA
        ORDER BY CANTIDAD DESC;
        """
        data = self.hacer_consulta(query)
        
        # Preparar datos
        provincias = [item[0] for item in data]
        cantidades = [item[1] for item in data]
        
        # Crear figura
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Personalizar gráfico
        bars = ax.bar(provincias, cantidades, color='salmon')
        ax.set_title('Distribución de Citas por Provincia', pad=20)
        ax.set_xlabel('Provincia')
        ax.set_ylabel('Número de Citas')
        
        # Rotar etiquetas del eje X para mejor legibilidad
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        
        # Añadir valores a las barras
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom')
        
        # Ajustar layout para evitar cortes
        fig.tight_layout()
        
        # Integrar con PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
    
    def grafica5(self, parent):
        layout = QVBoxLayout(parent)
        
        # Consulta SQL para obtener compañías y planes
        query = """
        SELECT S.COMPAÑIA_SEGURO, S.PLAN, COUNT(S.ID_CLIENTE) as CLIENTES
        FROM SEGUROS S
        GROUP BY S.COMPAÑIA_SEGURO, S.PLAN
        ORDER BY S.COMPAÑIA_SEGURO, CLIENTES DESC;
        """
        data = self.hacer_consulta(query)
        
        # Procesar datos para gráfico apilado
        compañias = {}
        for compañia, plan, clientes in data:
            if compañia not in compañias:
                compañias[compañia] = {}
            compañias[compañia][plan] = clientes
        
        # Preparar datos para matplotlib
        compañias_list = list(compañias.keys())
        planes = set()
        for plans in compañias.values():
            planes.update(plans.keys())
        planes = sorted(planes)
        
        # Crear matriz de datos
        bottom = [0] * len(compañias_list)
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Colores para los diferentes planes
        colors = plt.cm.tab20.colors
        
        # Dibujar barras apiladas
        for i, plan in enumerate(planes):
            values = []
            for compañia in compañias_list:
                values.append(compañias[compañia].get(plan, 0))
            
            ax.bar(compañias_list, values, bottom=bottom, label=plan, color=colors[i % len(colors)])
            bottom = [sum(x) for x in zip(bottom, values)]
        
        # Personalizar gráfico
        ax.set_title('Clientes por Aseguradora y Plan', pad=20)
        ax.set_xlabel('Compañía de Seguro')
        ax.set_ylabel('Número de Clientes')
        ax.legend(title='Planes', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Rotar etiquetas del eje X
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        
        # Ajustar layout
        fig.tight_layout()
        
        # Integrar con PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
    
    def grafica6(self, parent):
        layout = QVBoxLayout(parent)
        
        # Consulta SQL
        query = """
        SELECT MOTIVO, COUNT(ID_CITA) as FRECUENCIA
        FROM CITAS
        WHERE MOTIVO IS NOT NULL AND MOTIVO != ''
        GROUP BY MOTIVO
        ORDER BY FRECUENCIA DESC
        LIMIT 10;
        """
        data = self.hacer_consulta(query)
        
        # Preparar datos
        motivos = [item[0] for item in data]
        frecuencias = [item[1] for item in data]
        
        # Crear figura
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Personalizar gráfico
        bars = ax.barh(motivos, frecuencias, color='lightgreen')
        ax.set_title('Motivos de citas mas frecuentes', pad=20)
        ax.set_xlabel('Frecuencia')
        ax.set_ylabel('Motivo')
        
        # Añadir valores a las barras
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                    f'{int(width)}',
                    va='center')
        
        # Ajustar layout
        fig.tight_layout()
        
        # Integrar con PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
    
    def cerrar_conexion(self, event):
        self.conn.close()
        super().cerrar_conexion(event)