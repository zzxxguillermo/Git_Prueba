materias = ["Matemáticas", "Lengua", "Ciencias", "Historia"]

total_materias = len(materias)
print(f"Total de materias: {total_materias}")

# mostar el primer elemento de la lista
print(f"Primer materia: {materias[0]}")

# usamos el len(materias) -1 para calcular dinamicamente el índice del último elemento
print(f"Última materia: {materias[len(materias) - 1]}")