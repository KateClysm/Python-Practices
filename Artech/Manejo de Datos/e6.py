# * Ejercicio 6
#     Contar cuántos registros hay en un archivo CSV.

import pandas as pd

rutaArchivo = "Artech/CSV/personas.txt"

df = pd.read_csv(rutaArchivo)

cantidad = len(df)

print(f"El archivo tiene {cantidad} registros.")