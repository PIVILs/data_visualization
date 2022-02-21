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
        try:
            high = int(row[3])
            low = int(row[4])
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig = plt.figure(dpi=128, figsize=(10, 6))
ax = fig.add_subplot(111)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures - 2021\nDallas, TX")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()