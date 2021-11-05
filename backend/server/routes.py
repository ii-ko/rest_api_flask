from flask import jsonify, request
from ..server.models import Articles, ArticlesSchema
from ..server import app, db
# from backend.server.db import Articles, ArticlesSchema
# from backend.server import app, db

# to save data, to show data by schema
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
    return article_schema.jsonify(articles)


@app.route('/get/<id>/', methods=['GET'])
def get_by_id(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)


@app.route('/update/<id>/', methods=['PUT'])
def update_by_id(id):
    # request from db
    article = Articles.query.get(id)

    # request Data
    title = request.json['title']
    body = request.json['body']

    # replace data
    article.title = title
    article.body = body

    # update data
    db.session.commit()

    return article_schema.jsonify(article)


@app.route('/delete/<id>/', methods=['DELETE'])
def delete_by_id(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article)