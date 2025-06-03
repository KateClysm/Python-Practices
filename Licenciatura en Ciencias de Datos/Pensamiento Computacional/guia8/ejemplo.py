import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4]
y = [2, 3, 5, 7]

# Crear gráfico
plt.plot(x, y)

# Mostrar gráfico
plt.title("Gráfico de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)

plt.show()