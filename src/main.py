from flask import Flask, render_template, url_for, jsonify
app = Flask(__name__)

# must be imported after app has been defined:
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
