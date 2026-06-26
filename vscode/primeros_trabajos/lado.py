# NO ME DABA POR CULPA DE DIEGOJADIBOT
import datetime


lado = int(input("ingrese Nro para el valor lado:" ))
perimetro_cuadrado = lado * 5

print ("el perimetro es: ", (perimetro_cuadrado))

#punto 2

base = int(input("ingrese el valor de la base: "))
altura = 5
perimetro_rectangulo = (base + altura) * 2


print ("el resultado del ejersiocio 2 es: ", (perimetro_rectangulo))

# nro 3

kilos = float(input("ingrese cuantos kilos compro: "))
precio_por_kilo = float(input("ingrese el precio por kilo: "))
gasto_total = kilos * precio_por_kilo

print ("gasto un total de: ", gasto_total)

#numero impar o par 

numero = int(input("ingrese su primer numero: "))

if numero % 2 == 0:
    print("el numero ingresado es par!")
else:
    print("el numero es impar!")

# nro 4

caramelos = int(input("ingrese un numero de caramelos a repartir!" \
"a cada uno le tocaran 3 por persona: "))
por_nietos = caramelos // 3
sobrante = caramelos % 3

print("a cada uno le tocan!", por_nietos)
print("sobran! ", sobrante)

# nro 5 control de acces (CORREGIR)

anio_de_nacimiento = int(input("ingrese su año de nacimiento! "))
edad = anio_de_nacimiento - 2026

if edad >= 18:
    print("Eres mayor!" \
"acesso concedido")
else:
    print("eres menor aun acesso denegado")

# nro 6 tienda de descuento

precio = int(input("ingrese el precio del producto:"))
descuento = precio * 0.15

print ("el precio total es: ", descuento)

# nro 7 validar multuplos (CORREGIR)

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))

if n1 % n2 == 0:
    print("Si,", n1, "es multiplo de", n2)
else:
    print("No,", n1, "no es multiplo de", n2)

# calculadora de iva

precio = float(input("ingrese el precio del producto: "))
precio_con_iva = precio * 1.21

print("el recio estimado con iva seria de unos ", precio_con_iva)

# promedio de notas

nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("ingrese su segunda nota: "))
nota3 = float(input("ingrese su tercera nota: "))

promedio = (nota1 + nota2 + nota3) // 3

print("El promedio del alumno es de: ", promedio, "sigue asi!")

# conversor de moneda 

pesos = float(input("ingrese la catidad de pesos a convertir: "))
tipo_cambio = 1381,87 #valor del dolar
pesos * tipo_cambio
dolares = pesos / tipo_cambio
print("podes comprar", dolares, "dolares!")

# REPARTIR 15000 PESOS ENTRE AMIGOS

goles_a = float(input("Goles del A"))
goles_b = float(input("Goles del B"))
diferencia = goles_a - goles_b
print("la diferecia entre el equipo a y el ve es de", diferencia)



