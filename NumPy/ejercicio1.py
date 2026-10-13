# Notas de un grupo. Crea un array con las notas de un grupo y calcula su promedio, máximo, mínimo y
# desviación estándar.
# notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]

import numpy as np


notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
array_notas = np.array(notas)

promedio = np.mean(array_notas)
maximo = np.max(array_notas)
minimo = np.min(array_notas)
desviacion = np.std(array_notas)  

print(f"Notas: {array_notas}")
print(f"Promedio: {promedio:.2f}")
print(f"Nota máxima: {maximo}")
print(f"Nota mínima: {minimo}")
print(f"Desviación estándar: {desviacion:.2f}")