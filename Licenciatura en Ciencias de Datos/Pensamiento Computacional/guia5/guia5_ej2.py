""" 
2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue esa planta a la lista de diccionarios. 
"""

def agregar_planta(lista_de_plantas, planta):
    lista_de_plantas.append({'especie': planta['especie'], 'luz_solar': planta['luz_solar'], 'precio': planta['precio']})

plantas = []
print(plantas)

si = input('Quiere agregar una nueva planta? ingrese cualquier tecla. Aprete 0 para salir:  ')
while si != '0':
    especie = input('De qué especie es la planta?:  ')
    luz_solar = input('Necesita luz solar? True/False:  ')
    while luz_solar not in ['True', 'False']:
        luz_solar = input('necesita luz solar? True/False:  ')
    if luz_solar == 'True': 
        luz_solar = True 
    else: 
        luz_solar = False
    
    while True:
        try:
            precio = float(input('Cuál es el precio?:  ').replace(',', '.'))
            break
        except ValueError:
            print("Usar punto para decimales")


    planta = {'especie': especie, 'luz_solar': luz_solar, 'precio': precio}

    agregar_planta(plantas, planta)
    si = input('Quiere agregar una nueva planta? aprete cualquier tecla. Aprete 0 para salir:  ')

print(plantas)

for planta in plantas:
    print(planta)