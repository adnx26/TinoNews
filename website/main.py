from flask import Flask, render_template

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
from apiViews import api

from auth0.authentication import Users

domain = 'tinotutor.auth0.com'



ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


app.register_blueprint(api, url_prefix="/admin")


oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

@app.route("/")
def home():
    return render_template(
        "test.jinja",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    print(token)
    print("-------------------------------------------------")
    print(session["user"]["access_token"])
    return redirect("/")


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


if __name__ == "__main__":
    app.run(debug=True)