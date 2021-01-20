from flask import jsonify

from app import app
from app.match_utils import find_most_similar_game_names


@app.route("/")
def main():
    return "Welcome to my app!"


@app.route("/find/")
@app.route("/find/<query_name>")
def find_game_name(query_name=None, num_matches=5):
    data = find_most_similar_game_names(query_name, num_matches)
    return jsonify(data)
