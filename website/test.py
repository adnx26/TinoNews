'''
import http.client
import json
from os import environ as env
from dotenv import find_dotenv, load_dotenv
from main import session



ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

conn = http.client.HTTPSConnection("tinotutor.us.auth0.com")

headers = { 'authorization': "Bearer " + env.get("MNGEMNT_API_TKN")}

conn.request("GET", "/api/v2/users?q=email%3A%22advaithnair26@gmail.com%22&search_engine=v3", headers=headers)


res = conn.getresponse()
data = res.read()
uuid = json.loads(data.decode("utf-8"))

print(uuid[0]["identities"][0]["user_id"])
'''

import http.client

conn = http.client.HTTPSConnection("")

payload = "grant_type=client_credentials&client_id=0TuQIx2LpUCOh7eY5T8CqIpkj16ye38o&client_secret=%7ByourClientSecret%7D&audience=https%3A%2F%2Ftinotutor.us.auth0.com%2Fapi%2Fv2%2F"

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/tinotutor.us.auth0.com/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))