from models.connect import get_connection

def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    edad INTEGER)"""
        cursor.execute(query)
        conn.commit()

def insert_datos(nombre:str, edad:int):
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)"
        datos = (nombre, edad)
        cursor.execute(query, datos) # -> "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad)
        conn.commit()


def select():
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM usuarios"
        resultado = cursor.execute(query).fetchall()
    return resultado

# .fetchall() → trae todos los resultados de esa consulta en forma de lista de tuplas.
# resultado → almacena esa lista de tuplas para usarla después en tu programa.