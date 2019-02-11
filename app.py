from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        return 'Hello, World!'
    else:
    	return 'Nothing Here'
