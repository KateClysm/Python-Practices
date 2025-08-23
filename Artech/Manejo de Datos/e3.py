# * Ejercicio 3
#     Leer un Excel y listar las columnas que contiene.

import pandas as pd

df = pd.read_excel("C:/Users/katec/OneDrive/Escritorio/PROYECTOS/Python-Practices/Artech/Excel/viajes.xlsx", sheet_name="Sheet1")

print()
columns = df.columns
print(columns)

print("--------------------------------------------------------------------")

data_content = df[['Destino', 'Precio', 'Clima', 'Transporte', 'Duración', 'Categoría']]
print(data_content)