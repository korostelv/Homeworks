from app.models import Restaurant
from app import app,db
rest = Restaurant.query.all()
print(rest)