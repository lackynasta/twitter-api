# tests/apis/test_tweet_view.py
from flask_testing import TestCase
from app import create_app

class TestTweetView(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_tweet(self):
        response = self.client.get("/tweets/hello")
        text = response.data.decode()
        self.assertIn("Goodbye", text)
