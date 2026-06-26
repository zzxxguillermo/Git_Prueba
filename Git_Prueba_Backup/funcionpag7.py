# 1. Función para calcular IVA
def calcular_iva(precio, categoria):

    if categoria == 1:
        return precio * 1.105   # 10.5% IVA
    else:
        return precio * 1.21    # 21% IVA


# 2. Programa principal
total_general = 0

print("--- CAJA DE COBRO ---")

while True:

    monto = float(input("\nPrecio del producto (0 para salir): $"))

    # Condición de salida
    if monto == 0:
        break

    print("Categoría: [1] Informática | [2] Oficina")
    tipo = int(input("Seleccione: "))

    # Se suma el precio con IVA
    total_general += calcular_iva(monto, tipo)

# Resultado final
print(f"\nTOTAL A COBRAR: ${total_general:.2f}")