import json
from os.path import dirname
import pickle

datadir = dirname(__file__) + '/../data/'

with open(datadir + 'stops.pkl', 'rb') as f:
    STOPS = pickle.load(f)

with open(datadir + 'buslines.json') as f:
    LINES = json.load(f)

with open(datadir + 'graph.pkl', 'rb') as f:
    GRAPH = pickle.load(f)

with open(datadir + 'all_stops_tree.pkl', 'rb') as f:
    ALL_STOPS_TREE = pickle.load(f)

with open(datadir + 'coord_stops.pkl', 'rb') as f:
    COORD_STOPS = pickle.load(f)
