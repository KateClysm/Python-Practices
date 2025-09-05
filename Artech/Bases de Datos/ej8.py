# Ejercicio 8: Escribir un script que realice las siguientes tareas en orden:
# o Conectarse a la base de datos.
# o Insertar un nuevo cliente llamado "Juan".
# o Imprimir todos los clientes de la tabla para verificar la inserción.
# o Actualizar el nombre de "Juan" a "Juan Pérez".
# o Imprimir todos los clientes nuevamente para confirmar el cambio.
# o Eliminar el registro de "Juan Pérez".
# o Imprimir todos los clientes una última vez para demostrar que ha sido eliminado.



import sqlite3


#Muestra toda la info de la bd
def imprimir_db(conection):
    try:
        puntero = conection.execute("select * from clientes")
        for fila in puntero:
            print(fila)
    except Exception as e:
        print("Ups:", e)

#Crea un cliente
def create_client(conection):
    nombre = input('Nombre del usuario que desea crear: ')
    try:
        conection.execute("INSERT INTO clientes(nombre) VALUES (?)", (nombre,))
        print('Usuario creado con éxito.')
        conection.commit()
        
    except Exception as e:
        print("Ups:", e)

#Actualiza un nombre según un id
def update_name(conection):
    id_cliente = int(input('Ingrese el id del cliente que quiere actualizar: '))
    nuevo_nombre = input('Ingrese un nuevo nombre para el cliente: ')
    try:
        conection.execute("UPDATE clientes SET nombre = ? WHERE id = ?", (nuevo_nombre, id_cliente))
        print("Nombre actualizado.")
        conection.commit()
    except Exception as e:
        print("Ups:", e)

#Elimina un registro por id
def delete_client(conection):
    id_cliente = int(input('Ingrese el id del cliente que quiere eliminar: '))
    try:
        conection.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        print("Cliente eliminado satisfactoriamente.")
        conection.commit()
    except Exception as e:
        print("Ups:", e)


#------------------Conexión Base de datos----------------------------------------------------

conection=sqlite3.connect("bd1.db")


#--------------Programa Principal-----------------------------------------------------------

create_client(conection)
imprimir_db(conection)
update_name(conection)
imprimir_db(conection)
delete_client(conection)
conection.close