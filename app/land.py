from models.giga import getatt, getmarket
from models.kandinsky import logo
from app import app

from flask import request, jsonify

import json
import logging


@app.route('/')
def about():
    return 'The about page'


# основной метод в который будет ходить Миша
@app.route('/get-campaign-info', methods=['POST'])
def get_message():
    content = request.json
    logging.info(content)

    try:
        json_data = json.dumps(content)
        content = json.loads(json_data)
        market = content[0]

    except:
        print("json parsing error")
        raise ValueError

    result = {"losung": getatt(market), "logo": logo(market), "tam": getmarket(market)}

    return jsonify(**result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
