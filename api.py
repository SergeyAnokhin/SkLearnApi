from flask import Flask
from flask import request
from ApiPresentor import ApiPresentor
from commonHelper import CommonHelper
import datetime

app = Flask(__name__)
presentor = ApiPresentor()
cHelper = CommonHelper()
print('start: {}'.format(datetime.datetime.now()))
presentor.Init()

@app.route('/')
def index():
    return presentor.status()

@app.route('/Hello')
def hello():
    return 'OK'

@app.route('/fit', methods=['POST'])
def fit():
    return presentor.fit(request.data)

@app.route('/predict', methods=['POST'])
def predict(json):
    return presentor.predict(request.data)

@app.route('/fitTest', methods=['GET'])
def fitTest():
    return presentor.fit(cHelper.ReadFile('fitTest.json'))
