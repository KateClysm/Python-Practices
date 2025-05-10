""" 
3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene la siguiente información:
● Nombre del producto
● Precio por unidad
● Cantidad
Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar 
"""


ticket = [
    {'nombre':'banana', 'precio': 10.5, 'cantidad': 1},
    {'nombre':'manzana', 'precio': 3, 'cantidad': 4},
    {'nombre':'arroz', 'precio': 10.7, 'cantidad': 3},
    {'nombre':'leche', 'precio': 5, 'cantidad': 1},
    {'nombre':'canela', 'precio': 1.50, 'cantidad': 1}
    ]

def monto_a_pagar(ticket):
    total = 0
    for producto in ticket:
        total += producto['precio'] * producto['cantidad']
        print('Nuevo Total: ', round(total, 2))
    return total

print('El total a pagar es de : ', round(monto_a_pagar(ticket), 2)) #redondea el valor numérico a 2 decimales
