from flask import Flask, request
from utils import getAPIResponse

app = Flask("_name_")

@app.route("/")
def index():
    return 'Api'

    
@app.route("/notas", methods=['POST', 'GET'])
def notas():

    if request.method == "GET":
        return 1
    
    elif request.method == "POST":
        return getAPIResponse(url="URL", request=request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)