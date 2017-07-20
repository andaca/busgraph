from geopy.distance import distance

from data_src import ALL_STOPS_TREE, COORD_STOPS, GRAPH


def nearest_stops(lat, lon, max_n=1, max_dist=100):
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


def least_changes_line(origin_stop_id, desination_stop_id):
    pass


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


if __name__ == '__main__':
    for s in STOPS:
        input(s)
