# ==========================================
# Centro de Formación Profesional N°402
# Curso: Programador
# Docente: Munafo Guillermo
# Clase: Funciones y Parámetros (Pág. 5)
# ==========================================

# 1. Definimos la función COmienzo
def aplicar_iva(precio_base):
    impuesto = precio_base * 0.21
    precio_final = precio_base + impuesto
    return precio_final  # Devolvemos el total para usarlo afuera

# 1. FInalizan Funciones


# 2. Programa Principal
print("--- CALCULADORA DE IVA ---")

# Pedimos el dato (usamos float para que acepte números con decimales)
monto = float(input("Ingrese el precio del producto: $"))

# Llamamos a la función pasando el monto ingresado y guardamos el resultado
total_a_cobrar = aplicar_iva(monto)

# Mostramos el resultado final en la terminal
# El :.2f sirve para formatear el texto y mostrar solo 2 decimales (centavos)
print(f"El precio final con IVA es: ${total_a_cobrar:.2f}")