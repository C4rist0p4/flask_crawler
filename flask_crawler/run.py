from flask import Flask, jsonify
from flask_crawler.Insta_Crawler import InstaCrawler

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():

    crawler = InstaCrawler('sport')
    items = crawler.crawl()

    return jsonify(items)
