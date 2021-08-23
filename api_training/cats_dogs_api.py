  
import requests
import json
import webbrowser
from enum import IntEnum


def change_parameters_facts(animal_type, amount_of_facts):
    params = {
        "amount": amount_of_facts,
        "animal_type": animal_type,
    }
    return params


def display_facts(website_url, params):
    website = requests.get(website_url, params)
    try:
        content = website.json()
    except json.decoder.JSONDecodeError:
        print("NIEPOPRAWNY FORMAT!")
    else:
        for animal in content:
            print(animal["text"])


def display_image_dogs(image_url):
    website_image = requests.get(image_url)
    try:
        content = website_image.json()
    except json.decoder.JSONDecodeError:
        print("NIEPOPRAWNY FORMAT!")
    else:
        webbrowser.open_new_tab(content["message"])


def display_image_cats(website_url, parameters):
    params = {
        "breed_id": parameters,
    }

    website_cat = requests.get(website_url, params)

    try:
        content = website_cat.json()
    except json.decoder.JSONDecodeError:
        print("Nieprawidłowy format!")
    else:
        for cat in content:
            webbrowser.open_new_tab(cat["url"])


numberOfFacts = int(input("Podaj liczbę faktów do wyświetlenia: "))

animalType = IntEnum("animalType", "Kot Pies")

choice = int(
    input(
        """ Chcę fakty o:
    1. Kotach(1)
    2. Psach(2)
"""
    )
)
if choice == animalType.Kot:
    parameters = change_parameters_facts("cat", numberOfFacts)
    display_facts("https://cat-fact.herokuapp.com/facts/random/", parameters)
    display_image_cats("https://api.thecatapi.com/v1/images/search", "beng")

elif choice == animalType.Pies:
    parameters = change_parameters_facts("dog", numberOfFacts)
    display_facts("https://cat-fact.herokuapp.com/facts/random/", parameters)
    display_image_dogs("https://dog.ceo/api/breeds/image/random")
