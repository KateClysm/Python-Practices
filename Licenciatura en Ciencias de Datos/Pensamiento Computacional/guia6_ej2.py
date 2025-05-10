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

def mostrar_personas(lista_personas, mensaje=None):
    if lista_personas:
        if mensaje: 
            print(mensaje)
            print('----------------------------------')
    for persona in lista_personas:
        print(persona)

def dinero_total(lista_personas):
    total = len(lista_personas) * 1000
    if 'Santi' in lista_personas:
        print('Santi está en la lista, agregando a Tomi a la lista... ')
        with open('regalo.txt', 'a') as archivo:
            archivo.write('\nTomi')
            lista_personas.append('Tomi') #Solución rápida para no tener que re-leer el archivo
        total += 1000
    return total


with open('regalo.txt') as archivo:
    contenido = archivo.readlines()  #Para leer todas las líneas y devolverlas como una lista de cadenas con \n
    
print("Antes de formatear: ", contenido)
        
for persona in range(len(contenido)):
    contenido[persona] = contenido[persona].strip('\n')  # Reasignamos la versión limpia

print("Después de formatear:", contenido)
print('----------------------------------')
#el método .strip('\n') devuelve una nueva cadena sin el salto de línea, pero no modifica la cadena original en la lista

mostrar_personas(contenido, 'Las personas que participarán son: ')
print('----------------------------------')

print('El dinero total que tiene Ale para el regalo de Sol es: ', dinero_total(contenido))
print('----------------------------------')

#Lista modificada agregando a Tomi:
mostrar_personas(contenido, 'Participantes: ')