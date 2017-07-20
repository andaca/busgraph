import json

from main import app
from flask import jsonify, render_template, request

from data_src import LINES, STOPS

from find_journey import nearest_stops


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
    return jsonify({
        'origins': origins,
        'destinations': destinations
    })
