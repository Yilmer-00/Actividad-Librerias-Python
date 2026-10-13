# Pronóstico del clima. Dado un array de temperaturas en Celsius, conviértelas todas a Fahrenheit en una
# sola línea (F = C * 9/5 + 32).
# celsius = [18, 22, 25, 19, 30]

import numpy as np

celsius = np.array([18, 22, 25, 19, 30])

Fahrenheit = celsius * 9/5 + 32

print(Fahrenheit)