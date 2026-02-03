import os
from flask_admin import Admin
from models import db, User, Character, Location
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class UserAdmin(ModelView):
        form_columns =[
            'email', 
            'password', 
            'fav_character', 
            'fav_location']
        
        column_list = ('id', 'email', 'fav_character', 'fav_location')
    
    class LocationAdmin(ModelView):
        form_columns= [
            'name',
            'img_location',
            'use_location'
        ]

    class CharacterAdmin(ModelView):
        form_columns= [
            'name',
            'img_char',
            'age'
        ]
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(LocationAdmin(Location, db.session))
    admin.add_view(CharacterAdmin(Character, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))