import requests

def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    json_data = requests.get(url).json()
    return [json_data["setup"], json_data["punchline"]]

previous_jokes = []

def get_new_joke():
    global previous_jokes
    new_joke = joke()
    while new_joke in previous_jokes:
        new_joke = joke()
    previous_jokes.append(new_joke)
    if len(previous_jokes) > 5:
        previous_jokes.pop(0)
    return new_joke