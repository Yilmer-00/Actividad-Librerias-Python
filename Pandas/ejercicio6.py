# Productos por reponer. Filtra y muestra solo los productos con stock menor a 10.
import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}
df = pd.DataFrame(inventario)

print("Productos por reponer (stock < 10)")
print(df[df["stock"] < 10])
