# Ventas de una tienda. Convierte la lista de ventas diarias en un array de numpy, aplica un aumento del
# 10% a todas las ventas (sin usar bucles) y calcula el total de la semana.
# ventas = [120000, 95000, 150000, 80000, 200000, 175000, 110000]

import numpy as np

ventas = [120000, 95000, 150000, 80000, 200000, 175000, 110000]
array_ventas = np.array(ventas)

ventas_aumentadas = array_ventas * 1.10

total_semana = np.sum(ventas_aumentadas)

print(f"Ventas originales: {array_ventas}")
print(f"Ventas con 10% de aumento: {ventas_aumentadas}")
print(f"Total de la semana: {total_semana:,.2f}")