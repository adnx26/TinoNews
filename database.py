import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://TinoNews:tinonews1241@tinonews.ntbnmtj.mongodb.net/")

db = cluster["TinoNews"]
collection = db["Questions"]

post1 = {"_id": 0, "name": "xob", "score":5}
post2 = {"_id": 1, "name": "noble", "score":5}

#collection.insert_one(post1)
#collection.insert_many([post1, post2])


results = collection.find({"name": "xob", "score":5})

for result in results:
    print(result)
    print(result["_id"])

results = collection.find_one({"_id": 0})

print(result)