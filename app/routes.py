from flask import jsonify, request

from app import app
from app.match_utils import find_most_similar_game_names


@app.route("/")
def main():
    return "Welcome to my app!"


@app.route("/find/")
@app.route("/lv/")
@app.route("/levenshtein/")
def find_game_name_with_lv():
    query_name = request.args.get("name", "")
    num_matches = request.args.get("n", None)
    data = find_most_similar_game_names(
        query_name,
        num_matches,
        use_levenshtein=True,
    )
    return jsonify(data)


@app.route("/dl/")
@app.route("/difflib/")
def find_game_name_with_difflib():
    query_name = request.args.get("name", "")
    num_matches = request.args.get("n", None)
    data = find_most_similar_game_names(
        query_name,
        num_matches,
        use_levenshtein=False,
    )
    return jsonify(data)
