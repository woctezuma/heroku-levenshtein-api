from flask import jsonify

from app import app

@app.route("/")
def main():
    return "Welcome to my app!"

@app.route("/<name>")
def match_game_name(name=None):
    matches = get_matches(name)
    return jsonify(matches)

