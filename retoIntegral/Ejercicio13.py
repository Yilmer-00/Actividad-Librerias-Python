import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

estudiantes = {
    "horas_estudio": [2, 4, 5, 6, 8, 10, 3, 7, 9, 1],
    "asistencia": [60, 70, 75, 80, 90, 95, 65, 85, 92, 50],
    "aprobo": [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
}

df = pd.DataFrame(estudiantes)

print("--- DATOS ---")
print(df)

print("\n--- ESTADISTICAS ---")
print(df.describe())

df["promedio_semanal"] = df["horas_estudio"] / 7

filtro = df[(df["aprobo"] == 1) & (df["horas_estudio"] < 6)]
print("\n--- APROBARON CON MENOS DE 6 HORAS ---")
print(filtro)

promedio = np.mean(df["asistencia"])
desviacion = np.std(df["asistencia"])

print("\nPromedio de asistencia:", promedio)
print("Desviación estándar:", desviacion)

X = df[["horas_estudio", "asistencia"]]
y = df["aprobo"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)
precision = accuracy_score(y_test, predicciones)

print("\nPrecisión:", precision)

nuevo_estudiante = pd.DataFrame({"horas_estudio": [5], "asistencia": [78]})
resultado = modelo.predict(nuevo_estudiante)

if resultado[0] == 1:
    print("\nResultado: Aprueba")
else:
    print("\nResultado: No aprueba")
