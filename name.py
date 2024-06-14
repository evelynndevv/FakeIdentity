import json
import random


def load_names(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def random_last_name():
    last_names = load_names('names/last.json')["last_names"]
    return random.choice(last_names)


def name(isFemale):
    if isFemale:
        female_names = load_names('names/female.json')["female_names"]
        first_name = random.choice(female_names)
    else:
        male_names = load_names('names/male.json')["male_names"]
        first_name = random.choice(male_names)

    last_name = random_last_name()
    return f"{first_name} {last_name}"
