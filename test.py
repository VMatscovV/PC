import requests

res = requests.post('http://pitch-construct.onrender.com/get-campaign-info', json={"mytext": "lalala"})
if res.ok:
    print(res.json())
