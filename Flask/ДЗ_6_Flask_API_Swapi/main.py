# import requests
# import math

# films_link = 'https://swapi.dev/api/films/?format=json'
# films= requests.get('https://swapi.dev/api/films/?format=json').json()['results']
#
# part =2
# link = 'https://swapi.dev/api/films/'+str(part)+'/?format=json'
# film = requests.get(link).json()
#

#
import requests
import math

films = requests.get('https://swapi.dev/api/films/?format=json').json()['results']
# Получаем информацию о персонажах
link_characters = 'https://swapi.dev/api/people/?format=json'
characters = requests.get(link_characters).json()
page = math.ceil(characters['count'] / 10)
count = 1
dict_all_characters = {}
dict_all_numbers_character = {}
while count <= page:
    link_all = f'https://swapi.dev/api/people/?page={count}&format=json'
    char_all = requests.get(link_all).json()
    for character in char_all['results']:
        dict_all_characters[character['name']] = character['url']
        dict_all_numbers_character[character['name']] = character['url'].split('/')[-2]
    count += 1

# Получаем информацию о планетах
link_planets = 'https://swapi.dev/api/planets/?format=json'
planets = requests.get(link_planets).json()
page_planets = math.ceil(planets['count'] / 10)
dict_all_planets = {}
dict_all_numbers_planet = {}
count_p = 1
while count_p <= page_planets:
    link_all_planets = f'https://swapi.dev/api/planets/?page={count_p}&format=json'
    planets_all = requests.get(link_all_planets).json()
    for planet in planets_all['results']:
        dict_all_planets[planet['name']] = planet['url']
        dict_all_numbers_planet[planet['name']] = planet['url'].split('/')[-2]
    count_p += 1

