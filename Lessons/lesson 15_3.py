import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа активна.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Назначение размера области просмотра.
    plt.figure(dpi=64, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values , linewidth=5)

    # Удаление осей.
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
