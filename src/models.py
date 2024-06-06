from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    homeworld = db.Column(db.String(120))
    planet_residing = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld,
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120))
    people_residing = db.relationship('Person', backref='resident', lazy='dynamic')
    
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "people_residing": self.people_residing,
            # do not serialize the password, its a security breach
        }
    