import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print(f"Did you mean {get_close_matches(word, data.keys())[0]} instead?")
        decide = input("Press y or n : ")
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return print("Please type correct word.")
        else:
            return print("You have entered wrong input. PLease enter just y or n.")
    else:
        print("Entered word not found. Try again")


word = input("Enter the word you want to search : ")
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
