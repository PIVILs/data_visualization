# Temperature chart for Dallas
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "data/dallas_weather_2021.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Чтение температур и дат из файла.
    dates, highs, lows = [], [], []
    for row in reader:
        high = int(row[3])
        highs.append(high)
        low = int(row[4])
        lows.append(low)
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig = plt.figure(dpi=128, figsize=(10, 6))
ax = fig.add_subplot(111)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.title("Daily high and low temperatures - 2021\nDallas, TX")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()