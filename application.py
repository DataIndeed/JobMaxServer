from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'this will be job max main page.'