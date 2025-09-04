# Ejercicio 6: Escribir un script que le pida al usuario un ID de cliente. El script debe eliminar el registro correspondiente a ese ID y confirmar que la eliminación fue exitosa

import sqlite3
conexion=sqlite3.connect("bd1.db")

id_cliente = int(input('Ingrese un id de cliente: '))

try:
    conexion.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexion.commit()
    print("Cliente eliminado satisfactoriamente.")

except Exception as e:
    print("Ups:", e)

conexion.close