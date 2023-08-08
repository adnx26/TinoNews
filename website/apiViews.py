from flask import Blueprint, render_template, jsonify, request, Flask
import urllib.request, json
import os
import pymongo
from pymongo import MongoClient
from datetime import datetime
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import  redirect, session, url_for
import http.client


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


api = Blueprint('api', __name__, static_folder="static", template_folder="templates")



cluster = MongoClient("mongodb+srv://TinoTutor:tinotutor1241@tinotutor.dupch6q.mongodb.net/")
db = cluster["TinoTutor"]
QDB = db["Questions"] #Question Database
RDB = db["Replies"] #Replies Database
UDB = db["User"] #User Database
SDB = db["Subject"] # Subject Database

'''
conn = http.client.HTTPSConnection("tinotutor.us.auth0.com")

headers = { 'authorization': "Bearer " + env.get("MNGEMNT_API_TKN")}

conn.request("GET", "/api/v2/users?q=email%3A%22" + main.session.userinfo.name + "%22&search_engine=v3", headers=headers)


res = conn.getresponse()
data = res.read()
uuid = json.loads(data.decode("utf-8"))
print(uuid[0]["identities"][0]["user_id"])
'''

#API
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

@api.route('/')
def test():
    return "<h1>Hello</h1>"


#get question
@api.route('/api/question/get')
def get_questions():
    mydict = create_dict()
    for y in QDB.find():
        mydict.add(str(y['_id']), ({"uuid":y['uuid'],"time":y['time'],"context":y['context'], "subjectid":y['subjectid'], "schoolid":y['schoolid']}))
    return json.dumps(mydict)

#post question after enter into input box
@api.route('/api/question/post', methods=['POST'])
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
@api.route('/api/replies/get')
def get_replies():
    mydict = create_dict()
    for y in RDB.find():
        mydict.add(str(y['_id']), ({"qid":y['qid'],"uuid":y['uuid'],"time":y['time'], "context":y['context']}))
    return json.dumps(mydict)

@api.route('/api/replies/post', methods=['POST'])
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
@api.route('/api/subjects/get')
def get_subjects():
    mydict = create_dict()
    for y in SDB.find():
        mydict.add("Subjects", ({"CALCAB":y['CALCAB'],"APLIT":y['APLIT']}))
    return json.dumps(mydict)

@api.route('/api/user/post')
def add_user():
    data = request.get_json()
    data = jsonify(data)
    print(data)
    return '', 204

