import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime

filename = 'data/MODIS_C6_1_Russia_Asia_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lats, lons, brights, hover_texts = [], [], [], []
    for row in reader:
        lat = float(row[0])
        lats.append(lat)
        lon = float(row[1])
        lons.append(lon)
        bright = float(row[10])
        brights.append(bright)
        hover_text = datetime.strptime(row[5], "%Y-%m-%d")
        hover_texts.append(hover_text)

data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'text': hover_texts,
    'marker': {
        'size': [0.025*bright for bright in brights],
        'color': brights,
        'colorscale': 'Reds',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='Active Fire Data')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='russia_asia_fire.html')