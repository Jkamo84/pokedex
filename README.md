# Project Title

Simple Pokemon Search App

## Description

A form where a name is queried, and the stats and evolutions of that pokemon are retrieved.
Additionally, there is a management command to retrieve pokemons by evolution chain.

## Getting Started

### Dependencies

Create a virtual environment and instll these dependencies

* This app was made with Django 3.1.3
* requests 2.24.0

> pip install -r requirements

can be used to install the dependencies

### Executing retrieving command

> python manage.py retrieve {id}

where "id" would be the evolution chain ID

### Testing

currently there are only two tests for the model and the view, to run them:

> python manage.py test pokedex/tests

## Authors

Juan Camilo Plazas 

## Version History

* 0.1
    * Initial Release
