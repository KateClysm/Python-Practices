# Ejercicio 3: Escribir un nuevo script que se conecte a la base de datos mi_base_de_datos.db, seleccione todos los registros de la tabla clientes y los imprima en la consola.

import sqlite3
conexion=sqlite3.connect("bd1.db")
try:
    puntero = conexion.execute("select id, nombre from clientes")
    for fila in puntero:
        print(fila)
except Exception as e:
    print("Ups:", e)
conexion.close