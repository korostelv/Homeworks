import requests
import math


# Получаем информацию о персонажах
link_characters = 'https://swapi.dev/api/people/?format=json'
characters = requests.get(link_characters).json()
print(characters)