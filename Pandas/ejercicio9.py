# Leer datos desde un archivo. Guarda el DataFrame como inventario.csv (df.to_csv) y luego léelo de
# nuevo con pd.read_csv. Verifica que los datos sean iguales.

import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}
df = pd.DataFrame(inventario)

df.to_csv("inventario.csv", index=False)
print("¡Archivo 'inventario.csv' guardado con éxito!\n")

df_leido = pd.read_csv("inventario.csv")

print(" DataFrame leído desde el archivo CSV ")
print(df_leido)

son_iguales = df.equals(df_leido)

print(f"\n¿Los datos del DataFrame original y el leído son iguales? {son_iguales}")
