from flask import Flask, request
import json
import numpy as np

from model.loadModel import model, predict

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recieve_data():
    data = json.loads(request.data)

    labels = predict(model, np.array(data['data']))

    return ','.join(map(str, labels))
