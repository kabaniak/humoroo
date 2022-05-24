from flask import Flask, request
import flask
import json
from flask_cors import CORS

from find_similar_word import ten_similar
from WordsToComic import GenerateComic
from model import create_joke

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET", "POST"])
def users():
    print("users endpoint reached...")
    if request.method == "GET":
        with open("words.json", "r") as f:
            data = json.load(f)
            return flask.jsonify(data)
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")

        word1 = received_data['data']['noun1']
        word2 = received_data['data']['noun2']
        
        joke, word3 = create_joke(word1, word2)
        jokeForm = [joke[0].format(word1), joke[1].format(word2), joke[2].format(word3)]

        print("joke prepared")
    
        print(joke)
        print(jokeForm)
        GenerateComic(word1, word2, word3, jokeForm[0], jokeForm[1], jokeForm[2])

        print(f"image created")

        message = received_data['data']
        return_data = {
            "status": "success",
            "message": f"received: {message}",
            "simil": jokeForm
        }
        return flask.Response(response=json.dumps(return_data), status=201)

