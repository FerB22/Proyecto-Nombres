import random

# 1. Definimos las reglas lingüísticas de tu universo
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
    }
}

def generar_nombre(region):
    # Validamos que la región exista en nuestras reglas
    if region not in morfologia_universo:
        return "Región desconocida"

    # Extraemos las listas de la región seleccionada
    reglas = morfologia_universo[region]
    
    # Elegimos un elemento al azar de cada lista
    prefijo = random.choice(reglas["prefijos"])
    raiz = random.choice(reglas["raices"])
    sufijo = random.choice(reglas["sufijos"])

    # Unimos los morfemas y aseguramos que la primera letra sea mayúscula
    nombre_generado = f"{prefijo}{raiz}{sufijo}".capitalize()
    
    return nombre_generado

# 2. Ponemos a prueba el generador
print("--- Nombres del Reino del Norte ---")
for _ in range(5):
    print(generar_nombre("Reino del Norte"))

print("\n--- Nombres de las Tribus del Fuego ---")
for _ in range(5):
    print(generar_nombre("Tribus del Fuego"))