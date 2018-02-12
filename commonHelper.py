class CommonHelper:
    def ReadFile(self, path):
        with open(path, 'r') as myfile:
            return myfile.read()