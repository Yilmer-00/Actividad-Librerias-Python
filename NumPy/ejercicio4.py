# Calificaciones por estudiante y materia. Crea una matriz de 3 estudiantes por 4 materias. Calcula el
# promedio de cada estudiante (por fila) y el promedio de cada materia (por columna).
# calificaciones = [
# [8.5, 7.0, 9.0, 8.0], # Carlos
# [6.0, 7.5, 8.0, 7.0], # Ana
# [9.0, 8.5, 9.5, 9.0], # Luis
# ]

# Pista: usa .mean(axis=1) para promediar por fila y .mean(axis=0) para promediar por columna.

import numpy as np

# 1. Definir la lista de listas y convertirla en una matriz de NumPy (3x4)
calificaciones = [
    [8.5, 7.0, 9.0, 8.0],  # Carlos
    [6.0, 7.5, 8.0, 7.0],  # Ana
    [9.0, 8.5, 9.5, 9.0],  # Luis
]

matriz_calificaciones = np.array(calificaciones)

# 2. Calcular el promedio de cada estudiante (por fila -> axis=1)
promedio_estudiantes = np.mean(matriz_calificaciones, axis=1)

# 3. Calcular el promedio de cada materia (por columna -> axis=0)
promedio_materias = np.mean(matriz_calificaciones, axis=0)

# 4. Mostrar los resultados
print("Matriz de calificaciones:")
print(matriz_calificaciones)
print("Promedio de cada estudiante:")
print(f"Carlos: {promedio_estudiantes[0]:.2f}")
print(f"Ana: {promedio_estudiantes[1]:.2f}")
print(f"Luis: {promedio_estudiantes[2]:.2f}")

print("Promedio de cada materia:")
for i, prom in enumerate(promedio_materias, 1):
    print(f"Materia {i}: {prom:.2f}")
