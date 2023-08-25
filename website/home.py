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


website = Blueprint('website', __name__, static_folder="static", template_folder="templates")

temp = ""

@website.route("/<subjectID>")
def subjectPage(subjectID):
    print(subjectID)
    return render_template("questionsPage.jinja", subjectID=subjectID)

@website.route("/<int:questionId>")
def questionPage(questionId):
    print(questionId)
    return render_template("questionsPage.jinja", questionId=questionId)


