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


def formatear_csv_stock(lista_stock):
    linea_formateada = []
    for linea in range(len(lista_stock)):
        linea_formateada = lista_stock[linea].split(';')

        linea_formateada = {
            'nombre' : linea_formateada[0],
            'codigo' : int(linea_formateada[1]),
            'precio' : int(linea_formateada[2]),
            'stock': int(linea_formateada[3])
        }
        lista_stock[linea] = linea_formateada

def mostrar_stock(archivo_stock):
    with open('stock_libreria.csv') as archivo:
        stock = archivo.readlines()
    formatear_csv_stock(stock)
    for producto in range(len(stock)):
        print('Nombre producto: ', stock[producto]['nombre'])
        print('Código producto: ', stock[producto]['codigo'])
        print('Precio por unidad: ', stock[producto]['precio'])
        print('Stock: ', stock[producto]['stock'])

def agregar_producto(archivo_stock, producto):
    info = list(producto.values())
    for elemento in range(len(info)):
        info[elemento] = str(info[elemento])
    info = ';'.join(info)
    with open(archivo_stock, 'a') as archivo:
        archivo.write(f'\n{info}')
    
#---------------------------------------------------------------------------------------
print('__________________________________')
mostrar_stock('stock_libreria.csv')
producto_nuevo = {
    'nombre': 'hojas A4',
    'código': 35662,
    'precio': 600,
    'stock': 45
}
agregar_producto('stock_libreria.csv', producto_nuevo)
print('__________________________________')
mostrar_stock('stock_libreria.csv')
