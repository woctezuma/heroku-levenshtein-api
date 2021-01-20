from flask import jsonify, request

from app import app
from app.match_utils import find_most_similar_game_names


@app.route("/")
def main():
    return "Welcome to my app!"


@app.route("/find/")
def find_game_name():
    query_name = request.args.get("name", "")
    num_matches = request.args.get("n", None)
    data = find_most_similar_game_names(query_name, num_matches)
    return jsonify(data)
