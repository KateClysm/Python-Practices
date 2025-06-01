""" 
6. Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos, tres o cuatro. Crear una función que pida al usuario informar el número de jugadores, considerando que este puede ingresar:
● un valor no válido, por ejemplo, una palabra.
● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
● un valor mayor a 4, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 4 jugadores."
● un valor válido, en cuyo caso, mostrarlo.
"""

def ingresar_entero():
    while True:
        try:
            num = int(input('Ingrese un número entero: ')) 
        except ValueError:
            print('El valor contiene símbolos o letras, vuelva a intentarlo.')        
        else: 
            return num



def jugadores():
    while True:
        print('¿Cuántos van a jugar?: ')
        personas = ingresar_entero()
        if personas < 2:
            print("Debe haber al menos 2 jugadores.")
        elif personas > 4:
            print("Se puede jugar con un máximo de 4 jugadores.")
        else:
            print(f"{personas} Es una cantidad de jugadores válida")
            break
jugadores()