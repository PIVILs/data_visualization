import matplotlib.pyplot as plt
from die import Die

# Создание кубика D6.
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
x_values = list(range(1, 7))

fig, ax = plt.subplots()
ax.bar(x_values, frequencies, width=1, edgecolor="white", linewidth=0.7)
plt.show()



