import json

class Model():
    def __init__(self):
        self.getData()
        
    def getData(self):
        with open('./data.json', 'r') as f:
            data = f.read()
        self.data = json.loads(data)
        self.waitTime = int(self.data['waitTime'])
        self.spaceTime = int(self.data['spaceTime'])
        self.pathList = self.data['pathList']
    
    def setData(self):
        with open('./data.json', 'w') as f:
            f.write(json.dumps(self.data))