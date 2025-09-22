import json
import pandas as pd
import requests

def get_api_conn(api_url):
    """Realiza una petición GET a la API y retorna los datos en JSON o None si falla."""
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None
    

def save_as_json(dict_info, ruta_json):
    """Guarda un diccionario o lista en un archivo JSON."""
    with open(ruta_json, "w", encoding="utf-8") as f: 
        json.dump(dict_info, f, indent=4, ensure_ascii=False)


def open_json(ruta_json):
    """Abre un archivo JSON y retorna su contenido como diccionario o lista."""
    with open(ruta_json, "r", encoding="utf-8") as f:
        return json.load(f)
    

def normalize_json(data):
    """Normaliza datos JSON anidados y retorna un DataFrame de pandas."""
    df = pd.json_normalize(data)
    return df


def df_to_csv(df, ruta_csv):
    """Guarda un DataFrame de pandas en un archivo CSV."""
    df.to_csv(ruta_csv, index=False, encoding="utf-8")


def csv_to_df(ruta_csv):
    """Lee un archivo CSV y retorna un DataFrame de pandas."""
    return pd.read_csv(ruta_csv, encoding="utf-8")
