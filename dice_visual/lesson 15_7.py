#Results of rolling a D8 and a D8 15,000,000 times.

from die import Die
import pygal

# Создание двух кубиков D8 и D8.
die_1 = Die(8)
die_2 = Die(8)

# Моделироваение бросков с сохранением результатов в списке.
results = []
for roll_num in range(15000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling a D8 and a D8 15,000,000 times."
hist.x_labels = [x_label for x_label in range(min(results), max(results)+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual_D8D8.svg')