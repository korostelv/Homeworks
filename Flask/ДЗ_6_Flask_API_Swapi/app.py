from flask import Flask, render_template, url_for
import requests
from main import films, dict_all_characters, dict_all_numbers_character, dict_all_planets, dict_all_numbers_planet

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('/index.html', films=films)


@app.route('/<int:part>/film')
def film(part):
    link_films = 'https://swapi.dev/api/films/' + str(part) + '/?format=json'
    film = requests.get(link_films).json()
    link_characters = 'https://swapi.dev/api/people/?format=json'
    characters = requests.get(link_characters).json()

    return render_template('/film.html',
                           part=part,
                           film=film,
                           characters=characters,
                           dict_all_characters=dict_all_characters,
                           dict_all_numbers_character=dict_all_numbers_character,
                           dict_all_planets=dict_all_planets,
                           dict_all_numbers_planet=dict_all_numbers_planet
                           )


@app.route('/<int:char>/people')
def character(char):
    link_people ='https://swapi.dev/api/people/' + str(char) + '/?format=json'
    people = requests.get(link_people).json()


    return render_template('/people.html',people=people,char=char)


if __name__ == '__main__':
    app.run(debug=True)

