from main import app
from flask import jsonify, render_template, request

from data_src import LINES, STOPS


@app.route('/')
def index():
    return render_template('index.html', STOPS=STOPS)


@app.route('/line/<lineId>/<direction>')
def send_line(lineId, direction):
    lineId = lineId.lower()
    direction = direction.upper()
    key = '_'.join((lineId, direction))
    return jsonify(LINES[key])


@app.route('/getjourney', methods=['POST'])
def get_journey():
    print(request.json)
    return jsonify({'st': 'OK'})
