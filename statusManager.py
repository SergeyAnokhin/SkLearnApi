from classificationManager import ClassificationManager

class StatusManager:

    def status(self, classificationManager: ClassificationManager):
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
        for key, value in classificationManager.classifiers.items():
            result = result + '<tr><td><b>{}</b></td><td><pre>{}</pre></td><tr>\n'.format(key, value)
        result = result + '</table></body></html>'
        return result