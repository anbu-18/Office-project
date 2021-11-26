from flask import Flask, request, jsonify
import malwaredetect

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Webpage</h1>"

@app.route('/insertdata/',methods=["POST"])
def insertdata():
    data = request.json
    obj = malwaredetect.malwaredetect()
    response = obj.table_values(data)
    return response

@app.route('/getalldata/',methods=["GET"])
def getalldata():
    #data = request.json
    obj = malwaredetect.malwaredetect()
    response = obj.getallvalues()
    return response

@app.route('/malwarecheck/',methods=["POST"])
def malwarecheck():
    data = request.json
    obj = malwaredetect.malwaredetect()
    response = obj.detection(data)
    return response    
        
