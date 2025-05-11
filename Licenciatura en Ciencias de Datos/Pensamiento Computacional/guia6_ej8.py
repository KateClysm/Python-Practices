"""
8. Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada respuesta en un .csv de la siguiente manera: nombre;color;le gusta, pero se dió cuenta que no es una forma muy práctica de guardarlo, así que lo quiere cambiar. Hacer un programa que lea el archivo y lo transforme en un archivo .txt. Es decir que si se tiene un archivo csv de la siguiente forma:

Agus;verde;si
Tomi; violeta;no
Manu;marrón;no

El archivo .txt tiene que quedar así:

A Agus sí le gusta el verde
A Tomi no le gusta el violeta
A Manu no le gusta el marrón 
"""

with open('colores.csv') as archivo_csv_colores:
    lineas = archivo_csv_colores.readlines()

for linea in lineas:
    datos = linea.strip().split(';')
    nombre = datos[0]
    color = datos[1]
    si_no = datos[2]
    with open('colores.txt', 'a') as archivo_txt_colores:
        archivo_txt_colores.write(f'A {nombre} {si_no} le gusta el {color}\n')

#Chequeo
with open('colores.txt') as archivo_txt_colores:
    lineas = archivo_txt_colores.readlines()
    for linea in lineas:
        print(linea.strip())