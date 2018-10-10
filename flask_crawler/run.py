from flask import Flask, jsonify
from flask_crawler.Insta_Crawler import Insta_Crawler
import json

app = Flask(__name__)

test_json = {
    'id': 1,
    'name': u'test',
    'preis': 55
}

@app.route('/', methods=['GET'])
def hello():

    crawler = Insta_Crawler()
    items = crawler.crawl()

    d = {'Movie': [item for item in items]}

    json_string = json.dumps(d)

    return jsonify(json_string)