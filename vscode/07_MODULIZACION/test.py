# MODULIZACION
import datetime

# bloque 1

def calcular_total_con_descuento(precio_base, porcentaje_descuentos):
    descuento_en_dinero = precio_base * (porcentaje_descuentos / 100)
    precio_final = precio_base - descuento_en_dinero
    return precio_final

# BLOQUE 2 

def mostrar_ticket(precio_original, precio_final_calculado, fecha_hora_venta):
 fecha_formateada = fecha_hora_venta.strftime("%d/%m/%Y %H:%M:%S")
 print("\n=====================================")
 print("            PUNTO DE VENTA             ")
 print("           Comercio Local              ")
 print("            bahia blanca               ")
 print("=======================================")
 print(f"FECHA/HORA:    {fecha_formateada}     ")
 print("TICKET Nro:        00000-00001         ")
 print("---------------------------------------")
 print(f"Subtotal compra: ${precio_original:.2f}")
 ahorro = precio_original - precio_final_calculado
 print(f"Descuento aplicado ${ahorro:.2f}      ")
 print("---------------------------------------")
 print(f"TOTAL a APAGAR  ${precio_final_calculado:.2f}")
 print("---------------------------------------")
 print("¡GRACIAS POR SU COMPRA, VUELVA PRONTO! ")
 print("---------------------------------------")

#BLOQUE 2

def ejecutar_sistema():
   #COORDINA ODO EL FLUJO
   print("--- INICIO DE FACTURACION AUTOMATICO---")
   #SOLICITAR DATOS AL USUARIO
   monto_compra = float(input("Ingrese el monto total de su compra: $"))
   descuento_aplicable = float(input("ingrese el descuento: "))
   #capturar la fecha y hora 
   ahora = datetime.datetime.now()
   
   #invocar a la funcion de calculo
   total_neto = calcular_total_con_descuento(monto_compra, descuento_aplicable)

   #4 invocara a la funcion 
   mostrar_ticket(monto_compra, total_neto, ahora)


if __name__ == "__main__":
    ejecutar_sistema()
