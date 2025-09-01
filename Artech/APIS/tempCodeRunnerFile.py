import requests
import pandas as pd

url = "http://api.worldbank.org/v2/country/AR/indicator/VC.IHR.PSRC.P5?format=json"

response = requests.get(url)
response.raise_for_status()  # Lanza error si la petición falla
data = response.json()

#print(data)
records = data[1]

df = pd.DataFrame(records)

print("Columnas disponibles en el DataFrame:")
print(df.columns.tolist())