from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added', auto_now_add=True)
    pokedex_id = models.IntegerField('pokedex id')
    height = models.IntegerField('height')
    weight = models.IntegerField('weight')
    health = models.IntegerField('stats')
    attack = models.IntegerField('attack')
    defense = models.IntegerField('defense')
    special_attack = models.IntegerField('special attack')
    special_defense = models.IntegerField('special defense')
    speed = models.IntegerField('speed')
    evolutions = models.ManyToManyField('Pokemon', blank=True)

    def __str__(self):
        return self.name