# 1. La herramienta para calcular
def calcular_iva(precio, categoria):
    # Simplificado usando una expresión condicional
    tasa = 1.105 if categoria == 1 else 1.21
    return precio * tasa

# 2. El programa que pide los datos
total_general = 0
print("--- CAJA DE COBRO ---")
while True:
    monto = float(input("\nPrecio del producto (0 para salir): $"))
    if monto == 0:
        break  # Si pone 0, el bucle se rompe y sale
    
    print("Categoría: [1] Informática | [2] Oficina")
    tipo = int(input("Seleccione: "))
    
    # Ahora procesamos cada monto dentro del bucle para acumular el total correctamente
    total_general += calcular_iva(monto, tipo)

print(f"\nTOTAL A COBRAR: ${total_general:.2f}") 