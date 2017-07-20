import json
from os.path import dirname
import pickle

datadir = dirname(__file__) + '../../data/'

with open(datadir + 'stopcoords.json') as f:
    d = json.load(f)


coords_stops = {}
for stopId, coords in d.items():
    coords = (float(coords[0]), float(coords[1]))
    coords_stops[coords] = stopId

print(coords_stops)

with open(datadir + 'coord_stops.pkl', 'wb') as f:
    pickle.dump(coords_stops, f)

print('DONE')
