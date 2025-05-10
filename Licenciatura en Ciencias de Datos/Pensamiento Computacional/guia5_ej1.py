"""
    1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener mejor organizados sus datos.
    a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las características que se consideren más relevantes para identificar a una persona (su nombre, DNI, edad, etc).
    b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso del estudiante y sus características (año, división, orientación, etc).
    c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad e imprimirla por pantalla. 
"""

alumno1 = {'nombre': 'Carlos Sanchez', 'DNI': '12345678', 'edad': 15}
print(alumno1)
alumno1.update({'curso': {'anio':2010, 'division':'2A', 'orientacion':'comunicacion'}})
print(alumno1)

#{'anio': '', 'division': '', 'orientacion': ''}
lista_estudiantes = [
    {'nombre': 'Carlos Sanchez', 'DNI': '12345678', 'edad': 15},
    {'nombre': 'Clara Prez', 'DNI': '12324455', 'edad': 18},
    {'nombre': 'Maria Lu', 'DNI': '43245678', 'edad': 13},
    {'nombre': 'Lara Rodriguez', 'DNI': '11234578', 'edad': 12}
    ]

print(lista_estudiantes)

# print(max(map(lambda alumno: alumno['edad'])))  map genera un iterable con solo las edades de cada estudiante, max obtiene la edad máxima
print(max(lista_estudiantes, key=lambda alumno: alumno['edad']))