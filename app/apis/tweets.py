# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource

api = Namespace("tweets")


@api.route("/hello")
class TweetResource(Resource):
    def get(self):
        return "Goodbye from the 'tweets' namespace!"
