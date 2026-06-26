# =====================================================================
# BLOQUE 1: LÓGICA Y CÁLCULOS
# Su única función es hacer la matemática. No interactúa con el usuario.
# =====================================================================

# Definimos la función de cálculo. Recibe dos datos externos (parámetros).
def calcular_total_con_descuento(precio_base, porcentaje_descuento):
    """
    Esta función calcula el precio final aplicando un descuento.
    Es 'pura': no tiene inputs ni prints adentro.
    """
    # 1. Calculamos cuánto dinero representa el porcentaje de descuento
    descuento = precio_base * (porcentaje_descuento / 100)
    
    # 2. Restamos ese dinero al precio original para obtener el neto
    precio_final = precio_base - descuento
    
    # 3. Devolvemos el resultado al programa principal mediante 'return'
    return precio_final


# =====================================================================
# BLOQUE 2: INTERFAZ Y PRESENTACIÓN
# Su única función es mostrar información estética. No calcula nada raro.
# =====================================================================

# Esta función recibe el precio antes y después del descuento para armar el ticket.
def mostrar_ticket(precio_original, precio_final):
    """
    Se encarga exclusivamente de darle un formato limpio y ordenado 
    a la salida de la pantalla (consola).
    """
    # Usamos print() con multiplicadores de texto ("=" * 30) para armar las líneas
    print("\n" + "=" * 30)
    print("       TICKET DE COMPRA       ")
    print("=" * 30)
    
    # El modificador :.2f sirve para mostrar solo 2 decimales (ideal para dinero)
    print(f"Subtotal:       ${precio_original:.2f}")
    print(f"Total a pagar:  ${precio_final:.2f}")
    
    print("=" * 30)
    print("   ¡Gracias por su compra!   \n")


# =====================================================================
# BLOQUE 3: PROGRAMA PRINCIPAL (EL ORQUESTADOR)
# No calcula ni dibuja, solo coordina los tiempos del programa.
# =====================================================================

def ejecutar_sistema():
    """
    Función central. Dicta el orden en el que se ejecuta cada proceso.
    """
    print("--- Sistema de Facturación Iniciado ---")
    
    # PASO 1: Captura de datos (Interactúa con el cajero)
    # Convertimos a 'float' porque los precios y descuentos pueden llevar decimales
    monto = float(input("Ingrese el monto total de la compra: $"))
    descuento = float(input("Ingrese el porcentaje de descuento (0 si no tiene): "))
    
    # PASO 2: Procesamiento (Llama al Bloque 1)
    # Le enviamos las variables 'monto' y 'descuento' a la función matemática
    # Guardamos el resultado que nos devuelve el return en una variable nueva
    total_facturado = calcular_total_con_descuento(monto, descuento)
    
    # PASO 3: Salida (Llama al Bloque 2)
    # Le mandamos los datos listos a la función de interfaz para que dibuje el ticket
    mostrar_ticket(monto, total_facturado)


# =====================================================================
# PUNTO DE ARRANQUE (EL BOTÓN DE ENCENDIDO)
# =====================================================================

# Llamamos a la función principal para que el programa empiece a correr
ejecutar_sistema()