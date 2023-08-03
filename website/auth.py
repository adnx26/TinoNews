from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/xob")
def login():
    print("reached auth")
    return
