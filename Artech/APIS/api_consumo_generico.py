import requests
import json
import pandas as pd


#-----------------------Variables-----------------------------------------------------------------------------------------------------------------------


link_pokeapi = "https://pokeapi.co/api/v2/pokemon?limit=1281"
ruta_json = "Artech/JSON/pokeapi.json"
ruta_csv = "Artech/CSV/pokeapi.csv"


#-----------------------Funciones Generales-------------------------------------------------------------------------------------------------------------


""" 
Hace la petición a la api, chequea por errores y devuelve un diccionario
info = requests.get(api_url)  -> objeto response de la librería requests
info.json() -> Diccionario en formato JSON
"""
def get_api(api_url):
    info = requests.get(api_url)
    info.raise_for_status()
    return info.json() 


""" 
Guarda un diccionario que esté en formato JSON en una ruta dada
"w": modo de apertura → write (escribir) -> Si el archivo ya existe, se sobrescribe, si no existe, lo crea.
encoding="utf-8": asegura que se guarden bien caracteres especiales (como acentos, ñ, etc.)
with ... as f: → abre el archivo y lo cierra automáticamente al terminar, aunque haya errores
f es el objeto archivo donde vamos a escribir
indent=4 → agrega indentación de 4 espacios para que el archivo quede legible
"""
def save_as_json(dict_info, ruta_json):
    with open(ruta_json, "w", encoding="utf-8") as f: 
        json.dump(dict_info, f, indent=4)


""" 
Lee un archivo JSON dada la ruta del mismo y lo retorna en formato dict o list, dependiendo de la estructura del JSON
"r": modo de apertura → read (leer)
json.load(f): toma el contenido del archivo (texto en formato JSON) y lo PARSEA, convirtiéndolo en el tipo de dato equivalente en Python
"""
def open_json(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as f:
       a_json = json.load(f)
       return a_json


""" 
Toma un dict o list y lo aplana hasta no dejar ninguna estructura dentro. Luego, lo convierte a DataFrame y lo retorna
"""
def normalize_data(data):
    df = pd.json_normalize(data)
    return df


"""
Guarda un DataFrame como archivo CSV en una ruta dada
"""
def save_to_csv(df, ruta_csv):
    df.to_csv(ruta_csv, index=False, encoding="utf-8")


""" 
Lee un archivo CSV dada la ruta del mismo y lo retorna en formato DataFrame
"""
def read_csv(ruta_csv):
    df = pd.read_csv(ruta_csv, encoding="utf-8")
    return df





#-----------------------Programa Principal--------------------------------------------------------------------------------------------------------------


api_info = get_api(link_pokeapi)                            # Llama a la API
save_as_json(api_info, ruta_json)                           # Guardamon en un JSON
pokemon_json = open_json(ruta_json)                         # Lee un JSON
pokemon_df = normalize_data(pokemon_json["results"])        # Conversión a DataFrame -> En este caso esp. aclaramos que queremos solo la parte de results
#print(pokemon_df)                                          # Chequeamos el estado del DataFrame
save_to_csv(pokemon_df, ruta_csv)                           # Guardamos en un CSV
print(read_csv(ruta_csv))                                   # Leemos el CSV como un DataFrame