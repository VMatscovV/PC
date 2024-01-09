from flask import Flask, request, jsonify
import logging
import sys
from flask_cors import CORS
import json

from giga import getatt, getmarket
from kandinsky import logo

app = Flask(__name__)
cors = CORS(app, resources={r"/get-campaign-info": {"origins": "*"}})


@app.route('/')
def about():
    return 'The about page'


# основной метод в который будет ходить Миша
@app.route('/get-campaign-info', methods=['POST'])
def get_message():
    content = request.json
    print(content)
    logging.info(content)

    market = "виноделия"

    result = {"losung": getatt(market), "logo": logo(market), "tam": getmarket(market)}

    return jsonify(**result)


if __name__ == '__main__':

    app.debug = True
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    app.run(host='0.0.0.0', port=3000)


