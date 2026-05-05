# 1. Pedimos los datos al usuario
monto_total = float(input("Ingrese el precio total del repuesto: $"))
cuotas = int(input("Ingrese la cantidad de cuotas (2 a 12): "))

# 2. Calculamos el valor de cada cuota
valor_cuota = monto_total / cuotas

print(f"\nLiquidación del plan por el total de ${monto_total}:")

# 3. Usamos el bucle PARA (for) para mostrar el detalle
# Usamos range(1, cuotas + 1) para que empiece en 1 y termine en el número exacto
for i in range(1, cuotas + 1):
    print(f"Cuota {i}: ${valor_cuota:.2f}")

print("\n¡Plan de pago generado con éxito!")