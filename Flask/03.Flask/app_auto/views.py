from app_auto import  app
from flask import  render_template,url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/toyota')
def toyota():
    return render_template('/toyota.html')


@app.route('/honda')
def honda():
    return render_template('/honda.html')

@app.route('/renault')
def renault():
    return render_template('/renault.html')


