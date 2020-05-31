import random
import json

# Read value from JSON file
def read_character_from_json():
    values = []
    with open('characters.json') as f:
        data = json.load(f)
        for entry in data:
            values.append(entry['character'])
        return values

# Read value form JSON file
def read_quote_from_json():
    values = []
    with open('quotes.json') as f:
        data = json.load(f)
        for entry in data:
            values.append(entry['quote'])
        return values

# Show random quote 
def get_random_item(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb]
    return item

def random_character():
    all_values = read_character_from_json()
    return get_random_item(all_values)

def random_quote():
    all_values = read_quote_from_json()
    return get_random_item(all_values)

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} aurais peut-etre dit : '{}'".format(character, quote)

# ask user for action
user_answer = input("Tapez entree pour connaitre une autre citation ou B pour quitter le programme : ")

# loop  
while user_answer != "B" :
  
    print(message(random_character(), random_quote()))
    user_answer = input("Tapez entree pour connaitre une autre citation ou B pour quitter le programme : ")



