# Ejercicio 5: Crear un script que le pida al usuario un ID y un nuevo nombre. El script debe actualizar el registro con el ID proporcionado con el nuevo nombre. Confirma la actualización imprimiendo un mensaje.

import sqlite3
conexion=sqlite3.connect("bd1.db")

id_cliente = int(input('Ingrese un id de cliente: '))
nombre_cliente = input('Ingrese un nombre: ')


try:
    conexion.execute("UPDATE clientes SET nombre = ? WHERE id = ?", (nombre_cliente, id_cliente))
    conexion.commit()
    print("Nombre actualizado.")

except Exception as e:
    print("Ups:", e)

conexion.close