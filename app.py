
from flask import Flask, request

app = Flask(__name__)

global dataList
dataList = []

@app.route('/',methods = ['POST', 'GET', 'HEAD'])
def index():
    data = {
        'name' : None,
        'lastname' : None,
        'address' : None,
        'birthday' : None,
        'latitude' : None,
        'longitude' : None
    }
    if request.method == 'POST':
        data = request.data
        dataList.append(data)
        print(dataList)
        return data
    else:
        if request.method == 'GET':
            try:
                return dataList.pop()
            except IndexError:
                return data
        else:
            return data

if __name__ == "__main__":
    app.run()