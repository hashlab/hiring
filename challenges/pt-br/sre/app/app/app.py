from flask import Flask
from flask.json import jsonify
from flask_httpauth import HTTPTokenAuth
from prettyconf import config

from .utils import fetch_count_from_redis, store_count_in_redis


def create_app():
    app = Flask(__name__)
    auth = HTTPTokenAuth("Token")

    @auth.verify_token
    def verify_token(token):
        return token == config("AUTH_TOKEN")

    @app.route("/")
    @auth.login_required
    def access_counter():
        count = fetch_count_from_redis()
        count = count + 1
        store_count_in_redis(count)

        return jsonify({"access_counter": count})

    return app
