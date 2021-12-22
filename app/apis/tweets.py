# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository
from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from app.models import Tweet

api = Namespace('tweets')

tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})

@api.route('/<int:id>', methods=['GET'])
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.marshal_with(tweet)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet

@api.route('/add', methods=['POST'])
@api.response(404, 'Tweet not found')
class CreateTweet(Resource):
    def post(self):
        data = request.get_json()
        if data is None:
            api.abort(400)
        text = data.get('text')
        if text is None:
            api.abort(400)
        tweet = Tweet(text)
        tweet_repository.add(tweet)
        return 'tweet inséré', 200

@api.route('/<int:id>', methods=['PATCH'])
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class UpdateTweet(Resource):
    def patch(self, id):
        data = request.get_json()
        if data is None:
            api.abort(400)
        text = data.get('text')
        if text is None:
            api.abort(400)
        tweet = tweet_repository.get(id)
        tweet_repository.update(tweet, text)
        return 'tweet à jour', 200

@api.route('/', methods=['DELETE'])
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    def delete(self):
        tweet_repository.clear()
        return 'tous les tweets supprimés', 200

@api.route('/<int:id>', methods=['DELETE'])
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    def delete(self, id):
        tweet = tweet_repository.get(id)
        tweet_repository.delete(tweet)
        return 'tweet supprimé', 200
