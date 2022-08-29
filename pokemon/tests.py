from django.test import TestCase
from .models import Pokemon
from django.contrib.auth import get_user_model

class PokemonTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser", password="pass")
        testuser1.save()

        test_pokemon = Pokemon.objects.create(name="Marco", owner=testuser1, level=12)

    def test_pokemon_model(self):
        pokemon = Pokemon.objects.get(id=1)
        actual_owner = str(pokemon.owner)
        actual_name = str(pokemon.name)
        actual_level = pokemon.level
        self.assertEqual(actual_level, 12)
        self.assertEqual(actual_name, "Marco")
        self.assertEqual(actual_owner, "testuser")