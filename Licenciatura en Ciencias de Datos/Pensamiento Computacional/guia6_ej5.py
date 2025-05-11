""" 
5. Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
nombre;código;precio;stock
Un posible ejemplo de este archivo es el siguiente:
lapiceras;34512;50;120
cuadernos;41611;500;130
sacapuntas;62812;30;210
…
Se pide:
a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
Nombre producto: lapiceras
Código producto: 34512
Precio por unidad: 50
Stock: 120
Nombre producto: cuadernos
Código producto: 41611
Precio por unidad: 500
Stock: 130
…
b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue, es decir que si se recibe un diccionario del tipo:
{
“nombre”: “hojas A4”,
“código”: 35662,
“precio”: 600,
“stock”: 45
}
"""

#Devuelve una lista de diccionarios
def formatear_csv_stock(lista_lineas):
    lista = []
    for linea in lista_lineas:
        partes = linea.strip().split(';')
        producto = {
            'nombre': partes[0],
            'codigo': int(partes[1]),
            'precio': int(partes[2]),
            'stock': int(partes[3])
        }
        lista.append(producto)
    return lista

def mostrar_stock(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    lineas = formatear_csv_stock(lineas) #transforma la lista de strings a lista de dicts
    for producto in lineas:
        print('Nombre producto:', producto['nombre'])
        print('Código producto:', producto['codigo'])
        print('Precio por unidad:', producto['precio'])
        print('Stock:', producto['stock'])
    
def agregar_producto(nombre_archivo, producto):
    linea = f"\n{producto['nombre']};{producto['codigo']};{producto['precio']};{producto['stock']}"
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(linea)


#---------------------------------------------------------------------------------------
producto_nuevo = {
    'nombre': 'hojas A4',
    'codigo': 35662,
    'precio': 600,
    'stock': 45
}
print('__________________________________')
mostrar_stock('stock_libreria.csv')
agregar_producto('stock_libreria.csv', producto_nuevo)
print('__________________________________')
mostrar_stock('stock_libreria.csv')

