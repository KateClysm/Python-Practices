""" 
1. Se tiene un archivo con la pregunta “¿Cómo estás hoy?” 
llamado pregunta.txt. 
Se pide leerlo y mostrar la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. 
Después, guardar la respuesta dada por el usuario en el archivo.
Por ejemplo, se tiene el archivo pregunta.txt que originalmente tiene:
¿Cómo estás hoy?

Y el usuario da la respuesta: “¡Bien, porque me comí una hamburguesa!”
Entonces el archivo debería quedar de la forma:
¿Cómo estás hoy?
¡Bien, porque me comí una hamburguesa! 
"""

#--------------------------------------------------------------------------------------------------------------------------------
archivo = open('pregunta.txt')
contenido = archivo.read()
archivo.close()
print(contenido)
respuesta = input('Ingrese una respuesta: ')

archivo = open("pregunta.txt", "a")
archivo.write(f'\n{respuesta}')
archivo.close()

archivo = open('pregunta.txt')
contenido = archivo.read()
archivo.close()
print(contenido) 

#--------------------------------------------------------------------------------------------------------------------------------
#Usando With:
#cierra automáticamente el archivo aunque ocurra un error

with open('pregunta.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)

respuesta = input('Ingrese una respuesta: ')

with open("pregunta.txt", "a") as archivo:
    archivo.write(f'\n{respuesta}')  

with open('pregunta.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)


#--------------------------------------------------------------------------------------------------------------------------------
#Usando With y r+
#Si leemos y luego escribimos,  el “puntero de posición” para escribir queda al final, lo cual produce que escribamos al final del archivo.

with open("pregunta.txt", "r+") as archivo:
    contenido = archivo.read()
    print(contenido)
    respuesta = input("Ingrese una respuesta: ")

    archivo.write(f'\n{respuesta}')


#--------------------------------------------------------------------------------------------------------------------------------
#Usando Seek
with open("pregunta.txt", "a+") as archivo:
    archivo.seek(0)
    print(archivo.read())

    respuesta = input("Ingrese una respuesta: ")
    archivo.write(f'\n{respuesta}')