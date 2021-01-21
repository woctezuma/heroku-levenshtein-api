from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/find/*": {"origins": "*"}})

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["25 per hour", "5 per minute"]
)

from app import routes
