def pedir_numero():
    numero = int(input("Ingrese un número entero positivo: "))

    while numero <= 0:
        print("Error. Debe ingresar un número positivo.")
        numero = int(input("Ingrese nuevamente el número: "))

    return numero


def es_primo(numero):
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        print("El número es Primo")
    else:
        print("El número NO es Primo")


# Programa principal
num = pedir_numero()
es_primo(num)
