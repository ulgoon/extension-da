from flask import Flask
from flask import json, Response
from pymongo import MongoClient
from bson import json_util
# requirement: flask($ pip install flask)

# define app using Flask
app = Flask(__name__)

# route(ex> https://www.naver.com"/news" )
@app.route('/')
def index():
    return "hello"

# route for api server
# load data from mlab with pymongo
# bson to json => serve over /api/v1/naver
@app.route('/api/v1/naver')
def get_keyword():
    # customize your uri
    uri = "mongodb://strongadmin:12341234@ds123500.mlab.com:23500/collections"
    # connect client
    client = MongoClient(uri)
    db = client.collections
    query_list = db.nvquerylist
    # make dictionary from loaded data from query_list
    results = {"data":
            [
                item for item in query_list.find({})
            ]
        }
    # serve json data over http
    return Response(json_util.dumps(results), mimetype="application/json")

# flask run with shell
if __name__ == '__main__':
    app.run('0.0.0.0', port=8088)
