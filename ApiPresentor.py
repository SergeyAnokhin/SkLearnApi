from classificationManager import ClassificationManager
import json

class ApiPresentor:
    manager = ClassificationManager()

    def Init(self):
        self.manager.Init()

    def status(self):
        result = '''<!DOCTYPE html><html><head><style>
pre {
    display: block;
    font-family: monospace;
    white-space: pre;
    margin: 1em 0;
}
.text{
    font-family: verdana;
    font-size: 12px;
}
</style></head><body><div class='text'>SkLearn API. Status : </div><table class='text'>'''
        for key, value in self.manager.classifiers.items():
            result = result + '<tr><td><b>{}</b></td><td><pre>{}</pre></td><tr>\n'.format(key, value)
        result = result + '</table></body></html>'
        return result

    def fit(self, requestJson):
        print("#### FIT #####")
        print('Request : {}'.format(requestJson))
        learnData = json.loads(requestJson)
        result = self.manager.fit(learnData)
        print('Result : {}'.format(result))
        print("#### /FIT ####")
        return json.dumps(result)

    def predict(self, requestJson):
        print("#### PREDICT #####")
        print('Request : {}'.format(requestJson))
        learnData = json.loads(requestJson)
        result = self.manager.predict(learnData)
        print('Result : {}'.format(result))
        print("#### /PREDICT ####")
        return json.dumps(result)
