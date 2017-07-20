import json
from os.path import dirname
import pickle

from scipy.spatial import cKDTree

datadir = dirname(__file__) + '../../data/'

with open(datadir + 'stopcoords.json', 'rt') as f:
    stops = json.load(f)

points = []
for _, coords in stops.items():
    points.append(tuple(float(c) for c in coords))

tree = cKDTree(points)

with open(datadir + 'all_stops_tree.pkl', 'wb') as f:
    pickle.dump(tree, f)

print(tree)
print('DONE')
