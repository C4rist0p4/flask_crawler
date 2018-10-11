from flask import Flask, jsonify
from flask_crawler.Insta_Crawler import Insta_Crawler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():

    crawler = Insta_Crawler()
    items = crawler.crawl()

    return jsonify({'Movie': [item for item in items]})