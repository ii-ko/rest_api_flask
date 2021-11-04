import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.Text())
    date_created = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, title, body):
        self.title = title
        self.body = body


# Create DB Schema
class ArticlesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')


article_schema = ArticlesSchema()
articles_schema = ArticlesSchema(many=True)


# default route
@app.route('/', methods=['GET'])
def index():
    return jsonify({"Hello" : "World"})


# route for post
@app.route('/post', methods=['POST'])
def post():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return articles_schema.jsonify(articles)


if __name__ == '__main__':
    app.run(debug=True, port=8000)