""" 
2. En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta forma:
Agus
Manu
Santi
Lorena
Maria
La función tiene que devolver 5000
c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo de los nombres, se agregue también a Tomi. 
"""

def mostrar_personas(nombre_archivo, mensaje=None):

    with open(nombre_archivo) as archivo:
        contenido = archivo.readlines()
        for persona in range(len(contenido)):
            contenido[persona] = contenido[persona].strip('\n')  

    if mensaje: 
        print(mensaje)
        print('----------------------------------')

    for persona in contenido:
        print(persona)

def dinero_total(nombre_archivo):
    with open(nombre_archivo) as archivo:
        lista_personas = archivo.readlines()
    total = len(lista_personas) * 1000
    if 'Santi\n' in lista_personas:
        print('Santi está en la lista, agregando a Tomi a la lista... ')
        with open(nombre_archivo, 'a') as archivo:
            archivo.write('\nTomi')
        total += 1000
    return total


print('El dinero total que tiene Ale para el regalo de Sol es: ', dinero_total('regalo.txt'))
print('----------------------------------')

#Lista modificada agregando a Tomi:
mostrar_personas('regalo.txt', 'Participantes: ')