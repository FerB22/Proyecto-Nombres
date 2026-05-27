# 🌌 Enciclopedia del Universo - Generador de Lore

Una aplicación de escritorio construida con **Python** y **PySide6** para gestionar la construcción de mundos (worldbuilding), permitiendo administrar regiones, facciones y generar nombres procedimentales basados en reglas morfológicas personalizadas.

## 🚀 Características Principales

La aplicación está estructurada como una **Suite de Ingeniería** con 4 módulos principales sincronizados en tiempo real:

1. **🌌 Forja de Nombres (Generador):** * Generación procedimental de nombres combinando prefijos, raíces y sufijos en tiempo real.
   * Control dinámico de longitud (nombres de 2, 3 o 4 sílabas).
   * Visor de asentamientos (reinos y tribus) para la región seleccionada.
   * Historial de nombres generados por sesión.

2. **🗺️ Panel de Mundo:**
   * Creación de nuevas **Regiones** geográficas.
   * Asignación de **Facciones** (Reinos y Tribus) vinculadas a una región específica mediante claves relacionales.

3. **🧬 Lingüística:**
   * Inyección de **Morfemas** (prefijos, raíces, sufijos) asociados a regiones particulares para expandir su vocabulario procedural.

4. **📝 Editor de Contenido (CRUD):**
   * Panel de administración unificado mediante capas (`QStackedWidget`).
   * Permite **Modificar** o **Eliminar** regiones, facciones y morfemas.
   * Eliminación segura (con borrado en cascada y confirmaciones mediante `QMessageBox`).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Interfaz Gráfica (GUI):** PySide6 (Qt for Python)
* **Base de Datos:** SQLite3 (Librería nativa)
* **Diseño Visual:** Estilos CSS embebidos (Modo oscuro moderno, sin "cajas" residuales en fuentes tipográficas).
