# Ordenar y resumir. Ordena el inventario del producto más caro al más barato (sort_values) y calcula el
# precio promedio de todos los productos.
import pandas as pd

# Datos de partida
inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

df = pd.DataFrame(inventario)

df_ordenado = df.sort_values(by="precio", ascending=False)


print(df_ordenado)

precio_promedio = df["precio"].mean()

print("\n el precio promedio es:")
print(f"El precio promedio de los productos es: {precio_promedio}")
