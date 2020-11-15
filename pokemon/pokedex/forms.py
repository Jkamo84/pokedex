from django import forms
    
class SearchPokemonForm(forms.Form):
    name = forms.CharField(help_text="Enter a Pokemon name", max_length=200)