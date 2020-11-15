from django.core.management.base import BaseCommand, CommandError
from pokedex.models import Pokemon
import requests


class Command(BaseCommand):
    help = 'prints panzas'

    def add_arguments(self, parser):
        parser.add_argument('chain_id', nargs=1, type=int)

    def handle(self, *args, **options):
        id_chain = options['chain_id'][0]
        url = f'https://pokeapi.co/api/v2/evolution-chain/{id_chain}/'

        r = requests.get(url)
        data = r.json()

        pokemon_list = self.get_name_and_route(data['chain'], [])
        for pokemon in pokemon_list:
            evolutions = list(p for p in pokemon_list if p.name != pokemon.name)
            if len(evolutions) > 0:
                pokemon.evolutions.add(*evolutions)

        print(pokemon_list[0], 'evolution chain obtained')

    def get_name_and_route(self, data, pokemons):
        pokemon_id = data["species"]["url"].split("/")[-2]
        pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/').json()

        pokemon, created = Pokemon.objects.get_or_create(
            name=data['species']['name'],
            pokedex_id=pokemon_id,
            height=pokemon_data['height'],
            weight=pokemon_data['weight'],
            health=pokemon_data['stats'][0]['base_stat'],
            attack=pokemon_data['stats'][1]['base_stat'],
            defense=pokemon_data['stats'][2]['base_stat'],
            special_attack=pokemon_data['stats'][3]['base_stat'],
            special_defense=pokemon_data['stats'][4]['base_stat'],
            speed=pokemon_data['stats'][5]['base_stat'],
        )

        pokemons.append(pokemon)
        
        if data['evolves_to']:
            self.get_name_and_route(data['evolves_to'][0], pokemons)

        return pokemons
        