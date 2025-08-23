# * Ejercicio 4
#     Filtrar de un CSV a todas las personas mayores de 30 años.

import pandas as pd

rutaArchivo = "Artech/CSV/personas.txt"
personas = pd.read_csv(rutaArchivo)

print(f"\n {personas.head(10)}\n...")

# Filtrar filas donde Edad > 30
mayores30 = personas[personas["Edad"] > 30]

# Imprimir el resultado
print("\nPersonas mayores a 30:")
print(mayores30)