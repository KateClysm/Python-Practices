# Ejercicio 1: Escribir un script de Python que se conecte a una base de datos SQLite. Si el archivo de la base de datos no existe, se creará
# automáticamente. Luego, el script debe crear una tabla llamada clientes con las columnas id (entero, clave primaria) y nombre(texto).


import sqlite3
db_name = "Clientes.db"
conexion=sqlite3.connect(db_name)
try:
    conexion.execute("""create table clientes (id integer primary key autoincrement, nombre text)""")
    print("se creo la tabla clientes")
except Exception as e:
    print("Ups: ", e)
conexion.close
