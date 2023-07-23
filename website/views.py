from flask import Blueprint, render_template, jsonify, request
import urllib.request, json
import os
import pymongo
from pymongo import MongoClient


views = Blueprint('views', __name__)
cluster = MongoClient("mongodb+srv://TinoTutor:tinotutor1241@tinotutor.dupch6q.mongodb.net/")
db = cluster["TinoTutor"]
QDB = db["Questions"] #Question Database
RDB = db["Replies"] #Replies Database
UDB = db["User"] #User Database
SDB = db["Subject"] # Subject Database

#QDB.insert_one({"_id": 0, "uuid": "xob", "time":5, "context":"What is 2+2", "subjectid": "MTH"})

@views.route('/')
def home():
    return render_template("test.html", question = "placeholder")

#API
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

mydict = create_dict()
for y in QDB.find():
    mydict.add("Questions", ({"uuid":y['uuid'],"time":y['time'],"context":y['context'], "subjectid":y['subjectid']}))
#get question
@views.route('/api/question/get')
def get_questions():
    return json.dumps(mydict)

@views.route('/api/question/post', methods=['POST'])
def add_questions():
    data = request.get_json()
    data = jsonify(data)

    print(request.get_json())
    QDB.insert_one(str(json.loads(data)))

    return '', 204
