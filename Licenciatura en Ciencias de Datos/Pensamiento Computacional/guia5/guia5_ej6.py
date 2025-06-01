""" 
6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente información de cada producto:
● Código del producto
● Fecha de vencimiento
● Si pasó el chequeo de calidad o no
Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la cantidad de elementos que quedaron en el diccionario.
Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué momento deberíamos crear la tupla?
"""

resultado_chequeo = [
    {'codigo':123, 'fecha_v':10, 'chequeo': True},
    {'codigo':313, 'fecha_v':10, 'chequeo': False},
    {'codigo':123123, 'fecha_v':10, 'chequeo': True},
    {'codigo':1231, 'fecha_v':10, 'chequeo': False},
    {'codigo':4353, 'fecha_v':10, 'chequeo': True},
    {'codigo':36534, 'fecha_v':10, 'chequeo': False},
    {'codigo':5645, 'fecha_v':10, 'chequeo': True},
    {'codigo':6345, 'fecha_v':10, 'chequeo': True},
    {'codigo':67832, 'fecha_v':10, 'chequeo': False}
]

def limpiar_chequeo(productos):
    #Eliminar productos que no pasaron el chequeo de calidad
    lista_eliminados = []
    lista_validos = []
    for producto in productos:
        if producto['chequeo']: 
            lista_validos.append(producto)
        else:
            lista_eliminados.append(producto)
            print('No pasó el chequeo: ', lista_eliminados[-1])

    productos.clear()
    productos.extend(lista_validos)
    tupla_eliminados = ( lista_eliminados, len(lista_validos))
    return tupla_eliminados

tupla_chequeo = limpiar_chequeo(resultado_chequeo)
eliminados, validos = tupla_chequeo

print('No pasaron el chequeo: ', eliminados)
print('Pasaron el chequeo: ', validos)
