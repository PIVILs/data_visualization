import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
            edgecolors='none', s=40)

# Назначение заголовка диаграммы и меток осей.
plt.title("Cubes Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.axis([0, 5100, 0, 130000000000])

plt.show()