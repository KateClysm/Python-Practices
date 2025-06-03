import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)

#5. Elegir un continente el cual te gustaría analizar con más detalle:
# =========== Código de alumno ===============
continent = 'Africa'
# ============================================
data_one_continent = data[data["continent"] == continent]
data_one_continent = data_one_continent[['country', 'gdpPercap']]
data_one_continent = data_one_continent.groupby(['country']).agg('sum') #utiliza los paises como índices de la columna gdpPercap
data_one_continent = data_one_continent.sort_values(by=['gdpPercap']) #ordena
data_one_continent[['gdpPercap']] #redundante, porque el DataFrame solo tiene una columna.
print(data_one_continent)
print('_____________________________________________________________________________________\n')

""" 
Realizar un gráfico de barras horizontales que muestre el PBI per cápita de los habitantes del continente escogido (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos en caso de ser necesario
● Nombre de los paises al lado de cada barra
● Grilla con líneas verticales únicamente, color "#CDD7DA" y línea discontinua. 
"""



fig, ax = plt.subplots()
# =========== Código de alumno ===============
data_one_continent = data_one_continent.reset_index()
ax.barh(
    data_one_continent['country'],
    data_one_continent['gdpPercap']
)
ax.set_ylabel('Países')
ax.set_xlabel('PBI per cápita')
ax.set_title(f'PBI per cápita de los habitantes de {continent}')
ax.grid(
    axis = 'x', 
    color = '#CDD7DA', 
    linestyle = 'dashed'
)

# ============================================
plt.show()
