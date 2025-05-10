""" 
7. Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
a. Crear el diccionario que represente esta situación.
AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las maratones? ¿Y qué tipo de dato es la maratón en sí?
b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una de forma ascendente.
"""

#Lista base de ejemplo
lista_maratonistas = [
    {'nombre': 'maria', 
     'dni': 1434243, 
     'maratones':[
            {'nombre': 'san carlos ol', 'anio': 2000, 'puesto': 3, 'tiempo': 1.30},
            {'nombre': 'new york', 'anio': 2010, 'puesto': 2, 'tiempo': 3.30},
            {'nombre': 'Japon', 'anio': 2015, 'puesto': 1, 'tiempo': 1},
            {'nombre': 'Argentina', 'anio': 2003, 'puesto': 2, 'tiempo': 3}
        ]
    },
    {'nombre': 'Carlos', 
     'dni': 2938474, 
     'maratones':[
            {'nombre': 'san carlos ol', 'anio': 2000, 'puesto': 2, 'tiempo': 1},
            {'nombre': 'new york', 'anio': 2010, 'puesto': 1, 'tiempo': 1.30},
            {'nombre': 'Japon', 'anio': 2015, 'puesto': 2, 'tiempo': 3},
            {'nombre': 'Argentina', 'anio': 2003, 'puesto': 3, 'tiempo': 3.30}
        ]
    },
    {'nombre': 'Carla', 
     'dni': 8492342, 
     'maratones':[
            {'nombre': 'san carlos ol', 'anio': 2000, 'puesto': 1, 'tiempo': 0.50},
            {'nombre': 'new york', 'anio': 2010, 'puesto': 3, 'tiempo': 4.30},
            {'nombre': 'Japon', 'anio': 2015, 'puesto': 3, 'tiempo': 4},
            {'nombre': 'Argentina', 'anio': 2003, 'puesto': 1, 'tiempo': 2.30}
        ]
    },
]

#Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
def ingresar_maratonistas(lista_m):
    
    while input('¿Desea ingresar un maratonista? (0 para salir): ') != '0':
        nombre = input('Nombre: ')
        dni = int(input('DNI: '))
        maratones = []
        while input('¿Desea cargar una maratón? (0 para salir): ') != '0':
            nombre_maraton = input('Nombre de la maratón: ')
            anio = int(input('Año: '))
            puesto = int(input('Puesto: '))
            tiempo = float(input('Tiempo (en horas): '))
            maratones.append({'nombre': nombre_maraton, 'anio': anio, 'puesto': puesto, 'tiempo': tiempo})
        lista_m.append({'nombre': nombre, 'dni': dni, 'maratones': maratones})

# b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
def ordenar_maratonistas(lista_m):
    print('Ordenando Maratonistas alfabéticamente...')
    lista_m.sort(key=lambda maratonista: maratonista['nombre'].lower())
    
# c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una de forma ascendente.
def ordenar_maratones(lista_m):
    print('Ordenando Los maratones de los maratonistas en forma ascendente...')
    for maratonista in lista_m:
        maratonista['maratones'].sort(key=lambda maraton: maraton['tiempo'])

def mostrar_maratonistas(lista_m):
    for maratonista in lista_m:
        print(f"\nNombre: {maratonista['nombre']}")
        print(f"DNI: {maratonista['dni']}")
        print("Maratones:")
        for maraton in maratonista['maratones']:
            print(f"  * Maraton: {maraton['nombre']} Anio: ({maraton['anio']}), Puesto: {maraton['puesto']}, Tiempo: {maraton['tiempo']} hs")


#PROGRAMA PRINCIPAL

print('Lista sin alterar: ')
mostrar_maratonistas(lista_maratonistas)

print()
ingresar_maratonistas(lista_maratonistas)

print()
print('Lista alterada: ')
mostrar_maratonistas(lista_maratonistas)

print()
if input('¿Desea ordenar alfabeticamente los maratonistas? (0 para salir): ') != '0':
    ordenar_maratonistas(lista_maratonistas)
    mostrar_maratonistas(lista_maratonistas)

print()
if input('¿Desea ordenar los maratones de los maratonistas? (0 para salir): ') != '0':
    ordenar_maratones(lista_maratonistas)
    mostrar_maratonistas(lista_maratonistas)
