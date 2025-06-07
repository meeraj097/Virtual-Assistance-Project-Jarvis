import requests
from ss import *


api_address = f'http://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid={key2}'
json_data = requests.get(api_address).json()

# Print the JSON data to inspect its structure
#print(json_data)

def temp():
    try:
        if 'main' in json_data:
            temperature = round(json_data["main"]["temp"] - 273.15, 1)
            return temperature
        else:
            return "Main key not found in the response."
    except Exception as e:
        return f"An error occurred: {e}"

def des():
    try:

        if 'weather' in json_data and len(json_data['weather']) > 0:
            description = json_data["weather"][0]["description"]
            return description
        else:
            return "Weather key not found in the response."
    except Exception as e:
        return f"An error occurred: {e}"


# temperature = temp()
# description = des()
# # speak(f"The current temperature in Hyderabad is {temperature} degrees Celsius with {description}.")
# print(f"The current temperature in Hyderabad is {temperature} degrees Celsius.")
# print(description)
