import sqlite3

def crear_base_datos():
    # 1. Conectarse (o crear) el archivo de la base de datos
    conexion = sqlite3.connect("lore.db")
    cursor = conexion.cursor()

    # 2. Crear las tablas SQL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS regiones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS morfemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region_id INTEGER,
            tipo TEXT NOT NULL, 
            valor TEXT NOT NULL,
            FOREIGN KEY (region_id) REFERENCES regiones (id)
        )
    """)

    # 3. La información original que vamos a insertar
    morfologia_universo = {
        "Reino del Norte": {
            "prefijos": ["Vael", "Thar", "Kael", "Ny", "Fros"],
            "raices": ["grim", "dor", "vorn", "thas", "run"],
            "sufijos": ["ia", "gard", "heim", "is", "eth"]
        },
        "Tribus del Fuego": {
            "prefijos": ["Ig", "Zar", "Kha", "Vul", "Pyr"],
            "raices": ["rak", "shir", "tun", "dur", "gath"],
            "sufijos": ["ad", "ah", "im", "ak", "or"]
        },
        "El Imperio Central": {
            "prefijos": ["Aure", "Val", "Cen", "Lu", "Sola"],
            "raices": ["li", "ti", "van", "cor", "min"],
            "sufijos": ["us", "a", "os", "ion", "or"]
        }
    }

    # 4. Insertar los datos usando SQL
    for region, reglas in morfologia_universo.items():
        # Insertar región
        cursor.execute("INSERT OR IGNORE INTO regiones (nombre) VALUES (?)", (region,))
        
        # Obtener el ID de la región recién insertada
        cursor.execute("SELECT id FROM regiones WHERE nombre = ?", (region,))
        region_id = cursor.fetchone()[0]

        # Insertar cada morfema asociado a esa región
        for tipo, lista_valores in reglas.items():
            for valor in lista_valores:
                cursor.execute("""
                    INSERT INTO morfemas (region_id, tipo, valor) 
                    VALUES (?, ?, ?)
                """, (region_id, tipo, valor))

    # 5. Guardar los cambios y cerrar
    conexion.commit()
    conexion.close()
    print("¡Base de datos 'lore.db' creada con éxito!")

if __name__ == "__main__":
    crear_base_datos()