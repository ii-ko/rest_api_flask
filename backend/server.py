from flask import Flask, jsonify


app = Flask(__name__)


# default route
@app.route('/')
def index():
    return jsonify({"Hello" : "World"})


if __name__ == '__main__':
    app.run(debug=True, port=8000)