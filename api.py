from flask import Flask
from flask import request
from ApiPresentor import ApiPresentor
from commonHelper import CommonHelper
import datetime

# run locally :
# export FLASK_APP=api.py
# flask run

app = Flask(__name__)
# app.run(host='127.0.0.1', port=99)
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

@app.route('/configure', methods=['POST'])
def fit():
    return presentor.configure(request.data)

@app.route('/fit', methods=['POST'])
def fit():
    return presentor.fit(request.data)

@app.route('/predict', methods=['POST'])
def predict():
    return presentor.predict(request.data)

@app.route('/fitTest', methods=['GET'])
def fitTest():
    return presentor.fit(cHelper.ReadFile('fitTest.json'))
