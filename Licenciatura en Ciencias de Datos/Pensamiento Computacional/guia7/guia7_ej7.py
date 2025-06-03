import pandas as pd

peliculas = {'nombre': ['Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
                        'Casablanca', 'El exorcista',  'Soy leyenda',
                        'El club de la pelea', 'Mujercitas'],
            'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
                        'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
                        'William Friedkin', 'Francis Lawrence','David Fincher',
                        'Greta Gerwig'],
            'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
            'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
                        'ciencia ficción', 'drama', 'drama'],
            'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0]}

df = pd.DataFrame(peliculas)

# 7. Mostrar las películas que no hayan sido puntuadas (que el puntaje tenga un valor nulo).

print( df[ df['puntaje'].isnull() == True ]) 
print('_______________________________________________________________________________\n')
#Imprime un DataFrame reducido


print( df['nombre'][ df['puntaje'].isnull() == True ]) 
print('_______________________________________________________________________________\n')
#Imprime una Serie reducida