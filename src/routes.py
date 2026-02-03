from flask import Blueprint, jsonify
from models import db, User, Character
from sqlalchemy import select


api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = db.session.execute(select(User)).scalars().all()
    responde = [user.serialize() for user in users]
    return jsonify(responde)

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.session.get(User, id)
    print(user.serialize())
    return jsonify(user.serialize())

@api.route('/characters', methods=['GET'])
def get_characters():
    characters = db.session.execute(select(Character)).scalars().all()
    responde = [character.serialize() for character in characters]
    return jsonify(responde)

@api.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = db.session.get(Character, id)
    print(character.serialize())
    return jsonify(character.serialize())

@api.route('/locations', methods=['GET'])
def get_locations():
    locations = db.session.execute(select(Location)).scalars().all()
    responde = [location.serialize() for location in locations]
    return jsonify(responde)

@api.route('/locations/<int:id>', methods=['GET'])
def get_location(id):
    location = db.session.get(Location, id)
    print(location.serialize())
    return jsonify(location.serialize())