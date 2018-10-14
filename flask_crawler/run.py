from flask import Flask, jsonify, render_template, request
from flask_crawler.Insta_Crawler import InstaCrawler


app = Flask(__name__)


@app.route("/search")
def test():
    search = request.args.get('search')
    print(search)

    if search is None:
        return render_template('test.html')
    else:
        crawler = InstaCrawler(search)
        items = crawler.crawl()

        return jsonify(items)
