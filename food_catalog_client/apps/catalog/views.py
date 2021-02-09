from django.shortcuts import render, redirect
from food_catalog_client.apps.catalog.entities.food import Food
from food_catalog_client.apps.catalog.entities.cake import Cake
from food_catalog_client.apps.catalog.entities.drinks import Drink

def home(request):
    foods = [
        [
            Cake("Sandwich", "Blue", "sandwich.jpg"),
            Food("Steak", "Steak enak", "steak.jpg"),
            Cake("Cherries", "Pink", "cherries.jpg"),
            Food("Steak", "Steak enak", "croissant.jpg"),
        ],
        [
            Drink("Es Popsicle", "Panas panas dingin", "popsicle.jpg"),
            Drink("Es Jeruk Panas", "Jeruk nya enak tapi panas dingin", "jeruk_panas.jpg"),
            Drink("Es Jus Mangga", "Jus Mangga paling niqmat", "sandwich.jpg"),
            Drink("Es Jeruk Dingin", "Yang ini mah dingin", "wine.jpg"),
        ],
    ]
    return render(request, 'food.html', {'foods': foods})

def foods(request):
    foods = [
        [
            Cake("Sandwich", "Blue", "sandwich.jpg"),
            Food("Steak", "Steak enak", "steak.jpg"),
            Cake("Cherries", "Pink", "cherries.jpg"),
            Food("Steak", "Steak enak", "croissant.jpg"),
        ],
    ]
    return render(request, 'food.html', {'foods': foods})


def drinks(request):
    drinks = [
        [
            Drink("Es Popsicle", "Panas panas dingin", "popsicle.jpg"),
            Drink("Es Jeruk Panas", "Jeruk nya enak tapi panas dingin", "jeruk_panas.jpg"),
            Drink("Es Jus Mangga", "Jus Mangga paling niqmat", "sandwich.jpg"),
            Drink("Es Jeruk Dingin", "Yang ini mah dingin", "wine.jpg"),
        ],
    ]
    return render(request, 'drinks.html', {'foods': drinks})


def about(request):
    return render(request, 'about.html')
