import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

""" 
Ejercicios de Grillas
Para estos ejercicios, vamos a crear valores aleatorios, que serán contenidos en un
DataFrame que llamaremos df: 
"""


np.random.seed(0) #usa siempre los mismos números aleatorios  para que cada vez que se corra el código de los mismos resultados
df = pd.DataFrame(
    data={
        'a':np.random.randint(0, 100, 50),
        'b':np.random.randint(0, 100, 50),
        'c':np.random.randint(0, 100, 50),
        'd':np.random.randint(0, 100, 50)
    }
)
#Se crea una tabla de 4 columnas. Cada columna tiene 50 números al azar, del 0 al 99.
print(df.head())
print('_____________________________________________________________________________________\n')
print(df)
print('_____________________________________________________________________________________\n')
""" 
6. Crear una grilla de 4 gráficos de línea, en la que los ejes x va a contener los valores del índice df.index.values, mientras que los ejes y, los valores de las columnas a, b, c y d.
La figura debe tener:
● 2 filas y 2 columas
● Tamaño de figura de una altura de 8 y un ancho de 15.
● Nombre de los ejes y referencia en cada gráfico
● Grilla
● La siguiente posición de gráficos:
○ Los valores A en la parte superior izquierda, color green
○ Los valores B en la parte superior derecha, color red
○ Los valores C en la parte inferior izquierda, color magenta
○ Los valores D en la parte inferior derecha, color blue 
"""


# =========== Código de alumno ===============
def create_easy_graph(x, y, label, ax, xlabel='Índice', ylabel='Valor', title='', color="#909090"):
    ax.plot(x, y, label=label, color=color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 8)) #fig -> figura completa que puede contener varios gráficos, ax -> un gráfico individual
x = df.index.values
columnas = ['a', 'b', 'c', 'd']
titulos = ['Valores A', 'Valores B', 'Valores C', 'Valores D']
colores = { "#15AB42","#CD0707","#9D0490","#004EEB" }
ejes = [axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1]]

for col, title, color, ax in zip(columnas, titulos, colores, ejes):
    create_easy_graph(x, df[col], col.upper(), ax, 'Índice', 'Valor', title, color)

# x contiene números desde 0 a 49
#ej de df[col] -> df['a']
#col.upper() es la label del gráfico individual, toma el valor de col y lo pone en Mayúsculas
#ax tomo el valor de ejes, por ejemplo axs[0,0] en la primera iteración.
#color toma un color distinto en cada iteración

plt.tight_layout()
plt.show()
# ============================================