from flask import Flask, request
import json
import numpy as np

from model.loadModel import model, predict

app = Flask(__name__)

labels_to_remove = '''
6
7
8
10
14
17
20
23
24
25
26
27
29
30
32
33
34
35
37
40
41
42
43
46
48
50
51
52
54
55
57
58
59
'''.strip().split('\n')

@app.route('/', methods=['POST'])
def recieve_data():
	data = json.loads(request.data)

	x = np.array(data['data'])

	x = x.reshape((*x.shape, 1))

	labels = predict(model, np.array(x))

	for idx, label in enumerate(labels):
		if str(label) in labels_to_remove:
			labels[idx] = 0
		else:
			labels[idx] = 1

	return ','.join(map(str, labels))
