#====================================
# actividad: Ticket bloque 1
#====================================
PRECIOS = {
"1": { "nombre" : "leche", "precio" : 1200},
"2": { "nombre" : "pan", "precio" : 2500},
"3": { "nombre" : "yerba", "precio" : 4000}
}

def calcular_subtotal(id_producto, cantidad):
    precio_unitario = PRECIOS[id_producto]["precio"]
    return precio_unitario * cantidad

#=======================================================
# BLOQUE 2 INTERFAZ (SOLO MUESTRA EL TIVKET EN PANTALLA)
#========================================================

def mostrar_ticket(compras_realizadas, total_final):
    print("\n=================================")
    print("       ticket de venta             ")
    print("===================================")

    for item in compras_realizadas:
        print(f"{item['nombre']} x {item['cantidad']} - ${item['subtotal']}")
    print("---------------------------------")
    print(f"TOTAL A PAGAR: ${total_final}")
    print("=================================")
#=================================================
#    BLOQUE 3: GESTION (PIDE DATASO, VALIDACION)
#=================================================
def iniciar_punto_de_venta():
    ticket_actual = []
    total_acumulado = 0

    print("PRODUCTOS: [1] Leche ($1200) | [2] Pan ($2500) | [3] Yerba ($4000)")

    while True:
        # ingresar datos
        codigo = input("\nIngrese codigo de producto (o '0' para cobrar): ")

        if codigo == "0":
             break # termina la carga de datos inmediatamente

        if codigo in PRECIOS:
            try:
                cantidad = int(input(f"¿Cuantas unidades de {PRECIOS[codigo]['nombre']}?: "))
                
                # INVOCAR BLOQUE 1 (calculos)
                subtotal = calcular_subtotal(codigo, cantidad)
                total_acumulado += subtotal

                # Guardar el producto en la lista del ticket
                ticket_actual.append({
                    "nombre": PRECIOS[codigo]["nombre"],
                    "cantidad": cantidad,
                    "subtotal": subtotal
                })
            except ValueError:
                print("Error: Por favor, ingrese una cantidad numérica.")
        else:
            print("Codigo no valido!")
    #invoca bloque 2
    mostrar_ticket(ticket_actual, total_acumulado)

# EJECUCION (aranca el programa)
iniciar_punto_de_venta()
#NO TOCAR QUE FUNCIONA