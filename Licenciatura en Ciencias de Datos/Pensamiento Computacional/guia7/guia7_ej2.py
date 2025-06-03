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

print(df)
print('_______________________________________________________________________________\n')



#2. Mostrar sólo los nombres de las primeras 3 películas del DataFrame.


print(df[0:3]['nombre']) # Acceso directo
print('_______________________________________________________________________________\n')

print(df.iloc[0:3, 0])    # con iloc (no incluye la pos 3, el final)
print('_______________________________________________________________________________\n')

print(df.loc[0:2, 'nombre'])     # con loc (incluye la pos final)
print('_______________________________________________________________________________\n')

""" 
- df[...] o df[...][...]: acceso directo, usa posición.
- iloc: posición numérica → [inicio:fin) (sin incluir fin).
- loc: índice real/etiqueta → [inicio:fin] (sí incluye fin). 
"""

#-------------------------Manera recomendada-----------------------------------------------

print(df.head(3)['nombre'])
print('_______________________________________________________________________________\n')


#Todas estas versionas imprimen una Serie de pandas