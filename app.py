import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def about():
    return 'The about page'


# основной метод в который будет ходить Миша
@app.route('/get-campaign-info', methods=['POST'])
def get_message():
    content = request.json
    print(content)
    #     здесь я буду писать логику, и доставать данные из JSON, который пришлет миша
    # TODO:
    # далее я буду формировать новый json
    res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext": "lalala"})


# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=10000)
