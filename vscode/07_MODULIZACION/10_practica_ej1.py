def calcularIVA(monto):
    return monto * 0.21

def aplicarDescuento(monto):
    return monto * 0.90 # Descuento del %10 para jubilados

def leer_numero(mensaje, tipo=float):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido.")

def ejercicio1():
    print("\n" + "="*50)
    print("Changuito del super.")

    precio1 = leer_numero("Ingrese el precio del primer producto $ ")
    precio2 = leer_numero("Ingrese el precio del segundo producto $ ")
    precio3 = leer_numero("Ingrese el precio del tercer producto $ ")

    subtotal = precio1 + precio2 + precio3
    iva = calcularIVA(subtotal)
    total_con_iva = subtotal + iva

    es_jubilado = input("¿El cliente es jubilado? (1 = si, 0 = No default No). ")
    if es_jubilado == "1":
        total_final = aplicarDescuento(total_con_iva)
        print(f"\nSubtotal:      ${subtotal:.2f}")
        print(f"IVA (21%):       ${iva:.2f}")
        print(f"Total con iva:    ${total_con_iva:.2f}")
        print(f"Descuento (%10):  ${total_con_iva - total_final:.2f}")
        print(f"MONTO FINAL:     ${total_final:.2f}")
    else:
        print(f"\nSubtotal:      ${subtotal:.2f}")
        print(f"IVA (21%):       ${iva:.2f}")
        print(f"MONTO FINAL:     ${total_con_iva:.2f}")

#=======================================================================================
# EJERCIO 2
#=======================================================================================

def ValidarStock(actual, minimo):
    return actual <= minimo #True = hay que reponer

def ejercicio2():
    print("\n" + "="*50)
    print("Contol de stock")
    print("="*50)

    nombre = input("Nombre del producto: ")
    actual = leer_numero(f"Stock actual {nombre}: ", int)
    minimo = leer_numero(f"Stock minimo permitido: ", int)

    if ValidarStock(actual, minimo):
        print(f"\n ¡ATENCION! Es hora de pedir mas {nombre}")
    else:
        print(f"\n Stock seguro de {nombre}")

#=======================================================================================
# EJECERCICIO 3
#=======================================================================================

def calcularPromocion3x2(precio_unitario):
    return precio_unitario * 2 # se cobran solo 2 de cada 3

def ejercicio3():
    print("\n" + "="*50)
    print("Promocion lleva 3, paga 2!!")
    print("="*50)

    precio = leer_numero("Precio unitario del producto: $")
    combos = leer_numero("Cuantos combos de 3 lleva el cliente?: ", int)
    
    total_productos = combos * 3 
    total_pagado = calcularPromocion3x2(precio) * combos 
    precio_sin_promo = precio * total_productos
    ahorro = precio_sin_promo - total_pagado
    
    print(f"\nProductos llevados {total_productos} Unidades")
    print(f"Precio sin promocion: {precio_sin_promo:.2f}")
    print(f"Total ahorrado: ${ahorro:.2f}")
    print(f"MONTO FINAL A PAGAR ${total_pagado:.2f}")

#=======================================================================================
# EJERCICIO 4 LIQUIDAR SUELDOS DE COMERCIO
#=======================================================================================

def CalcularBruto(horas, valor_hora):
    return horas * valor_hora

def CalcularRetenciones(sueldo_bruto):
    return sueldo_bruto * 0.17 # !/% obra social + jubilacion 

def ejercicio4():
    print("\n" + "="*50)
    print("Liquidador de Sueldos")
    print("="*50)

    nombre = input("Nombre del empleado: ")
    horas = leer_numero("Horas trabajadas en el mes: ")
    valor_hora = leer_numero("Valor de la hora $ ")

    bruto = CalcularBruto(horas, valor_hora)
    retenciones = CalcularRetenciones(bruto)
    neto = bruto - retenciones

    print(f"\n{'='*40}")
    print("        RECIBO DE SUELDO      ")
    print(f"\n{'='*40}")
    print(f"Empleado:    {nombre}")
    print(f"Horas trabajadas:   {horas}hs")
    print(f"Valor de Hora      ${valor_hora}")
    print(f"\n{'='*40}")
    print(f"Sueldo Bruto         ${bruto:.2f}")
    print(f"Retenciones          ${retenciones:.2f}")
    print(f"\n{'='*40}")
    print(f"SUELDO NETO          ${neto:.2f}")
    print(f"\n{'='*40}")

#=========================================================================
#  EJERCICIO 5   
#=========================================================================

def minutoAhoras(minutos):
    return minutos / 60

def CalcularCobro(horas, tarifa_hora):
    return horas * tarifa_hora

def ejercicio5():
    print("\n" + "="*50)
    print("Calculadora de estacionamiento")
    print("="*50)

    minutos = leer_numero("Minutos estacionados: ")
    tarifa_hora = leer_numero("Tarifa por hora $ ")

    horas = minutoAhoras(minutos)
    total_a_pagar = CalcularCobro(horas, tarifa_hora)

    print(f"\nTiempo estacionado: {horas:.2f} horas")
    print(f"Total a pagar: ${total_a_pagar:.2f}")

#=======================================================================================
# EJERCICIO 6
#=======================================================================================

def cacularViaticos(kilometros):
    tarifa_km = 150
    return kilometros * tarifa_km

def calcularSueldoBruto(horas, km_recorridos):
    valor_hora = 3000
    sueldo_horas = horas * valor_hora
    viaticos = cacularViaticos(km_recorridos) #llama a funcion 1
    return sueldo_horas + viaticos

def calcularRetenciones(monto_bruto):
    return monto_bruto * 0.17 # !/% obra social + jubilacion

def ejercicio6():
    print("\n" + "="*50)
    print("Liquidador de Sueldos para vendedores")
    print("="*50)

    nombre = input("Nombre del vendedor: ")
    horas = leer_numero("Horas trabajadas en el mes: ")
    km_recorridos = leer_numero("Kilometros recorridos en el mes: ")

    sueldo_bruto = calcularSueldoBruto(horas, km_recorridos)
    retenciones = calcularRetenciones(sueldo_bruto)
    sueldo_neto = sueldo_bruto - retenciones

    print(f"\n{'='*40}")
    print("        RECIBO DE SUELDO      ")
    print(f"\n{'='*40}")
    print(f"Empleado:    {nombre}")
    print(f"Horas trabajadas:   {horas}hs")
    print(f"Kilometros recorridos: {km_recorridos}km")
    print(f"\n{'='*40}")
    print(f"Sueldo Bruto         ${sueldo_bruto:.2f}")
    print(f"Retenciones          ${retenciones:.2f}")
    print(f"\n{'='*40}")
    print(f"SUELDO NETO          ${sueldo_neto:.2f}")
    print(f"\n{'='*40}")


#=======================================================================================
# MENU PRINCIPAL
#=======================================================================================

def menu():
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("1. CHAguito del super")
        print("2. Control de stock")
        print("3. Promocion lleva 3, paga 2!!")
        print("4. Liquidador de Sueldos")
        print("5. Calculadora de estacionamiento")
        print("6. Liquidador de Sueldos para vendedores")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no valida, intente nuevamente.")

if __name__ == "__main__":
    menu()