# Ejercicio 7: Modificar uno de los scripts anteriores para incluir manejo de errores. Usa un bloque try...except para capturar cualquier error de sqlite3.Error y mostrar un mensaje de error amigable en lugar de que el programa se detenga bruscamente..

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