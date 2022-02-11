from random_walk import RandomWalk
import pygal

# Новые блуждания строятся до тех пор, пока программа активна.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(1000)
    rw.get_step()
    rw.fill_walk()
    break

coordinates_of_the_point = list(zip(rw.x_values, rw.y_values))

xy_chart = pygal.XY(stroke=True)
xy_chart.title = 'Random Walk'
xy_chart.add('Point',(coordinates_of_the_point))
xy_chart.render_to_file('rw_visual_pygal.svg')
