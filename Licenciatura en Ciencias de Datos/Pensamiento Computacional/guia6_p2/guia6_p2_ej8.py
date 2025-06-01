""" 
8. El kiosko de la facultad quiere automatizar un letrero que tome datos de un programa y le cobre al estudiante.
Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada producto.
Ejemplo:
opciones = {
1: "hamburguesas",
2: "milanesas",
3: "gaseosa",
4: "alfajor",
5: "papas fritas",
6: "agua"
}
valores = {
1:1000,
2:1500,
3:500,
4:300,
5:600,
6:350
}
Se quiere hacer un programa que muestre la información de la siguiente forma en la pantalla:
1: hamburguesas -> 1000
2: milanesas -> 1500
3: gaseosa -> 500
4: alfajor -> 300
5: papas fritas -> 600
6: agua -> 350
Y le pida al usuario una opción y una cantidad. Luego, debe imprimir el total a pagar.
Se debe considerar que el usuario podría ingresar una opción que no está en el diccionario, o ingresar una opción que no sea un número. El usuario debe en esos casos imprimir un mensaje de error que sea descriptivo y volver a pedirle al usuario que ingrese una opción.
"""

opciones = {
    1: "hamburguesas",
    2: "milanesas",
    3: "gaseosa",
    4: "alfajor",
    5: "papas fritas",
    6: "agua"
}
valores = {
    1:1000,
    2:1500,
    3:500,
    4:300,
    5:600,
    6:350
}

def ingresar_entero():
    while True:
        try:
            num = int(input('Ingrese un número entero: '))
        except ValueError:
            print('El valor ingresado contiene símbolos o letras.')
        else:
            return num
    
def mostrar_letrero(opciones, valores):
    for codigo in opciones:
        print(f"{codigo}: {opciones[codigo]} -> {valores[codigo]}")

def elegir_comida(precios):
    while True:
        print('¿Qué opción del menú desea?: ')
        eleccion = ingresar_entero()
        try:
            precio = precios[eleccion]
            break
        except KeyError:
            print("Debe elegir un número que corresponda a una comida del menú.")
    print('¿Cuántos desea?: ')
    cantidad = ingresar_entero()
    print('Total a pagar: ', cantidad * precio)
        
mostrar_letrero(opciones, valores)
elegir_comida(valores)

#El ejercicio se puede resolver sin un KeyError pero a modo de práctica lo implementé