from flask import Flask
from flask import request
from ApiPresentor import ApiPresentor
import datetime

app = Flask(__name__)
presentor = ApiPresentor()
print('start: {}'.format(datetime.datetime.now()))
presentor.Init()

@app.route('/')
def index():
    return presentor.status()

@app.route('/clearmodels')
def clearModels():
    pass

@app.route('/learn', methods=['POST'])
def learn():
    return presentor.learn(request.data)

@app.route('/fit')
def fit(json):
    pass

@app.route('/commit')
def commit(json):
    pass

@app.route('/rollback')
def rollback(json):
    pass

@app.route('/predict')
def predict(json):
    pass
