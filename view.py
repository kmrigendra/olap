#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run
import json
from pymongo.mongo_client import MongoClient


@route('/')
def load_feed():
    feed = []
    for item in fb_feed.find():
        del item['_id']
        feed.append(item)
    return json.dumps(feed) 

if __name__ == '__main__':
    Connection = MongoClient('localhost', 27017)
    db = Connection.olap
    fb_feed = db.facebook_feed
    run(host='localhost', port=8087, server='waitress')
