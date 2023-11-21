from app import app
from flask import render_template, url_for, redirect, request

top = ['Гарри Поттер', 'Зеленая миля', 'Властелин колец', 'Старик и море', 'И восходит солнце', ]

books_year = {
    'Hemingway': {
        1925: ['In Our Time'],
        1926: ['The Sun Also Rises', 'Men Without Women'],
        1940: ['For Whom the Bell Tolls']
    },
    'Shakespeare': {
        1997: ['Harry Potter and the Philosophers Stone'],
        1998: ['Harry Potter and the Chamber of Secrets']
    }
}


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html')


@app.route('/writers')
def writers():
    return render_template('writers.html')


@app.route('/books')
def books():
    return render_template('books.html', top=top)


@app.route('/writers/hemingway')
@app.route('/writers/Hemingway')
def hemingway():
    return render_template('hemingway.html')


@app.route('/writers/Shakespeare')
@app.route('/writers/shakespeare')
def shakespeare():
    return render_template('shakespeare.html')


@app.route('/books/1')
@app.route('/writers/rouling/garry_potter')
def potter():
    return render_template('potter.html')


@app.route('/books/2')
@app.route('/writers/king/green_mile')
def green_mile():
    return render_template('green_mile.html')


@app.route('/books/3')
@app.route('/writers/tolkien/lord_of_rings')
def lord_of_rings():
    return render_template('lord_of_rings.html')


@app.route('/books/4')
@app.route('/writers/hemingway/the_old_man_and_the_sea')
def the_old_man_and_the_sea():
    return render_template('old_man.html')


@app.route('/books/5')
@app.route('/writers/hemingway/the_sun_also_rises')
def the_sun_also_rises():
    return render_template('sun.html')


@app.errorhandler(404)
def error_page(error):
    return redirect(url_for('index'))


@app.route('/<path:section>/<error>')
def redirect_to_section(section, error):
    return redirect(url_for(section))


# @app.route('/writers/<section>/<error>')
# def redirect_to_section2(section, error):
#     return redirect(url_for(section))


@app.route('/cities/writers=<write>&year=<int:year>')
def cities(write, year):
    if write in books_year and year in books_year[write]:
        books = books_year[write][year]
        return render_template('cities.html', writer=write, year=year, books=books)
    else:
        return redirect(url_for(write.lower()))

