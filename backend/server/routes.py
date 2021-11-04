from flask import jsonify, request
from backend.server.db import Articles, ArticlesSchema
from backend.server import app, db

# to save data
article_schema = ArticlesSchema()
# to show data
articles_schema = ArticlesSchema(many=True)


# default route
@app.route('/', methods=['GET'])
def index():
    all_articles = Articles.query.all()
    res = articles_schema.dump(all_articles)
    return jsonify(res)


# route for post
@app.route('/post', methods=['POST'])
def post():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return articles_schema.jsonify(articles)