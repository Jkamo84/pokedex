from pokedex.models import Pokemon
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import SearchPokemonForm

class IndexView(TemplateView):
    template_name = "pokedex/index.html"
    form_class = SearchPokemonForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'welcome_message': 'Welcome to the Pokemon finder (pokedex)!',
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'welcome_message': 'Welcome to the Pokemon finder (pokedex)!',
            'form': form,
            'pokemon': None,
            'pre_evolutions': [],
            'evolutions': []
        }
        if form.is_valid():
            pokemon = Pokemon.objects.filter(name=request.POST.get('name')).last()
            if pokemon:
                context['pokemon'] = pokemon
                for evolution in pokemon.evolutions.all():
                    print(pokemon.id, evolution.pokedex_id)
                    if evolution.pokedex_id < pokemon.pokedex_id:
                        context['pre_evolutions'].append(evolution)
                    else:
                        context['evolutions'].append(evolution)

        if not context['pokemon']:
            context['not_found'] = 'We could not find that Pokemon. It could not be on the database yet, or it does not exist.'

        return render(request, self.template_name, context)
