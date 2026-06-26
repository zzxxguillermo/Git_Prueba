import tkinter as tk
from tkinter import messagebox

# --- LÓGICA DE PROGRAMA ---

total_general = 0.0

def calcular_iva(precio, categoria):
    if categoria == 1:
        return precio * 1.105
    else:
        return precio * 1.21

def agregar_producto():
    global total_general
    
    try:
        # Tomamos los datos de los campos de entrada
        precio = float(entry_precio.get())
        categoria = int(variable_categoria.get())
        
        if precio <= 0:
            messagebox.showwarning("Atención", "El precio debe ser mayor a 0.")
            return

        # Calculamos el IVA y acumulamos
        precio_con_iva = calcular_iva(precio, categoria)
        total_general += precio_con_iva
        
        # Actualizamos la etiqueta del total en la ventana
        lbl_total_resultado.config(text=f"${total_general:.2f}")
        
        # Limpiamos el campo de precio para el siguiente producto
        entry_precio.delete(0, tk.END)
        entry_precio.focus()
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un precio válido (use punto para decimales).")

def finalizar_venta():
    global total_general
    messagebox.showinfo("Venta Finalizada", f"El total a cobrar es: ${total_general:.2f}")
    # Reiniciamos la caja para la próxima venta
    total_general = 0.0
    lbl_total_resultado.config(text="$0.00")
    entry_precio.delete(0, tk.END)


# --- INTERFAZ GRÁFICA (TKINTER) ---

# 1. Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Caja de Cobro")
ventana.geometry("350x300")
ventana.config(padx=20, pady=20)

# 2. Elementos para el Precio
lbl_precio = tk.Label(ventana, text="Precio del producto:", font=("Arial", 11))
lbl_precio.pack(anchor="w", pady=5)

entry_precio = tk.Entry(ventana, font=("Arial", 11))
entry_precio.pack(fill="x", pady=5)
entry_precio.focus() # Hace que el cursor titile acá al abrir

# 3. Elementos para la Categoría (Usamos Radiobuttons para que elija una opción)
lbl_cat = tk.Label(ventana, text="Categoría del producto:", font=("Arial", 11))
lbl_cat.pack(anchor="w", pady=10)

variable_categoria = tk.IntVar(value=1) # Por defecto arranca en 1 (Informática)

radio_info = tk.Radiobutton(ventana, text="Informática (10.5%)", variable=variable_categoria, value=1, font=("Arial", 10))
radio_info.pack(anchor="w")

radio_ofi = tk.Radiobutton(ventana, text="Oficina (21%)", variable=variable_categoria, value=2, font=("Arial", 10))
radio_ofi.pack(anchor="w")

# 4. Botones de Acción
btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_agregar.pack(fill="x", pady=15)

# 5. Mostrar el Total Acumulado en Pantalla
frame_total = tk.Frame(ventana)
frame_total.pack(fill="x", pady=5)

lbl_total_texto = tk.Label(frame_total, text="Total acumulado: ", font=("Arial", 12, "bold"))
lbl_total_texto.pack(side="left")

lbl_total_resultado = tk.Label(frame_total, text="$0.00", font=("Arial", 12, "bold"), fg="blue")
lbl_total_resultado.pack(side="left")

# 6. Botón Cerrar Venta
btn_finalizar = tk.Button(ventana, text="Finalizar y Cobrar", command=finalizar_venta, bg="#008CBA", fg="white", font=("Arial", 10, "bold"))
btn_finalizar.pack(fill="x", pady=10)

# Lanzamos la aplicación
btn_finalizar = tk.Button(
    ventana,
    text="Finalizar y Cobrar",
    command=finalizar_venta,
    bg="#008CBA",
    fg="white",
    font=("Arial", 10, "bold")
)

btn_finalizar.pack(fill="x", pady=10)

# Lanzamos la aplicación
ventana.mainloop()
