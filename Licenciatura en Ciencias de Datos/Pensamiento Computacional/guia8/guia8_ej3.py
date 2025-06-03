import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)


#3. A continuación verá todos los países de los que poseemos información. Eligir uno que no sea nuestro país y luego, crear un nuevo DataFrame.
print(data["country"].unique())
print('_____________________________________________________________________________________\n')
# =========== Código de alumno ===============
country = 'Japan'
# ============================================
data_country = data[data["country"] == country]
print(data_country.head())
print('_____________________________________________________________________________________\n')



""" 
Realizar un gráfico de línea que muestre el PBI per cápita de los habitantes de Argentina (columna gdpPercap) a lo largo del tiempo y del país escogido anteriormente:
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos
● Linea sólida, espesor 2.2 y color "#30BFDE" para la curva de nuestro país.
● Linea sólida, espesor 2.2 y color "#1E92E3" para la curva del nuevo país.
● Referencias
● Grilla 
"""
data_arg = data[data["country"] == "Argentina"]

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(
    data_arg['year'], 
    data_arg['gdpPercap'], 
    label='Argentina',
    linestyle= '-',
    linewidth= 2.2,
    color='#30BFDE'
    )
ax.plot(
    data_country['year'], 
    data_country['gdpPercap'], 
    label={country},
    linestyle= '-',
    linewidth= 2.2,
    color='#1E92E3'
    )
ax.set_title(f'PBI per cápita de Argentina y {country} en el tiempo')
ax.set_xlabel('PBI per cápita en el País')
ax.set_ylabel('Expectativa de vida en el País')
ax.grid()
ax.legend()
plt.show()