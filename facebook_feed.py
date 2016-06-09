#!/usr/bin/python

from pymongo import MongoClient
import requests 
import json
from bson.objectid import ObjectId

def fetch_facebook_feed():
    feed = []
    req = requests.get('https://graph.facebook.com/v2.6/110141895861579/?fields=feed&access_token='+access_token)
    data = json.loads(req.text)
    for item in data['feed']['data']:
        try:
            r = requests.get('https://graph.facebook.com/v2.6/'+item['id']+'/?fields=name,message,link,insights&access_token='+access_token)
            dt = json.loads(r.text)
            del dt['insights']['paging']
            feed.append(dt)
        except Exception as e:
            print (e)        
            
    if len(feed)>0:
        fb_feed.remove()
        fb_feed.insert(feed)
    else:
        fb_feed.insert(feed)    
        
if __name__ == '__main__':
    Connection = MongoClient('localhost', 27017)
    db = Connection.olap
    fb_feed = db.facebook_feed
    access_token = ""
    fetch_facebook_feed()