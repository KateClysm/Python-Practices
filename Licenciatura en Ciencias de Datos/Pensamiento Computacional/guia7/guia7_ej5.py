""" 
5. Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la lista en esa ubicación.
a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango?
b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso contrario, mostrar un mensaje apropiado para dicho error. 
"""

def mostrar_valor (lista, indice):
    try:
        print(lista[indice])
    except IndexError:
        print('El índice provisto está fuera del rango de la lista')

lista = [1, 'a', ' 3', 5.0]
mostrar_valor(lista, 1)
mostrar_valor(lista, -1) #último elemento
mostrar_valor(lista, 7)