import pandas as pd

rutaArchivo = "Archivos/e1.txt"
df = pd.read_csv(rutaArchivo)

print(df.head(10))


