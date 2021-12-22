# tests/test_models.py
from unittest import TestCase
from app.models import Tweet  # Nous allons coder notre classe `Tweet` dans `app/models.py`.

class TestTweet(TestCase):
    def test_instance_variables(self):
        # Créer une instance de la classe `Tweet` avec un argument
        tweet = Tweet("my first tweet")
        # Vérifiez que `text` contient le contenu du tweet.
        self.assertEqual(tweet.text, "my first tweet")
        # Vérifiez que lors de la création d'une nouvelle instance de `Tweet`, sa date `created_at` est définie.
        self.assertIsNotNone(tweet.created_at)
        # Vérifier que l'id du tweet n'est pas encore attribué lors de la création d'un tweet en mémoire.
        self.assertIsNone(tweet.id)
