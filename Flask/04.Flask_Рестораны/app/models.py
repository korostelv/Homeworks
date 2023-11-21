from app import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    specialization = db.Column(db.String(64), index=True, unique=False)
    address = db.Column(db.String(128), index=True, unique=False)
    website = db.Column(db.String(64), index=True, unique=False)
    phone = db.Column(db.String(12), index=True, unique=False)

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)
