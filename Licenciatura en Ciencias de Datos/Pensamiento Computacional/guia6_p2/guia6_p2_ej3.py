""" 
3. Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el cociente entre ellos.
AYUDA: Considerar que el usuario podría brindar un valor no numérico o un divisor nulo. 
"""

def ingresar_float():
    while True:
        try:
            num = float(input('Ingrese cualquier número(positivo, negativo, decimal, entero): '))
        except ValueError:
            print('El número ingresado no es válido.')
        else:
            return num


def cociente(dividendo, divisor):
    try:
        cociente = dividendo / divisor
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    else: #si no hubo error
        print("El cociente es:", cociente)

dividendo = ingresar_float()
divisor = ingresar_float()
print(cociente(dividendo, divisor))