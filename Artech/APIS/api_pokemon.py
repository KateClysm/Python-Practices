import requests
import json
import pandas as pd


#-----------------------Variables-----------------------------------------------------------------------------------------------------------------------


link_pokeapi = "https://pokeapi.co/api/v2/pokemon?limit=1281"
ruta_pokemon_json = "Artech/JSON/pokeapi.json"
ruta_pokemon_csv = "Artech/CSV/pokeapi.csv"
ruta_pokemonystats_csv = "Artech/CSV/pokemon_y_stats_10.csv"


#-----------------------Funciones Generales-------------------------------------------------------------------------------------------------------------


def get_api(api_url):
    info = requests.get(api_url)
    info.raise_for_status()
    return info.json() 

def save_as_json(dict_info, ruta_json):
    with open(ruta_json, "w", encoding="utf-8") as f: 
        json.dump(dict_info, f, indent=4)

def open_json(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as f:
       a_json = json.load(f)
       return a_json

def normalize_data(data):
    df = pd.json_normalize(data)
    return df

def save_to_csv(df, ruta_csv):
    df.to_csv(ruta_csv, index=False, encoding="utf-8")

def read_csv(ruta_csv):
    df = pd.read_csv(ruta_csv, encoding="utf-8")
    return df



#-----------------------Programa Principal--------------------------------------------------------------------------------------------------------------


api_info = get_api(link_pokeapi)                            # Llama a la API
save_as_json(api_info, ruta_pokemon_json)                   # Guardamon en un JSON
pokemon_json = open_json(ruta_pokemon_json)                 # Lee un JSON
pokemon_df = normalize_data(pokemon_json["results"])        # Conversión a DataFrame -> En este caso esp. aclaramos que queremos solo la parte de results
#print(pokemon_df)                                          # Chequeamos el estado del DataFrame
save_to_csv(pokemon_df, ruta_pokemon_csv)                   # Guardamos en un CSV
print(read_csv(ruta_pokemon_csv))                           # Leemos el CSV como un DataFrame


#-----------------------Generación de un DF, Formateo de listas a strings, Unión de dos DF------------------------------------------------------------

#Creo mis listas (columnas)
poke_id = []
types = []
height = []
weight = []
location_area_encounters = []
abilities = []
base_experience = []

#Por cada item en pokemon_df, volvemos cada fila una Serie de Pandas, utilizando el nombre de las columnas como claves de acceso.
for index, row in pokemon_df[:10].iterrows():  #Lo reduje al df a 10 elementos para que no sea eterno el tiempo de espera entre tantas llamadas
    url = row['url']
    dict_stats = get_api(url)   #Llamada a la api de la info del pokemon
 

    poke_id.append(dict_stats["id"])

    #Formateamos los tipos
    types_list = [t['type']['name'] for t in dict_stats['types']]  #['grass', 'poison']
    types_string = ",".join(types_list)  #['grass', 'poison'] -> 'grass,poison'
    types.append(types_string)

    height.append(dict_stats["height"])
    weight.append(dict_stats["weight"])
    location_area_encounters.append(dict_stats["location_area_encounters"])

    #Formateamos las habilidades
    abilities_list = [t['ability']['name'] for t in dict_stats['abilities']]
    abilities_string = ",".join(abilities_list)  
    abilities.append(abilities_string)

    base_experience.append(dict_stats["base_experience"])
    
#Creamos el DataFrame de los stats
stats_df = pd.DataFrame({
    "id" : poke_id,
    "types" : types,
    "height" : height,
    "weight" : weight,
    "location_area_encounters" : location_area_encounters,
    "abilities" : abilities,
    "base_experience" : base_experience
})

#print(stats_df)

#Unimos dos DataFrames según el largo de uno.
pokemon_y_stats_df = pd.concat([pokemon_df[:len(stats_df)], stats_df], axis=1)  #con concat unimos los dataframes por columnas

#len(lista o dataframe) -> devuelve un número
#df[:num] -> acorta el dataframe
#pokemon_df[:len(stats_df)]  ->   ejemplo: si len(stats_df) = 5, pokemon_df[:5] -> Se acorta a 5 elementos
#.concat([df, otrodf], axis)

print(pokemon_y_stats_df) #Chequeamos

save_to_csv(pokemon_y_stats_df, ruta_pokemonystats_csv) #Guardamos a csv el dataframe unido