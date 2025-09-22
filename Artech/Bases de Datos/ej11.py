# Ejercicio 11: Simular un escenario más realista. Crea una nueva base de datos llamada ventas.db con dos tablas: productos y ventas. La tabla ventas debe tener un id_producto para relacionarse con la tabla productos. Inserta algunos datos en ambas tablas y luego crea un DataFrame que muestre el nombre del producto y la cantidad vendida.


import sqlite3, pandas as pd


#Crea una tabla
def create_table(connection, t_name, attributes):
    try:
        query = f"CREATE TABLE IF NOT EXISTS {t_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {attributes})"
        with connection:
            connection.execute(query) 
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
def select(connection, t_name, attributes, query_join=None, condition=None):
    try:
        query_join = query_join if query_join else ""
        condition  = f"WHERE {condition}" if condition else ""
        query = f"SELECT {attributes} FROM {t_name} {query_join} {condition}"
        with connection:
            df = pd.read_sql_query(query, connection)
            print(f"DataFrame Generado con éxito \n--------------------------------------------------------------\n")
        return df
    except Exception as e:
        print("Ups:", e)
    



#------------------Conexión Base de datos----------------------------------------------------
db_name = "Artech/DBS/Sales.db"
connection = sqlite3.connect(db_name) 
connection.execute("PRAGMA foreign_keys = ON;")  #Activa las foreign keys

#--------------Programa Principal-----------------------------------------------------------

create_table(connection, "Products", "Name varchar(30), QuantityPerUnit int, Price decimal")
create_table(connection, "Sales", "QuantitySold int, IdProduct int, FOREIGN KEY (IdProduct) REFERENCES Products(id)")
insert(
    connection,
    "Products",                          
    ["Name", "QuantityPerUnit", "Price"],
    [
        ("Manzanas", 10, 200),   # id = 1
        ("Peras", 8, 150),       # id = 2
        ("Bananas", 12, 180),    # id = 3
        ("Naranjas", 15, 90),    # id = 4
        ("Uvas", 20, 120)        # id = 5
    ]
)
insert(
    connection,
    "Sales",                          
    ["QuantitySold", "IdProduct"],
    [
        (5, 1),   # 5 Manzanas  (Product id=1)
        (3, 2),   # 3 Peras     (Product id=2)
        (7, 3),   # 7 Bananas   (Product id=3)
        (10, 1),  # 10 Manzanas (Product id=1 otra vez)
        (2, 5)    # 2 Uvas      (Product id=5)
    ]
)
df_from_db = table_to_df(connection, "Products")
print(select(connection, t_name="Products", attributes="*", condition="Price > 100"))
join = "INNER JOIN Sales s ON p.id = s.IdProduct"
print(select(connection, t_name="Products p", attributes="p.Name, s.QuantitySold", query_join=join))
