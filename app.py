from flask import Flask, request, jsonify
import config
import malwaredetect
import json
import os




app = Flask(__name__)

########################## Main Page #########################################################
@app.route('/')
def index():
    try:
        return "<h1>Webpage</h1>"
    except Exception as e:
        print("unable to load home page: ",e)
        return "unable to load home page"

########################## To insert URL into database from json request######################
@app.route('/insertdata/',methods=["POST"])
def insertdata():
    try:
        data = request.json
        obj = malwaredetect.malwaredetect()
        response = obj.table_values(data)
        return response
    except Exception as e:
        print(" Error while processing json request: ",e)
        return "Error while processing json request"

######################### Get all values from a database #####################################
@app.route('/getalldata/',methods=["GET"])
def getalldata():
    try:
        obj = malwaredetect.malwaredetect()
        response = obj.getallvalues()
        return response
    except Exception as e:
        print("Error while processing json request: ",e)
        return "Error while processing json request"

######################### To check whether a url is available in database ###################
@app.route('/malwarecheck/',methods=["POST"])
def malwarecheck():
    try:
        data = request.json
        obj = malwaredetect.malwaredetect()
        response = obj.detection(data)
        return response
    except Exception as e:
        print(" Error while processing json request: ",e)
        return "Error while processing json request"
        

######################### To insert the URL from a text file into database ###############
@app.route('/getfile/',methods=["POST"])
def getfile():
    try:
        file = request.files['file']
        fileContent = file.read().decode("utf-8")
        replaceWhitespace=fileContent.replace("\n", ",").strip()
        splitter = replaceWhitespace.split(",")
        for i in splitter:
            if i.strip() != "":
                userrequest = {'url':i.strip()}
                obj=malwaredetect.malwaredetect()
                response=obj.table_values(userrequest)
        return response
    except Exception as e:
        print("Error while processing input file: ",e)
        return "Error while processing input file"

################################ To clear values from a database ##########################
@app.route('/deleteall/',methods=["DELETE"])
def deleteall():
    try:
        obj= malwaredetect.malwaredetect()
        response = obj.deleteall()
        return response
    except Exception as e:
        print("Error while processing json request: ",e)
        return "Error while processing json request"
        
if __name__ == '__main__':
    obj= malwaredetect.malwaredetect()
    response = obj.table_creation()
    app.run(debug=True,host='0.0.0.0')
        
