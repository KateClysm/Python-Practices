# Ejercicio 3: Escribir un nuevo script que se conecte a la base de datos mi_base_de_datos.db, seleccione todos los registros de la tabla clientes y los imprima en la consola.

import sqlite3
db_name = "Clientes.db"
conexion=sqlite3.connect(db_name)
try:
    puntero = conexion.execute("SELECT * FROM clientes")
    print(puntero)
    for fila in puntero:
        print(fila)
except Exception as e:
    print("Ups:", e)
conexion.close