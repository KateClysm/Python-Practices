# Ejercicio 9: Crear un script que primero genere una base de datos SQLite con una tabla llamada productos. Inserta al menos 5 registros. Luego, lee toda la tabla de productos y la convierte en un DataFrame de pandas. Finalmente, imprime el DataFrame para verificar que los datos se han cargado correctamente.




import sqlite3, pandas as pd



#Crea una tabla
def create_table(connection, t_name, attributes):
    try:
        query = f"CREATE TABLE IF NOT EXISTS {t_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {attributes})"  #Formateo un string
        connection.execute(query) #lo paso como query
        print(f"Se creó (o ya existía) la tabla {t_name}")
    except Exception as e:
        print("Ups: La tabla clientes ya existe ", e)
    connection.close


#Muestra toda la info de una base de datos
def print_table(connection, t_name):
    try:
        query = f"SELECT * FROM {t_name}"
        puntero = connection.execute(query)
        for fila in puntero:
            print(fila)
    except Exception as e:
        print("Ups:", e)


#Inserta elementos de una lista en una tabla
# a_names -> ["nombre", "edad"]
# items -> [("...", 12), ("...", 12),  ...]
# item -> ("...", 12)
def insert(connection, t_name, a_names, items):  
    try:
        if(len(items) == 0):
            print('No se ingresó los valores requeridos para una inserción')
            return
        else:
            placeholders = ", ".join(["?"] * len(a_names))  #->  "?, ?, ?, ..."
            a_names = ", ".join(a_names) # -> "nombre, edad, ..."

            query = f"INSERT INTO {t_name} ({a_names}) VALUES ({placeholders})"
            
            #connection.executemany(query, items) Hace lo mismo que abajo

            for item in items:
                connection.execute(query, item)  
            if len(items) == 1:
                print('Registro insertado con éxito')
            else:
                print('Registros insertados con éxito')
            
        connection.commit()
        
    except Exception as e:
        print("Ups:", e)


#Base de datos a DataFrame
def dbtable_to_df(connection, t_name):
    sql_query = f"SELECT * FROM {t_name};"
    df = pd.read_sql_query(sql_query, connection)
    print(f"DataFrame Generado con éxito: \n--------------------------------------------------------------\n{df.head()}")
    #connection.close()
    return df


#------------------Conexión Base de datos----------------------------------------------------
db_name = "Sales.db"
connection = sqlite3.connect(db_name) #Si no existe la crea


#--------------Programa Principal-----------------------------------------------------------

create_table(connection, "Products", "Name varchar(30), QuantityPerUnit int, Price decimal")
print_table(connection, "Products")
insert(
    connection,
    "products",                          
    ["Name", "QuantityPerUnit", "Price"],
    [
        ("Manzanas", 10, 3.50),
        ("Peras", 8, 4.20),
        ("Bananas", 12, 2.80),
        ("Naranjas", 15, 5.00),
        ("Uvas", 20, 7.90)
    ]
)

df_from_db = dbtable_to_df(connection, "Products")
connection.close