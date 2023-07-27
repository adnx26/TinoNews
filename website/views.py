from flask import Blueprint, render_template, jsonify, request, Flask
import urllib.request, json
import os
import pymongo
from pymongo import MongoClient
from datetime import datetime



#views = Blueprint('views', __name__)
cluster = MongoClient("mongodb+srv://TinoTutor:tinotutor1241@tinotutor.dupch6q.mongodb.net/")
db = cluster["TinoTutor"]
QDB = db["Questions"] #Question Database
RDB = db["Replies"] #Replies Database
UDB = db["User"] #User Database
SDB = db["Subject"] # Subject Database

views = Flask(__name__)



@views.route('/')
def home():
    return render_template("home.html", question = "placeholder")


#API
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value




#get question
@views.route('/api/question/get')
def get_questions():
    mydict = create_dict()
    for y in QDB.find():
        mydict.add(y['_id'], ({"uuid":y['uuid'],"time":y['time'],"context":y['context'], "subjectid":y['subjectid'], "schoolid":y['schoolid']}))
    return json.dumps(mydict)

#post question after enter into input box
@views.route('/api/question/post', methods=['POST'])
def add_questions():
    data = request.get_json()
    data = jsonify(data)

    questionDict ={
        "uuid": 0,
        "time": str(datetime.now()),
        "context": request.get_json()["Question"],
        "subjectid": "CALCAB",
        "schoolid": 10
    }

    
    QDB.insert_one(questionDict)
    return '', 204


#get replies
@views.route('/api/replies/get')
def get_replies():
    mydict = create_dict()
    for y in RDB.find():
        mydict.add(y['_id'], ({"qid":y['qid'],"uuid":y['uuid'],"time":y['time'], "context":y['context']}))
    return json.dumps(mydict)

@views.route('/api/replies/post', methods=['POST'])
def add_replies():
    data = request.get_json()
    data = jsonify(data)
    repliesDict ={
        "qid": 0,
        "uuid":0,
        "time": str(datetime.now()),
        "context": request.get_json()["Replies"],
    }

    
    RDB.insert_one(repliesDict)
    return '', 204

#get subjects
@views.route('/api/subjects/get')
def get_subjects():
    mydict = create_dict()
    for y in SDB.find():
        mydict.add("Subjects", ({"CALCAB":y['CALCAB'],"APLIT":y['APLIT']}))
    return json.dumps(mydict)


if __name__ == '__main__':
    views.run(debug=True)