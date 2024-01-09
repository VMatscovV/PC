import requests
from flask import Flask, request, render_template, jsonify
import logging
import sys
from flask_cors import CORS, cross_origin
import json

from giga import getatt, getmarket
from kandinsky import logo

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def about():
    return 'The about page'


# основной метод в который будет ходить Миша
@app.route('/get-campaign-info', methods=['POST'])
@cross_origin()
def get_message():
    content = request.json
    print(content)
    logging.info(content)

    market = "Виноделия"

    result = {"Losung": getatt(market), "Logo": logo(market), "Tam": getmarket(market)}

    return jsonify(**result)


if __name__ == '__main__':

    app.debug = True
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    app.run(host='0.0.0.0', port=3000)


