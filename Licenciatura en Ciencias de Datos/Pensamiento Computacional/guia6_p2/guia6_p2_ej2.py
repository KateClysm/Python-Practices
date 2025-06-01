""" 
2. Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para calcular el producto entre dos números enteros ingresados. 
"""

def int_num(num):
    while type(num) is not int:  #Chequea por el tipo
        try:
            num = int(input('Ingrese un número entero: '))
        except ValueError:
            print('El número ingresado no es un entero.')
    return num

def producto(num1, num2):
    return num1 * num2

num1 = int_num(None) #Le paso a la función None, que como no es tipo int, entrará en el bucle while
num2 = int_num(None)
print(producto(num1, num2))


#-------------------------Mejor manera--------------------------------------------------------------------------------------------------------------
def ingresar_entero():
    while True:
        try:
            num = int(input('Ingrese un número entero: ')) #validación implícita, la conversión debe estar dentro del try para poder 'agarrar' los errores
        except ValueError:
            print('El valor contiene símbolos o letras, vuelva a intentarlo.')        
        else:
            return num
    
def producto(num1, num2):
    return num1 * num2

num1 = ingresar_entero()
num2 = ingresar_entero()
print(producto(num1, num2))