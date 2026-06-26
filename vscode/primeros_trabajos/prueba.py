# PROGRAMA SUPER BUENO

numero_ingresado = int(input("ingrese un numero entero: "))
contador = 1 

while numero_ingresado >= contador:
  print(contador)
  contador += 1
print("El bucle termino!")

# VALIDAR CONTRASEÑA

passaword =   (input("ingrese una contraseña: "))

while passaword != "1234": # CONTRASEÑA GUARDADA
  print("Error: intentelo de nuevo.")
  passaword = input("ingrese una contraseña: 1")
print("acceso concedido!")

# TABLA DE MULTIPLICAR 

numero_a_multiplicar = int(input("ingrese un numero del 1 al 10: "))
numero_2 = 1

while numero_2 <= 10:
  print(f"{numero_a_multiplicar} x {numero_2} = {numero_a_multiplicar * numero_2}")
  numero_2 += 1

# PROMEDIO DE NOTA

cantidad = int(input("Cuantas notas quieres cargar? "))
suma = 0
i = 0

while i < cantidad:
  nota = float(input(f"nota {i + 1}: "))
  suma += nota
  i += 1
print (f"Promedio: {suma / cantidad}")

# NUMEROS DE PARES 

n = int(input("ingrese un numero entero positivo: "))
i = 1

while i <= n:
  if i % 2 == 0:
    print("El numero es par!")
else:
 print("El numero es impar!")    

