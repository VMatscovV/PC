import requests
from flask import Flask, request, render_template, jsonify
import logging
import sys

app = Flask(__name__)


@app.route('/')
def about():
    return 'The about page'


# основной метод в который будет ходить Миша
@app.route('/get-campaign-info', methods=['POST'])
def get_message():
    content = request.json
    print(content)
    logging.info(content)
    #     здесь я буду писать логику, и доставать данные из JSON, который пришлет миша
    # # TODO:
    # # далее я буду формировать новый json
    # res = requests.post('/api/add_message/1234', json={"mytext": "lalala"})
    return jsonify(**request.json)


if __name__ == '__main__':
    app.debug = True
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    app.run(host='0.0.0.0', port=3000)
