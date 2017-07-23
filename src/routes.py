import json

from main import app
from flask import jsonify, render_template, request

from data_src import LINES, STOP_COORDS

from find_journey import nearest_stops, fewest_changes_journey, parse_route


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/line/<lineId>/<direction>')
def send_line(lineId, direction):
    lineId = lineId.lower()
    direction = direction.upper()
    key = '_'.join((lineId, direction))
    return jsonify(LINES[key])


@app.route('/getstops', methods=['POST'])
def get_stops():
    origin = request.json['origin']
    destination = request.json['destination']

    origins = nearest_stops(origin['lat'],
                            origin['lng'],
                            max_n=10,
                            max_dist=200)

    destinations = nearest_stops(destination['lat'],
                                 destination['lng'],
                                 max_n=5,
                                 max_dist=500)

    routes = []
    for origin in origins:
        for destination in destinations:
            routes.append(fewest_changes_journey(
                origin['id'], destination['id']))

    routes = [r for r in routes
              if not r is None and len(r) != 0]

    fewest_changes = 1000  # let's hope!
    for r in routes:
        if len(r) < fewest_changes:
            fewest_changes = len(r)

    # only use routes with the fewest number of changes
    # required
    routes = [
        r for r in routes if len(r) == fewest_changes]

    journeys = [list(parse_route(r)) for r in routes]

    # get coords of all stops
    # for j in journeys:
    #    for bus in j:
    #        bus['board_coords'] = STOP_COORDS[bus['board']]
    #        bus['deboard_coords'] = STOP_COORDS[bus['deboard']]

    print(journeys)

    stops = []
    for journey in journeys:
        for section in journey:
            board_coords = STOP_COORDS[section['board']]
            deboard_coords = STOP_COORDS[section['deboard']]

            # there can be > 1 bus options for the same
            # section
            for bus in section['busses']:
                stops.append({
                    'bus': bus,
                    'board': {
                        'id': section['board'],
                        'coords': board_coords
                    },
                    'deboard': {
                        'id': section['deboard'],
                        'coords': deboard_coords
                    }})

    print(stops)
    return jsonify(stops)
    # this is way too complicated to unpack with js
    # return jsonify(journeys)
