from flask import Flask
from ApiPresentor import ApiPresentor
import datetime

app = Flask(__name__)
presentor = ApiPresentor()
print('start: ' + datetime.datetime.now())
presentor.Init()

@app.route('/')
def index():
    return 'SkLearn API. Status : '

@app.route('/clearmodels')
def clearModels():
    pass

@app.route('/learn')
def learn(json):
    pass

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
