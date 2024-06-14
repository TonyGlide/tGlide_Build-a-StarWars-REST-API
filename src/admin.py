import os
from flask_admin import Admin
from models import db, Person, Planet, Users, FavoritePeople, FavoritePlanets
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
   
    admin.add_view(ModelView(Person, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(FavoritePeople, db.session))
    admin.add_view(ModelView(FavoritePlanets, db.session))


   