# Datos de partida para los ejercicios 2.1 a 2.5 (inventario de una tienda):

# inventario = {
# "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
# "precio": [45000, 30000, 89000, 8000, 150000],
# "stock": [20, 5, 12, 40, 3],
# }

# Explorar el inventario. Crea un DataFrame con el inventario y muestra las primeras filas, su forma
# (shape), los nombres de las columnas y las estadísticas rápidas (describe).

import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}
df = pd.DataFrame(inventario)

print("--- Primeras filas (head) ---")
print(df.head())

print("\n--- Forma (shape) ---")
print(df.shape)

print("\n--- Nombres de columnas ---")
print(df.columns)

print("\n--- Estadísticas rápidas (describe) ---")
print(df.describe())
