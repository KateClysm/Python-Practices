import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)

data['year'] = data['year'].astype("int")
data.info()

""" 
1. Elegir un año en el que desees ver la relación entre la expectativa de vida de los habitantes (columna `lifeExp`) y el PBI per cápita de los habitantes (columna gdpPercap). 
"""
# Modifica este valor
# =========== Código de alumno ===============
year = 2007
# ============================================
data_year = data[data["year"] == year] 

""" 
Realizar un gráfico de puntos que muestre la relación entre la expectativa de vida (columna lifeExp) y el PBI per cápita de los habitantes (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos
● Marcador de tipo triangular y color "#23A763"
● Grilla 
"""

fig, ax = plt.subplots()
# =========== Código de alumno ===============
ax.scatter(
    data_year['gdpPercap'],
    data_year['lifeExp'],
    color='#23A763',
    marker='^'
)
ax.set_xlabel('PBI per cápita')
ax.set_ylabel('Expectativa de vida')
ax.set_title(f'Relación entre PBI per cápita y Expectativa de Vida en {year}')
ax.grid(True)
# ============================================
plt.show()