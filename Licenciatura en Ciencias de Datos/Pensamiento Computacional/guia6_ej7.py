""" 
7. En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula Por ejemplo si se tienen los siguientes archivos:
(salas.txt) (peliculas.txt)

D2 Megamente
F1 Rápidos y furiosos
E4 El padrino

El nuevo archivo deberá quedar:
(funciones.csv)
D2;Megamente
F1;Rápidos y furiosos
E4;El padrino 
"""

with open('salas.txt', 'r') as archivo_salas:
    salas = archivo_salas.readlines()

with open('peliculas.txt', 'r') as archivo_peliculas:
    peliculas = archivo_peliculas.readlines()

with open('funciones.csv', 'w') as archivo_funciones:
    for i in range(len(salas)):
        sala = salas[i].strip()
        pelicula = peliculas[i].strip()
        archivo_funciones.write(sala + ';' + pelicula + '\n')