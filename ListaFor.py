# =========================================================
# CREAR LISTA VACÍA Y CARGAR 3 ELEMENTOS CON UN FOR
# =========================================================

# 1. Creamos la lista totalmente vacía
elementos = []

print("--- INICIO DE CARGA ---")

# Usamos un for para repetir el proceso 3 veces
for i in range(3):
    # Pedimos el dato (sumamos 1 a 'i' solo para la pantalla)
    nuevo_dato = input(f"Ingrese el elemento {i + 1}: ")
    
    # Guardamos el dato al final de la lista
    elementos.append(nuevo_dato)


# =========================================================
# MOSTRAR LOS ELEMENTOS USANDO UN FOR CLÁSICO CON ÍNDICE
# =========================================================
print("\n--- ELEMENTOS CARGADOS ---")

# Volvemos a recorrer 3 veces (del 0 al 2) para usar 'i' como el índice
for i in range(3):
    
    # Buscamos en la lista el elemento que está en la posición 'i'
    print(f"Posición [{i}]: {elementos[i]}")