from app_writers import app
from flask import render_template, url_for, redirect, request


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



@app.route('/writers/hemingway')
@app.route('/writers/Hemingway')
def hemingway():
    return render_template('hemingway.html')

@app.errorhandler(404)
def error_page(error):
    return redirect(url_for('index'))


@app.route('/cities/writers=<write>&year=<int:year>')
@app.route('/writers/writers=<write>&year=<int:year>')
def cities(write, year):
    if write in books_year and year in books_year[write]:
        books = books_year[write][year]
        return render_template('cities.html', writer=write, year=year, books=books)
    else:
        return redirect(url_for(write.lower()))

