""" 
4. Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.

"""

try:
    archivo = open('archivos/file.txt')
    contenido = archivo.read()
    archivo.close() #No va en un finally, porque existe la chance de que el archivo no exista, y daría error intentar cerrarlo al final.
except FileNotFoundError:
    print("No se pudo encontrar el archivo file.txt")


#------------------Versión con With----------------------------------------------------------------------------------------------------------

try:
    with open('archivos/file.txt', 'r') as archivo: #with cierra el archivo por nosotros
        contenido = archivo.read()
except FileNotFoundError:
    print("No se pudo encontrar el archivo file.txt")