""" 
4. Se tiene un archivo con el siguiente texto:

Paco Peco, chico rico,
insultaba como un loco
a su tío Federico;
y éste dijo: Poco a poco,
Paco Peco, poco pico. Me han dicho que has dicho un dicho
que han dicho que he dicho yo,
el que lo ha dicho, mintió,
y en caso que hubiese dicho
ese dicho que tú has dicho
que han dicho que he dicho yo,
dicho y redicho quedó.
y estaría muy bien dicho,
siempre que yo hubiera dicho
ese dicho que tú has dicho
que han dicho que he dicho yo.

Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.
"""

def formatear(lista_lineas): 
    for linea in range(len(lista_lineas)):
        lista_lineas[linea] = lista_lineas[linea].strip('\n')

def mostrar(nombre_archivo):
    with open(nombre_archivo) as archivo:
        lista_lineas = archivo.readlines()
    formatear(lista_lineas)
    for linea in lista_lineas:
        print(linea)

def reemplazar(nombre_archivo):
    palabra = input('Qué palabra quiere cambiar?: ')
    reemplazo = input('Por cuál?: ')
    with open(nombre_archivo) as archivo:
        lista_lineas = archivo.readlines()
    for linea in range(len(lista_lineas)):
        if palabra in lista_lineas[linea]:
            lista_lineas[linea] = lista_lineas[linea].replace(palabra, reemplazo)
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(lista_lineas)

print('Texto original: ')
print('-----------------------------------------------------------')
mostrar('texto_guia6_ej4.txt')
print('-----------------------------------------------------------')
reemplazar('texto_guia6_ej4.txt')
print('Texto cambiado: ')
print('-----------------------------------------------------------')
mostrar('texto_guia6_ej4.txt')