""" 
7. Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos, cuatro o seis. Crear una función que pida al usuario informar el número de jugadores, considerando que este puede ingresar:
● un valor no válido, por ejemplo, una palabra.
● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
● un valor mayor a 6, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 6 jugadores.".
● un valor impar, como 3 y 5, en cuyo caso, mostrar el mensaje "Debe haber un número par de jugadores.".
● un valor válido, en cuyo caso, mostrarlo.
"""

def ingresar_entero():
    while True:
        try:
            num = int(input('Ingrese un número entero: '))
        except ValueError:
            print('El valor ingresado contiene símbolos o letras.')
        else:
            return num

def jugar_truco():
    while True:
        print('¿Cuántos van a jugar al truco?')
        personas = ingresar_entero()
        #Como no son errores de tipo, los podemos abordar con advertencias y reiniciar el loop
        if personas < 2:
            print("Debe haber al menos 2 jugadores.")
        elif personas > 6:
            print("Se puede jugar con un máximo de 6 jugadores.")
        elif (personas % 2) != 0:
            print("Debe haber un número par de jugadores.")
        else:
            print(f"{personas} es una cantidad de jugadores válida!")
            break
jugar_truco()