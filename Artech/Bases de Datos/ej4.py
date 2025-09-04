# Ejercicio 4: Escribir un script que pida al usuario que ingrese un ID de cliente. El script debe buscar y mostrar el nombre del cliente correspondiente a ese ID. Si el ID no existe, debe mostrar un mensaje de error.


import sqlite3
conexion=sqlite3.connect("bd1.db")

id_cliente = int(input('Ingrese un id de cliente: '))

try:
    puntero = conexion.execute("SELECT nombre FROM clientes WHERE id = ?", (id_cliente,))
    nombre_cliente = puntero.fetchone()
    if nombre_cliente!=None:
        print(nombre_cliente[0])
    else:
        print("No existe un cliente con dicho id.")
except Exception as e:
    print("Ups:", e)

conexion.close
