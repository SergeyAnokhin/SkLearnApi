from classificationManager import ClassificationManager

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
