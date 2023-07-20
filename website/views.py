from flask import Blueprint, render_template, jsonify, request
import urllib.request, json
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
@views.route('/testxob')
def api():
    return render_template("apiTest.html")
