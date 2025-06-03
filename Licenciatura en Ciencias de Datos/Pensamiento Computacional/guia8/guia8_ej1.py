import matplotlib.pyplot as plt
import pandas as pd

""" 
Ejercicios de Tipos de Gráfico
Para realizar estos ejercicio, debemos importar la información del PBI per cápita de los distintos países, a lo largo de un período que abarca desde 1952 y 2007. 
PBI es un indicador económico que mide:
"El valor total de los bienes y servicios producidos por un país en un año, dividido por su población total."
"""

# Importo la información

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url) #Descarga y lee el archivo CSV, convirtiéndolo en un DataFrame


# Modificar el tipo de dato:

data['year'] = data['year'].astype("int")
#filtra las filas del DataFrame data para quedarte solo con las que tienen year == 2007, pero no elimina la columna year, porque sigue siendo parte de la estructura del DataFrame.

print('_____________________________________________________________________________________\n')
print(data.head())
print('_____________________________________________________________________________________\n')
data.info()
print('_____________________________________________________________________________________\n')


""" 
1. Elegir un año en el que desees ver la relación entre la expectativa de vida de los habitantes (columna `lifeExp`) y el PBI per cápita de los habitantes (columna gdpPercap). 
"""


# Modifica este valor
# =========== Código de alumno ===============
year = 2007
# ============================================

data_year = data[data["year"] == year] 
#filtra las filas de data para quedarte solo con los países en el año 2007
print(data_year)
print('_____________________________________________________________________________________\n')
print(data_year.head())



""" 
Realizar un gráfico de puntos que muestre la relación entre la expectativa de vida (columna lifeExp) y el PBI per cápita de los habitantes (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos
● Marcador de tipo triangular y color "#23A763"
● Grilla 
"""


fig, ax = plt.subplots() #Crea una figura (fig) y un eje (ax)

# =========== Código de alumno ===============

ax.scatter(
    data_year['gdpPercap'], # Eje X:
    data_year['lifeExp'], # Eje Y:
    color='#23A763',
    marker='^'
)

ax.set_xlabel('PBI per cápita')
ax.set_ylabel('Expectativa de vida')
ax.set_title(f'Relación entre PBI per cápita y Expectativa de Vida en {year}')
ax.grid(True)  # Mostrar grilla

# ============================================
plt.show()