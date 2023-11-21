from app_weekday import app
from flask import render_template
from datetime import datetime

weekday = datetime.now().weekday()


@app.route('/')
def index():
    return render_template('/index.html', weekday=weekday)
