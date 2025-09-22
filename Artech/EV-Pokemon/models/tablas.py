import sqlite3
import pandas as pd

def create_table_from_df(conn: sqlite3.Connection, table_name: str, df: pd.DataFrame) -> None:
    """Crea una tabla SQLite según las columnas y tipos del DataFrame."""


    type_mapping = {
        'int64': 'INTEGER',
        'float64': 'REAL',
        'object': 'TEXT',
        'bool': 'INTEGER',
        'datetime64[ns]': 'TEXT'
    }

    # Construir la lista de columnas con tipos SQL
    columns = []
    for col, dtype in df.dtypes.items(): 
        sql_type = type_mapping.get(str(dtype), "TEXT")   
        column_def = '"' + col + '" ' + sql_type
        columns.append(column_def)

    # Crear la sentencia SQL
    columns_sql = ""
    for i in range(len(columns)):
        if i == 0:
            columns_sql += columns[i]
        else:
            columns_sql += ", " + columns[i]

    query = 'CREATE TABLE IF NOT EXISTS "' + table_name + '" (' + columns_sql + ')'

    # Ejecutar la creación de la tabla
    with conn:
        conn.execute(query)


def insert_row(conn: sqlite3.Connection, table_name: str, row: dict[str, str | int | float | bool]) -> None:
    """Inserta un registro individual en la tabla SQLite."""
    keys = ""
    placeholders = ""
    values = tuple(row.values())

    # Construir la lista de columnas y los signos ?
    first = True
    for k in row.keys():
        if first:
            keys += '"' + k + '"'
            placeholders += "?"
            first = False
        else:
            keys += ", " + '"' + k + '"'
            placeholders += ", ?"

    query = 'INSERT INTO "' + table_name + '" (' + keys + ') VALUES (' + placeholders + ')'

    with conn:
        conn.execute(query)


def insert_dataframe(conn: sqlite3.Connection, table_name: str, df: pd.DataFrame) -> None:
    """Inserta todos los registros de un DataFrame en la tabla SQLite."""
    df.to_sql(table_name, conn, if_exists='append', index=False)
