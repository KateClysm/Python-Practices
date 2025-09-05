# Ejercicio 2: Modificar el script del problema 1 para insertar tres registros en la tabla clientes. Cada registro debe tener un nombre de cliente
# diferente.

import sqlite3
db_name = "Clientes.db"
conexion=sqlite3.connect(db_name)
try:
    conexion.execute("INSERT INTO clientes(nombre) VALUES (?)", ("Thomas",))
    conexion.execute("INSERT INTO clientes(nombre) VALUES (?)", ("Ayelén",))
    conexion.execute("INSERT INTO clientes(nombre) VALUES (?)", ("Kate",))
    conexion.execute("INSERT INTO clientes(nombre) VALUES (?)", ("Loredana",))
    conexion.commit()  # Guardar los cambios
    print("Los datos se ingresaron con éxito")
except Exception as e:
    print("Ups:", e)
conexion.close