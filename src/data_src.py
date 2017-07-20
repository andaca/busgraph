import json
import pickle

with open('../data/stops.pkl', 'rb') as f:
    STOPS = pickle.load(f)

with open('../data/buslines.json') as f:
    LINES = json.load(f)

with open('../data/graph.pkl', 'rb') as f:
    GRAPH = pickle.load(f)
