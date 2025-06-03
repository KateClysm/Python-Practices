import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)


#4. A continuación vamos a agrupar PBI per capita por continente.

data_continent = data[['continent', 'gdpPercap']]
print(data_continent)
print('_____________________________________________________________________________________\n')
data_continent = data_continent.groupby(['continent']).agg('sum')
#agrupa los datos por continente y suma todos los valores de gdpPercap de cada uno a lo largo de los años
print(data_continent)

""" 
Realizar un gráfico de torta la proporción del PBI per cápita de los habitantes de cada continente (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Cada parte con el nombre del continente y el porcentaje redondeado a las décimas.
● El color de cada parte será:
○ América: "#30BFDE"
○ Asia: "#E31E4B"
○ África: "#E36F1E"
○ Oceanía: "#1EE39B"
○ Europa: "#1E92E3" 
"""


fig, ax = plt.subplots()


# =========== Código de alumno ===============

print('_____________________________________________________________________________________\n')
data_continent = data_continent.reset_index()# Reinicia los índices para acceder al nombre del continente como columna
print(data_continent)
print('_____________________________________________________________________________________\n')
colors = {
    'Americas': "#30BFDE",
    'Asia': "#E31E4B",
    'Africa': "#E36F1E",
    'Oceania': "#1EE39B",
    'Europe': "#1E92E3"
}
#c_list = [colors[continent] for continent in data_continent['continent']]  #Lista por comprensión equivalente a:
c_list= []
for continent in data_continent['continent']:
    c_list.append(colors[continent])
print(c_list)
print('_____________________________________________________________________________________\n')
ax.pie(
        data_continent['gdpPercap'], 
        labels=data_continent['continent'],
        colors=c_list,
        autopct='%1.1f%%'
        )
ax.set_title('Proporción del PBI per cápita por continente')
# ============================================
plt.show()
