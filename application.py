from flask import Flask
application = Flask(__name__)

@application.route('/')
def main_page():
    return 'this will be job max main page.'