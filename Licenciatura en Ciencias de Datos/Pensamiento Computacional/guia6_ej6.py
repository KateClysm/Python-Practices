""" 
6. Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni y la nota que sacó.
a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados notas.csv
b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la cantidad de alumnos aprobados (su nota es mayor a 4).
"""

notas = [
    {'nombre': 'maria', 'apellido': 'garce', 'dni': 12312244, 'nota': 1},
    {'nombre': 'marcos', 'apellido': 'garcia', 'dni': 41341234, 'nota': 2},
    {'nombre': 'mara', 'apellido': 'galiano', 'dni': 44463454, 'nota': 3},
    {'nombre': 'mauricio', 'apellido': 'perez', 'dni': 2341244, 'nota': 4},
    {'nombre': 'malena', 'apellido': 'robles', 'dni': 46564566, 'nota': 5},
    {'nombre': 'manila', 'apellido': 'fernandez', 'dni': 76567575, 'nota': 6},
    {'nombre': 'marta', 'apellido': 'perez', 'dni': 32414124, 'nota': 7},
    {'nombre': 'martin', 'apellido': 'pugh', 'dni': 18273923, 'nota': 8},
    {'nombre': 'mateo', 'apellido': 'morales', 'dni': 19238290, 'nota': 9},
    {'nombre': 'mauro', 'apellido': 'nunies', 'dni': 21028019, 'nota': 10}
    ]


def guardar_notas(parciales):
    with open('parciales.csv', 'w') as archivo:
        for parcial in parciales:
            fila = ';'.join(str(valor) for valor in parcial.values()) #generator expression, devuelve una string
            archivo.write(fila + '\n') 

def cantidad_aprobados(parciales):
    with open(parciales, 'r') as archivo:
        lineas = archivo.readlines()

    aprobados = 0
    for linea in lineas:
        datos = linea.strip().split(';')
        nota = int(datos[-1])
        if nota > 4:
            aprobados += 1
    return aprobados

guardar_notas(notas)
print(f'Cantidad aprobados: {cantidad_aprobados('parciales.csv')}')



#-----------Ejemplo sin usar Generator Expressions & .values()
def guardar_notas2(parciales):
    with open('parciales.csv', 'w') as archivo:
        for parcial in parciales:
            fila = [
                str(parcial['nombre']),
                str(parcial['apellido']),
                str(parcial['dni']),
                str(parcial['nota'])
            ]
            linea = ';'.join(fila)
            archivo.write(linea + '\n')

def cantidad_aprobados2(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    aprobados = 0
    for linea in lineas:
        datos = linea.strip().split(';')
        nota = int(datos[3]) 
        if nota > 4:
            aprobados += 1
    return aprobados

# guardar_notas2(notas)
# print(f'Cantidad aprobados: {cantidad_aprobados2("parciales.csv")}')