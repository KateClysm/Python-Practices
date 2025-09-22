import sqlite3, pandas as pd


#Crea una tabla
def create_table(connection, t_name, attributes):
    try:
        query = f"CREATE TABLE IF NOT EXISTS {t_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {attributes})"  #Formateo un string
        with connection:
            connection.execute(query) #lo paso como query
            print(f"Se creó (o ya existía) la tabla {t_name}")
    except Exception as e:
        print("Ups: La tabla clientes ya existe ", e)
    connection.close


#Muestra toda la info de una base de datos
def print_table(connection, t_name):
    try:
        query = f"SELECT * FROM {t_name}"
        with connection:
            puntero = connection.execute(query)
            for fila in puntero:
                print(fila)
    except Exception as e:
        print("Ups:", e)


#Inserta elementos de una lista en una tabla
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

            with connection:
                for item in items:
                    connection.execute(query, item)  
                if len(items) == 1:
                    print('Registro insertado con éxito')
                else:
                    print('Registros insertados con éxito')
            
                connection.commit()
        
    except Exception as e:
        print("Ups:", e)


#Toda una tabla a DataFrame
def table_to_df(connection, t_name):
    sql_query = f"SELECT * FROM {t_name};"
    with connection:
        df = pd.read_sql_query(sql_query, connection)
        print(f"DataFrame Generado con éxito: \n--------------------------------------------------------------\n{df.head()}")
    return df


#Tabla que recibe una query condicionada y devuelve el dataframe
def select_by_condition(connection, t_name, attributes, condition):
    try:
        query = f"SELECT {attributes} FROM {t_name} WHERE {condition}"
        with connection:
            df = pd.read_sql_query(query, connection)
            print(f"DataFrame Generado con éxito: \n--------------------------------------------------------------\n")
        return df
    except Exception as e:
        print("Ups:", e)
    


#------------------Conexión Base de datos----------------------------------------------------
db_name = "Artech/DBS/Sales.db"
connection = sqlite3.connect(db_name) #Si no existe la crea


#--------------Programa Principal-----------------------------------------------------------

create_table(connection, "Products", "Name varchar(30), QuantityPerUnit int, Price decimal")
print_table(connection, "Products")
insert(
    connection,
    "Products",                          
    ["Name", "QuantityPerUnit", "Price"],
    [
        ("Manzanas", 10, 200),
        ("Peras", 8, 101),
        ("Bananas", 12, 180),
        ("Naranjas", 15, 5.00),
        ("Uvas", 20, 99)
    ]
)
df_from_db = table_to_df(connection, "Products")
print(select_by_condition(connection, "Products", "*", "Price > 100"))