from app_headphones import  app
from flask import  render_template

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template(
#         'index.html')


@app.route('/?model=<string:model>')
def model(model):
    return render_template(f'{model}.html')


@app.errorhandler(404)
def error_page(error):
    return 'Данной модели не найдено'