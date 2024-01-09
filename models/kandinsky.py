import requests

import json
import time
import base64
from random import choice


class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "style": "DEFAULT",
            "negativePromptUnclip": "shadows, bright colors, acidity, high contrast, shadows",
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


def gen(prom, dirr="res"):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '0F07401138BBCE53349F57D8BCD5CDC8',
                        '4B1A38B5D6D22AD61ECD7A00F95F15E0')
    model_id = api.get_model()
    uuid = api.generate(prom, model_id)
    images = api.check_generation(uuid)

    image_base64 = images[0]

    # -------Декодируем строку base64 в бинарные данные

    # image_data = base64.b64decode(image_base64)

    # -------Открываем файл для записи бинарных данных изображения

    # with open(f"logo.jpg", "wb") as file:
    #     file.write(image_data)

    return image_base64


def logo(market):
    form = choice(["квадрат", "круг", "капля", "треугольник", "волны", "шестеренка"])
    zapros = f"prompt:Логотип компании на чистом белом фоне, {form}, {market}, минимализм, четкие линии, плоское изображение"
    return gen(zapros.replace("\n", " "), )


def lite_image(prom):
    return gen(prom.replace("\n", " "), )
