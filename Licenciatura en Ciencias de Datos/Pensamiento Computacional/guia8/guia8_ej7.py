import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


np.random.seed(0) 
df = pd.DataFrame(
    data={
        'a':np.random.randint(0, 100, 50),
        'b':np.random.randint(0, 100, 50),
        'c':np.random.randint(0, 100, 50),
        'd':np.random.randint(0, 100, 50)
    }
)
print(df.head())
print('_____________________________________________________________________________________\n')


""" 
7. Crear una grilla de 2 gráficos: uno de línea y otro de puntos, siendo los ejes x los valores del índice df.index.values, mientras que los ejes y, los valores de las columnas a, b, c y d.
La figura debe tener:
● 2 filas y 1 columna
● Tamaño de figura de una altura de 8 y un ancho de 15.
● Título de cada gráfico
● Referencias
● Grilla
● La siguiente posición de gráficos:
○ Los valores A Y B en la parte superior, en un gráfico de línea, color green y red, tipo de línea sólida y discontinua respectivamente.
○ Los valores C Y D en la parte inferior, en un gráfico de puntos, color magenta y blue, marcador circular y triángulo invertido respectivamente.
"""


# =========== Código de alumno ===============
def create_easy_graph(x, y, label, ax, xlabel='Índice', ylabel='Valor', title='', color="#909090", tipo='linea', estilo='-', marcador='o'):
    if tipo == 'linea':
        ax.plot(x, y, label=label, color=color, linestyle=estilo)
    elif tipo == 'puntos':
        ax.scatter(x, y, label=label, color=color, marker=marcador)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 8)) #fig -> figura completa que puede contener varios gráficos, ax -> un gráfico individual
x = df.index.values

create_easy_graph(x, df['a'], 'A', axs[0], title='Valores A y B (líneas)', color="#04C43E", tipo='linea', estilo='-')
create_easy_graph(x, df['b'], 'B', axs[0], color="#E60A0A", tipo='linea', estilo='--')

# Gráfico de puntos (abajo)
create_easy_graph(x, df['c'], 'C', axs[1], title='Valores C y D (puntos)', color="#C904B9", tipo='puntos', marcador='o')
create_easy_graph(x, df['d'], 'D', axs[1], color="#1F67F6", tipo='puntos', marcador='v')

plt.tight_layout()
plt.show()

# ============================================