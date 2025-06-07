import requests
import random
from ss import key1  # Make sure you have your API key stored in the 'ss' module

api_address = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={key1}'
json_data = requests.get(api_address).json()

# Store all articles titles
all_titles = [article["title"] for article in json_data["articles"]]


def news():
    # Shuffle the titles to get random articles each time
    random.shuffle(all_titles)

    # Select the top 4 articles (or however many you want to read)
    selected_titles = all_titles[:4]

    # Prepare the news output
    ar = [f"Number {i + 1}, {title}" for i, title in enumerate(selected_titles)]
    return ar

# Example usage
# arr = news()
# for item in arr:
#     print(item)
#    speak(item)