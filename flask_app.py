
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/science')
def hello_world():
    return 'I love science!'

@app.route('/')
def hello():
    return 'SCIENCE'

@app.route('/hahaha')
def HAHAHA():
    return 'THE JOKER'

@app.route('/frootloops')
def frootloops():
    return 'FROOT LOOPS ALL HAVE DIFFERENT FLAVORS!!!!!'