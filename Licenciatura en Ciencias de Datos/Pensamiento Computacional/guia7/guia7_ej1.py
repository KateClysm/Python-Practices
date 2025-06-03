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

df = pd.DataFrame(peliculas) #de la librería pd usamos el método DataFrame para convertir películas en un dataframe


""" 
1. Mostrar la información del DataFrame con el método info(), 
a) ¿Cómo se llaman y qué tipo de dato tiene cada columna? 
b) ¿Cuántos elementos nulos hay en cada columna? 
c) Interpretar qué información se guarda en esta tabla y para qué puede servir 
"""

print(df.info())

""" 
a)  La primer columna se llama '#' y contiene los índices de las columnas del dataframe, 
    que también sirven como los índices de las filas del df.info()
    La segunda columna se llama 'Column' y contiene los nombres de las columnas del dataframe.
    La tercer columna se llama 'Non-Null Count' y contiene todos los valores no nulos que se encuentran en la columna correspondiente en el data frame.
    La cuarta columna se llama 'DType' y contiene el tipo de dato de todos los inputs de esa columna correspondiente. 
        Si en la columna hay tipos diferentes entre sí, Dtype interpreta a los datos totales de la columna como 'object'

b)  En todas las columnas hay elementos no nulos excepto en 'puntaje' que hay 3 elementos nulos.

c)  En la tabla de df.info() se guarda información sobre la estructura del dataframe:
    *cantidad de columnas
    *nombres de columnas
    *valores no nulos de cada columna
    *tipo general de la columna
    *uso aproximado de memoria

    Esta información puede servir para:
    *Identificar si hay datos faltantes (valores nulos) en alguna columna.
    *Comprensión de estructura -> qué tipo de variables hay (numéricas, categóricas, texto, fechas).
    *Preparación para limpieza de datos: si hay valores None o NaN, saber en qué columnas están y poder decidir cómo tratarlos.
    *Optimización del rendimiento: conocer los tipos de datos ayuda a ajustar el uso de memoria si es necesario.
"""