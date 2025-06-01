""" 
1. Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra?
b. Realizarlo utilizando try/ except. 
"""

# isnumeric() Devuelve True si todos los caracteres del string son números 
# El método .isdigit() verifica si todos los caracteres de una cadena (str) son dígitos, es decir, si representan números enteros positivos. Es más flexible que .isdecimal(), pero menos amplia que .isnumeric().
# El método .isdecimal() en Python se usa para verificar si todos los caracteres de una cadena son dígitos decimales (es decir, del 0 al 9, sin signos, puntos, fracciones, letras ni espacios). Devuelve un booleano

#1)a) 
#Chequea que sólo se ingresen enteros pero no verifica si se ingresa letras, tira error
num = input('Ingrese un número entero: ')
while not num.isnumeric():
    print('El número ingresado no es un entero')
    num = input('Intente otra vez: ')

#Chequea que se ingresen solo enteros
num = input('Ingrese un número entero: ')
while not num.isdigit():
    print('El número ingresado no es un entero')
    num = input('Intente otra vez: ')

#Chequea que se ingrese UN solo entero
num = input('Ingrese un número entero: ')
while not num.isdecimal():
    print('El número ingresado no es un entero')
    num = input('Intente otra vez: ')

#1)b)

num = None
while type(num) is not int:  #Chequea por el tipo
	try:
		num = int(input('Ingrese un número entero: '))
	except ValueError:
		print('El número ingresado no es un entero.')
            
#---------------------------------Mejor Manera------------------------------------------------------------------------------
      
def ingresar_entero():
    while True:
        try:
            num = int(input('Ingrese un número entero: ')) #validación implícita, la conversión debe estar dentro del try para poder 'agarrar' los errores
        except ValueError:
            print('El valor contiene símbolos o letras, vuelva a intentarlo.')        
        else: #Separa el código si no pasó ningún error en el try
            return num

num = ingresar_entero()