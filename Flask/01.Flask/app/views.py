from app import app
from flask import render_template, redirect, url_for

sections = ['about', 'branches', 'contact', 'news', 'management']


@app.route('/')
def index():
    return render_template(
        'index.html')


@app.route('/<sect>')
def redirect_base(sect):
    if sect not in sections:
        return redirect(url_for('index'))


@app.route('/news')
def news():
    return render_template(
        'news.html'
    )


@app.route('/management')
def management():
    return render_template(
        'management.html'
    )


@app.route('/about')
def about():
    return render_template(
        'about.html'
    )


@app.route('/contact')
def contact():
    return render_template(
        'contact.html'
    )


@app.route('/branches')
def branches():
    return render_template(
        'branches.html'
    )


@app.route('/branches/London')
@app.route('/branches/london')
def london():
    return render_template(
        'london.html'
    )


@app.route('/branches/paris')
@app.route('/branches/Paris')
def paris():
    return render_template(
        'paris.html'
    )


@app.route('/<section>/<_>')
def redirect_to_section(section, _):
    return redirect(url_for(section))
