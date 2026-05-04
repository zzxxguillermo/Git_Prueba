import customtkinter as ctk
from tkinter import messagebox

# 1. Configuración de apariencia
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# 2. Lógica de verificación
def verificar_divisor():
    try:
        # Paso A: Capturamos los datos de ambos componentes
        numero_principal = int(entrada_nro.get())
        divisor_elegido = int(desplegable.get())
        
        # Paso B: Aplicamos la lógica del resto (operador %)
        if numero_principal % divisor_elegido == 0:
            mensaje = f"¡Correcto! {divisor_elegido} es divisor de {numero_principal}."
            messagebox.showinfo("Resultado Positivo", mensaje)
        else:
            mensaje = f"No, {numero_principal} no es divisible por {divisor_elegido} de forma exacta."
            messagebox.showwarning("Resultado Negativo", mensaje)
            
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresá un número válido en el primer campo.")

# 3. Interfaz Gráfica
ventana = ctk.CTk()
ventana.title("Validador de Divisores - FP")
ventana.geometry("400x350")

# Campo para el número principal
ctk.CTkLabel(ventana, text="1. Ingresá el número principal:", font=("Arial", 14)).pack(pady=10)
entrada_nro = ctk.CTkEntry(ventana, placeholder_text="Ej: 50")
entrada_nro.pack(pady=5)

# Campo desplegable con números fijos del 1 al 10
ctk.CTkLabel(ventana, text="2. Elegí un divisor para probar:", font=("Arial", 14)).pack(pady=10)

# Generamos la lista del 1 al 10 usando un bucle range
opciones_fijas = [str(i) for i in range(1, 11)]

desplegable = ctk.CTkComboBox(ventana, values=opciones_fijas)
desplegable.pack(pady=5)
desplegable.set("1") # Valor por defecto

# Botón de acción única
boton_validar = ctk.CTkButton(
    ventana, 
    text="VERIFICAR DIVISIÓN", 
    command=verificar_divisor,
    fg_color="#2c3e50",
    hover_color="#34495e"
)
boton_validar.pack(pady=30)

ventana.mainloop()