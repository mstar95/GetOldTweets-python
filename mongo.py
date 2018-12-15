import json

from bson import json_util
from pymongo import MongoClient


def toJson(t):
    value = json.dumps(t.__dict__, default=json_util.default)
    value = json.loads(value, object_hook=json_util.object_hook)
    return value


def createMongo():
    client = MongoClient('localhost', 27017)
    db = client.tweets_db
    collection = db.tweets

    return collection


def mongoSaver(collection):
    def save(tweets):

        tweets = map(toJson, tweets)
        collection.insert_many(tweets)

    return save
