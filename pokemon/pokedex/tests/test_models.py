from django.test import TestCase
from django.template.defaultfilters import slugify
from pokedex.models import Pokemon


class ModelsTestCase(TestCase):
    def test_pokemon_created(self):
        """Posts are given slugs correctly when saving"""
        pokemon = Pokemon.objects.create(
            name='charizard',
            pokedex_id=6,
            height=10,
            weight=10,
            health=10,
            attack=10,
            defense=10,
            special_attack=10,
            special_defense=10,
            speed=10,
        )

        self.assertEqual(pokemon.name, 'charizard')