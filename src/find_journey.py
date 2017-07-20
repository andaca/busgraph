from data_src import GRAPH, STOPS


def nearest_stops(lat, lon, max_n=1, max_dist=100):
    return ['a', 'b']


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
