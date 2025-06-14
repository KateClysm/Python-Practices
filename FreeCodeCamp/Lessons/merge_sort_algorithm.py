def merge_sort(array): #Divide el arreglo en mitades hasta que cada parte tenga 1 solo elemento, y luego las va uniendo ordenadamente.
    if len(array) <= 1: #caso base de la recursión. Es una condición que evita que la función siga llamándose a sí misma indefinidamente
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part) #Se vuelve a aplicar merge_sort a ambas mitades.
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part): #Se entra en un bucle mientras aún haya elementos en ambas partes.
        if left_part[left_array_index] < right_part[right_array_index]: #Compara el elemento actual de la izquierda y de la derecha.
            array[sorted_index] = left_part[left_array_index] #Si el de la izquierda es menor, lo copiamos al arreglo original.
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index] #Si el de la derecha es menor o igual, se copia al arreglo original.
            right_array_index += 1
        sorted_index += 1 #En ambos casos, avanzamos en el arreglo original para colocar el siguiente número ordenado.

		#Puede que uno de los dos arreglos aún tenga elementos no copiados. Por eso hay dos bucles más
    while left_array_index < len(left_part): #Esto copiará todos los elementos sobrantes de left_part al arreglo final (ya están ordenados).
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part): # Lo mismo, pero para right_part
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1
 
if __name__ == '__main__':  #Este bloque se ejecuta solo si el archivo se corre directamente, no si es importado desde otro módulo
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))