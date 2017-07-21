
from geopy.distance import distance
import networkx as nx

from data_src import ALL_STOPS_TREE, COORD_STOPS, GRAPH, LINES


def nearest_stops(lat, lon, max_n=1, max_dist=100):
    """
    @returns {'coords': tuple,
               'id': str,
               'dist: float}
    """
    global ALL_STOPS_TREE
    results = []

    _, indexes = ALL_STOPS_TREE.query((lat, lon), k=max_n)

    for idx in indexes:
        coords = ALL_STOPS_TREE.data[idx]
        coords = (float(coords[0]), float(coords[1]))

        d = distance((lat, lon), coords).meters

        if d <= max_dist:
            result = {
                'coords': coords,
                'id': COORD_STOPS[coords],
                'dist': round(d, 2)
            }
            results.append(result)

    return results


def fewest_changes_journey(origin_stop_id, destination_stop_id, max_changes=None):
    global GRAPH
    #changes = nx.dijkstra_path(GRAPH, origin_stop_id, destination_stop_id)
    changes = nx.shortest_path(GRAPH, origin_stop_id, destination_stop_id)

    if max_changes and len(changes) - 2 > max_changes:
        return []

    return changes


def parse_route(changes):
    """takes the graph and a list of nodes, yields a tuple of a node, and the
    edges that link it to the next node in the list.

    @params: changes (list)
    @yields: (str (lineId), str (stopId))

    TODO: THE EDGE MIGHT BE CHOSEN ARBITRARILY. WHAT IF THERE ARE > 1 EDGES BEWTEEN
    THE NODES? CAN WE GET ALL EDGES?
    """

    global GRAPH
    changes = iter(changes)
    prev_stop = next(changes)

    for next_stop in changes:

        # Sometimes there's more than only line (edge) for any given 2 nodes
        lines = []
        edges = GRAPH[prev_stop][next_stop]
        for edge in edges.values():
            lines.append(edge['line'])

        yield {
            'busses': lines,
            'board': prev_stop,
            'deboard': next_stop
        }

        prev_stop = next_stop


def find_journey(origin, destination, max_walk=500):
    """Takes two (lat, lon) coordinates, and finds the 
    easiest route between them.

    Max_walk is in meters

    "easiest" is characterised by the least number of 
    changes, followed by the walking required.
    """

    origin_stops = nearest_stops(*origin,
                                 n=10,
                                 max_dist=max_walk)

    destination_stops = nearest_stops(*destination,
                                      n=10,
                                      max_dist=max_walk)


def all_stops_between(lineId, first, last):
    global LINES
    stops = LINES[lineId]
    start_idx = stops.index(first)
    stop_idx = stops.index(last)

    return stops[start_idx:stop_idx]


if __name__ == '__main__':
    for s in STOPS:
        input(s)
