# Valor del inventario. Agrega una columna valor_inventario (precio * stock) y otra columna reponer que
# sea True si el stock es menor a 10. Muestra el DataFrame resultante.

import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}
df = pd.DataFrame(inventario)

# agregamos la columna valor_inventario
df["valor_inventario"] = df["precio"] * df["stock"]

# agregamos la columna reponer
df["reponer"] = df["stock"] < 10

print("DataFrame resultante:")
print(df)