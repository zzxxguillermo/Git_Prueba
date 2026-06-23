# Variable normal (una cosa)
nombre = "Ana"

# Lista (varias cosas)
nombres = ["Ana", "Luis", "Carlos", "Maria"]

# =========================================================
# 1. ¿Cómo se muestra la lista completa?
# =========================================================
print(nombres)  # Imprime: ["Ana", "Luis", "Carlos", "Maria"]


# =========================================================
# 2. ¿Cómo elegir una sola cosa de la lista? (Uso de Índices)
# REGLA DE ORO: En programación se empieza a contar desde el 0.
# [0] es el primero, [1] el segundo, etc.
# =========================================================
print(nombres[0])  # Imprime: Ana (la posición 0)
print(nombres[2])  # Imprime: Carlos (la posición 2, que es el tercero)


# =========================================================
# 3. ¿Cómo saber cuántos elementos hay en total?
# Usamos la función len() -> viene de "length" (longitud)
# =========================================================
cantidad = len(nombres)
print(cantidad)  # Imprime: 4


# =========================================================
# 4. ¿Cómo agregar a alguien nuevo al final de la lista?
# Usamos .append() -> significa "adjuntar" o "añadir"
# =========================================================
nombres.append("Javier")
print(nombres)  # Imprime: ["Ana", "Luis", "Carlos", "Maria", "Javier"]