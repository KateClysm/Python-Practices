""" 
5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda la siguiente información:
● Nombre
● Apellido
● Intento
● Nota
Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el primer recuperatorio y 3 si es el segundo recuperatorio.
Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la primera oportunidad que rindieron los alumnos.
¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no solamente sirve para el intento 1, sino que también pueda servir para los demás. 
"""


info_primer_parcial = [
    {'Nombre': 'Laura', 'Apellido': 'Perez', 'Intento': 1, 'Nota': 10},
    {'Nombre': 'Marcos', 'Apellido': 'Bustamante', 'Intento': 1, 'Nota': 10},
    {'Nombre': 'Luna', 'Apellido': 'Garcia', 'Intento': 2, 'Nota': 5},
    {'Nombre': 'Maria', 'Apellido': 'Martinez', 'Intento': 1, 'Nota': 10},
    {'Nombre': 'Claudia', 'Apellido': 'Robles', 'Intento': 2, 'Nota': 5},
    {'Nombre': 'Romina', 'Apellido': 'Donetto', 'Intento': 1, 'Nota': 10},
    {'Nombre': 'Cesi', 'Apellido': 'Salari', 'Intento': 1, 'Nota': 10},
    {'Nombre': 'Mariela', 'Apellido': 'Soliz', 'Intento': 2, 'Nota': 5}
]

def promedio_notas(info, intento):
    parciales = 0
    notas = 0
    for persona in info:
        if persona['Intento'] == intento:
            notas += persona['Nota']
            parciales += 1
    return notas / parciales

print('El promedio de las notas del primer intento fue: ', round((promedio_notas(info_primer_parcial, 1)),2)  )

print('El promedio de las notas del segundo intento fue: ', round((promedio_notas(info_primer_parcial, 2)),2)  )