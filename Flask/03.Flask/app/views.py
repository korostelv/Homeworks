from app import  app
from flask import  render_template


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/fr')
def fr():
    return render_template('/fr.html')


@app.route('/de')
def de():
    return render_template('/de.html')


@app.route('/es')
def es():
    return render_template('/es.html')
