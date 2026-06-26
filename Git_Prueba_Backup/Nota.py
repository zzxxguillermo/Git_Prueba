def pedir_nota():
    nota = int(input("Ingrese una nota del 1 al 10: "))

    while nota < 1 or nota > 10:
        print("Error. Nota inválida.")
        nota = int(input("Ingrese nuevamente la nota: "))

    return nota


def evaluar_nota(nota):
    if nota >= 7:
        print("Aprobado")
    else:
        print("Desaprobado")


nota_final = pedir_nota()
evaluar_nota(nota_final)






