import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа активна.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(50000)
    rw.get_step()
    rw.fill_walk()

    # Назначение размера области просмотра.
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors= 'none', s=1)

    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)

    # Удаление осей.
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
