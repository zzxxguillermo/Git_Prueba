# ==========================================
# Centro de Formación Profesional N°402
# Curso: Programador
# Docente: Munafo Guillermo
# Clase: Funciones y Parámetros (Pág. 5)
# ==========================================

# 1. Definimos las funciones (Comienzo)

def aplicar_iva(precio_base):
    impuesto = precio_base * 0.21
    precio_final = precio_base + impuesto
    return precio_final  # Devolvemos el total para usarlo afuera


def aplicar_iva_10(precio_base2):
    impuesto = precio_base2 * 0.10
    precio_final2 = precio_base2 + impuesto  # <--- Corregido el nombre para que coincida con el return
    return precio_final2  # <--- Corregido: Ahora está alineado dentro de la función


# 1. Finalizan Funciones


# 2. Programa Principal
print("--- CALCULADORA DE IVA ---")

# Pedimos el dato (usamos float para que acepte números con decimales)
monto = float(input("Ingrese el precio del producto: $"))

# Llamamos a las funciones pasando el monto ingresado y guardamos los resultados
total_a_cobrar = aplicar_iva(monto)
total_a_cobrar2 = aplicar_iva_10(monto)

# Mostramos los resultados finales en la terminal
print(f"El precio final con IVA 21% es: ${total_a_cobrar:.2f}")
print(f"El precio final con IVA 10% es: ${total_a_cobrar2:.2f}")