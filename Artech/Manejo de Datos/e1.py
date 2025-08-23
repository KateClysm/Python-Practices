# * Ejercicio 1
#     Cargar un archivo CSV y mostrar sus primeras 10 filas.


import pandas as pd

rutaArchivo = "CSV/intereses.txt"
df = pd.read_csv(rutaArchivo)

print(df.head(10))


