from database.connect import get_db_conn
from models.tablas import create_table_from_df, insert_row, insert_dataframe
import pandas as pd


link_pokeapi = "https://pokeapi.co/api/v2/pokemon?limit=1281"
ruta_json = "Artech/EV-Pokemon/json/pokeapi.json"
ruta_csv = "Artech/EV-Pokemon/csv/pokeapi.csv"

conn = get_db_conn()

df = pd.DataFrame({
    'id': [1, 2],
    'name': ['Bulbasaur', 'Ivysaur'],
    'type': ['Grass/Poison', 'Grass/Poison'],
    'hp': [45, 60]
})

create_table_from_df(conn, "pokemon", df)

insert_row(conn, "pokemon", {'id': 3, 'name': 'Venusaur', 'type': 'Grass/Poison', 'hp': 80})

insert_dataframe(conn, "pokemon", df)

conn.close()