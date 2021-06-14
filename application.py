from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'this will be job max main page.'