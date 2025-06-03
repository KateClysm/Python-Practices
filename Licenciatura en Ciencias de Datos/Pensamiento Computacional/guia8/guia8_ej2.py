import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)
 
#2. Creamos un nuevo DataFrame con la información de la Argentina únicamente.
data_arg = data[data["country"] == "Argentina"]
data_arg.head()

"""
Realizar un gráfico de línea que muestre el PBI per cápita de los habitantes de Argentina (columna gdpPercap) a lo largo del tiempo:
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos
● Linea sólida, espesor 2.2 y color "#30BFDE"
● Grilla 
"""

# =========== Código de alumno ===============
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(
    data_arg['year'],
    data_arg['gdpPercap'],
    linestyle= '-',
    linewidth= 2.2,
    color='#30BFDE',
    )
ax.set_title(f'Relación entre PBI per cápita y Expectativa de Vida de Argentina a lo largo del tiempo')
ax.set_xlabel('PBI per cápita - Argentina')
ax.set_ylabel('Expectativa de vida - Argentina')

# ============================================
plt.show()
