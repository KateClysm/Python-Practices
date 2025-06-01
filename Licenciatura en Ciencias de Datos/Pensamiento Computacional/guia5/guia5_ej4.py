""" 
4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que vio.
Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7. 
"""

peliculas = [
    {'nombre': 'The Joker', 'anio': 2020, 'puntuacion': 10},
    {'nombre': 'Barbie', 'anio': 2023, 'puntuacion': 8},
    {'nombre': 'Only Lovers left Alive', 'anio': 2020, 'puntuacion': 10},
    {'nombre': 'Crimsom Peak', 'anio': 2002, 'puntuacion': 7},
    {'nombre': 'Coraline', 'anio': 2000, 'puntuacion': 5},
]

def mejores_peliculas(peliculas):
    nueva_lista= list(filter(lambda pelicula: pelicula['puntuacion'] > 7, peliculas))
    return nueva_lista

print(mejores_peliculas(peliculas))

for pelicula in mejores_peliculas(peliculas):
    print(pelicula)