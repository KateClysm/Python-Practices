# {} dictionary
# [] list 
# () tuple -> inmutable

#dictionary of nodes and their connected nodes with their respective distances
my_graph = { 
    # 'key' : [(node, distance),...] 
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):

    unvisited = list(graph) #['A', 'B', 'C', 'D', 'E', 'F']
    distances = {node: 0 if node == start else float('inf') for node in graph}
    """
    En la primera iteración:
    {
    'A': 0,
    'B': float('inf'),
    'C': float('inf'),
    'D': float('inf'),
    'E': float('inf'),
    'F': float('inf')
    } 
    """
    shortest_paths = {node: [] for node in graph}
    """     
    Lista vacía pensada para almacenar la secuencia de nodos visitados para llegar a cada nodo desde el nodo de inicio (start).
    {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': []
    } 
    """
    shortest_paths[start].append(start)
    """     
    shortest_paths = {
        'A': ['A'],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': []
    } 
    """
    #mientras hayan nodos por visitar
    while unvisited:
        current = min(unvisited, key=distances.get)
        #current es el nodo que tiene la distancia mínima, no el valor de la distancia en sí.
        #key=distances.get le dice a la función min() que, en lugar de comparar los elementos de unvisited directamente, compare los valores asociados en el diccionario distances para cada nodo de unvisited.
        #El valor de current será 'A' (porque su distancia es 0, la mínima en distances).
        for node, distance in graph[current]:
            #graph[current] devuelve  [('B', 5), ('C', 3), ('E', 11)] siendo el primer elemento el nodo y el segundo la distancia
            #Se compara si la nueva distancia calculada al nodo vecino es menor que la registrada en distances.
            if distance + distances[current] < distances[node]:
                #para B 5 + 0 < inf   # ✅ Se actualiza
                #para C 3 + 0 < inf   # ✅ Se actualiza
                #para E 11 + 0 < inf  # ✅ Se actualiza
                distances[node] = distance + distances[current] #Se actualizan los valores en distances
                #distances = {'A': 0, 'B': 5, 'C': 3, 'D': inf, 'E': 11, 'F': inf}
                if shortest_paths[node] and shortest_paths[node][-1] == node:
                    # Comprueba si la lista shortest_paths[node] no está vacía.
                    # Si la lista está vacía, significa que el nodo aún no tiene un camino registrado.
                    # En Python, una lista vacía ([]) es considerada falsa en una condición if.
                    # shortest_paths[node][-1] obtiene el último elemento de la lista.
                    # Se verifica si el último nodo en la ruta ya es el nodo actual (node).
                    # Esto se usa para evitar agregar duplicados en la lista de caminos más cortos.
                    # Si el nodo ya está correctamente registrado en su propia ruta, se sobreescribe con la ruta del nodo actual (current).
                    # Si no, simplemente se extiende la lista.
                    shortest_paths[node] = shortest_paths[current][:]
                else:
                    shortest_paths[node].extend(shortest_paths[current])
                shortest_paths[node].append(node) #Se añade el nodo visitado a la ruta.
        unvisited.remove(current) # Se elimina A de unvisited  unvisited = ['B', 'C', 'D', 'E', 'F']
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(shortest_paths[node])}')
    
    return distances, shortest_paths
    
shortest_path(my_graph, 'A', 'F')