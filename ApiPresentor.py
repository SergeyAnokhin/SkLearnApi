from classificationManager import ClassificationManager
from statusManager import StatusManager
import json

class ApiPresentor:
    manager = ClassificationManager()
    statusManager = StatusManager()

    def Init(self):
        pass

    def configure(self, config):
        self.manager.configure(config)

    def addTrainData(self, data):
        self.manager.addTrainData(data)

    def fit(self):
        self.manager.fit()

    def predict(self, data):
        self.manager.predict(data)

### api status
    def status(self):
        print("#### STATUS #####")
        html = self.statusManager.status(self.manager)
        print("#### /STATUS ####")
        return html

### LEGACY
    def fitBinary(self, requestJson):
        print("#### FIT #####")
        print('Request : {}'.format(requestJson))
        learnData = json.loads(requestJson)
        result = self.manager.fitBinary(learnData)
        print('Result : {}'.format(result))
        print("#### /FIT ####")
        return json.dumps(result)

    def predictBinary(self, requestJson):
        print("#### PREDICT #####")
        print('Request : {}'.format(requestJson))
        learnData = json.loads(requestJson)
        result = self.manager.predictBinary(learnData)
        print('Result : {}'.format(result))
        print("#### /PREDICT ####")
        return json.dumps(result)
