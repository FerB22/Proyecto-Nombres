import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox,
    QLineEdit, QVBoxLayout, QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt

class GestorMorfemas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Morfemas (Panel Admin)")
        self.resize(400, 250)
        
        self.crear_interfaz()
        self.aplicar_estilos()

    def obtener_regiones(self):
        """Consulta la base de datos para obtener los nombres de las regiones."""
        try:
            conexion = sqlite3.connect("lore.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre FROM regiones")
            regiones = cursor.fetchall()
            conexion.close()
            return regiones
        except sqlite3.Error:
            return []

    def crear_interfaz(self):
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(25, 25, 25, 25)
        layout_principal.setSpacing(15)

        titulo = QLabel("Añadir Nuevo Morfema")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setObjectName("titulo")
        layout_principal.addWidget(titulo)

        # Usamos QFormLayout para que las etiquetas y los campos queden alineados
        formulario = QFormLayout()
        
        # 1. Selector de Región
        self.combo_region = QComboBox()
        self.regiones_db = self.obtener_regiones()
        
        # Guardamos el ID internamente, pero mostramos el nombre al usuario
        for region_id, nombre in self.regiones_db:
            self.combo_region.addItem(nombre, userData=region_id)
            
        formulario.addRow("Región:", self.combo_region)

        # 2. Selector de Tipo
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["prefijos", "raices", "sufijos"])
        formulario.addRow("Tipo de Morfema:", self.combo_tipo)

        # 3. Campo de Texto para la sílaba
        self.input_valor = QLineEdit()
        self.input_valor.setPlaceholderText("Ej: thor, val, etc...")
        formulario.addRow("Valor (Sílaba):", self.input_valor)

        layout_principal.addLayout(formulario)

        # Botón de Guardar
        btn_guardar = QPushButton("Guardar en Base de Datos")
        btn_guardar.clicked.connect(self.guardar_morfema)
        layout_principal.addWidget(btn_guardar)

        self.setLayout(layout_principal)

    def aplicar_estilos(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1b1d22;
                color: #f2f2f2;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel#titulo {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QLineEdit, QComboBox {
                background-color: #262a31;
                border: 1px solid #343b48;
                border-radius: 6px;
                padding: 8px;
                color: white;
            }
            QPushButton {
                background-color: #2f80c1;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #3d8ed0;
            }
        """)

    def guardar_morfema(self):
        # 1. Capturar los datos de la interfaz
        region_id = self.combo_region.currentData() # Obtenemos el ID real (1, 2, 3...)
        tipo = self.combo_tipo.currentText()
        valor = self.input_valor.text().strip().lower() # Limpiamos espacios y pasamos a minúscula

        # 2. Validación básica
        if not valor:
            QMessageBox.warning(self, "Error", "El campo de valor no puede estar vacío.")
            return

        # 3. Inserción en la base de datos SQL
        try:
            conexion = sqlite3.connect("lore.db")
            cursor = conexion.cursor()
            
            cursor.execute("""
                INSERT INTO morfemas (region_id, tipo, valor)
                VALUES (?, ?, ?)
            """, (region_id, tipo, valor))
            
            conexion.commit()
            conexion.close()
            
            # Mensaje de éxito y limpieza del campo
            QMessageBox.information(self, "Éxito", f"'{valor}' añadido a {tipo} correctamente.")
            self.input_valor.clear()
            self.input_valor.setFocus()
            
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error de Base de Datos", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorMorfemas()
    ventana.show()
    sys.exit(app.exec())