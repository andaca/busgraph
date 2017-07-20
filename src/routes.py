import json

from main import app
from flask import jsonify, render_template, request

from data_src import LINES, STOPS

from find_journey import nearest_stops, fewest_changes_journey, parse_route


@app.route('/')
def index():
    return render_template('index.html', STOPS=STOPS)


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
                            max_n=5,
                            max_dist=500)

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

    print(fewest_changes)

    routes = [
        r for r in routes if len(r) == fewest_changes]

    print(routes)

    journeys = [list(parse_route(r)) for r in routes]
    print(journeys)
    return jsonify({
        'origins': origins,
        'destinations': destinations
    })
