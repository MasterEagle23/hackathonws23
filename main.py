from logic.strategy import decide
from models.table import Table
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def identify():
    return 'Poker Python Player'


@app.route('/', methods=['POST'])
def bet():
    return jsonify({'bet': int(decide(request.json))})
