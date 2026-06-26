def pedir_nota():
    nota = int(input("Ingrese una nota del 1 al 10: "))

    while nota < 1 or nota > 10:
        print("Error. La nota debe estar entre 1 y 10.")
        nota = int(input("Ingrese nuevamente la nota: "))

    return nota


def evaluar_nota(nota):
    if nota >= 7:
        print("Aprobado")
    else:
        print("Desaprobado")


# Programa principal
nota_final = pedir_nota()
evaluar_nota(nota_final)
python CodigoWass.py
