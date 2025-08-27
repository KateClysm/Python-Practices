# * Ejercicio 5
#     Ordenar un CSV por la columna "Edad" de menor a mayor.

import pandas as pd

rutaArchivo = "Artech/CSV/personas.txt"

df = pd.read_csv(rutaArchivo)

# Ordenar por la columna "Edad"
df_ordenado = df.sort_values(by="Edad", ascending=True)

# Guardar el archivo ordenado en un nuevo CSV
df_ordenado.to_csv("Artech/CSV/archivo_ordenado.csv", index=False)

print("CSV ordenado correctamente por Edad.")