from flask import Blueprint, jsonify, request
from models import db, User, Character, Location
from sqlalchemy import select


api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = db.session.execute(select(User)).scalars().all()
    responde = [user.serialize() for user in users]
    return jsonify(responde), 200

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.session.get(User, id)
    return jsonify(user.serialize()), 200

@api.route('/characters', methods=['GET'])
def get_characters():
    characters = db.session.execute(select(Character)).scalars().all()
    responde = [character.serialize() for character in characters]
    return jsonify(responde), 200

@api.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = db.session.get(Character, id)
    return jsonify(character.serialize()), 200

@api.route('/locations', methods=['GET'])
def get_locations():
    locations = db.session.execute(select(Location)).scalars().all()
    responde = [location.serialize() for location in locations]
    return jsonify(responde), 200

@api.route('/locations/<int:id>', methods=['GET'])
def get_location(id):
    location = db.session.get(Location, id)
    return jsonify(location.serialize()), 200

@api.route('/users/<int:user_id>/favorite/locations/<int:location_id>', methods=['POST'])
def add_location_favorite(user_id, location_id):
    user = db.session.get(User, user_id)
    location = db.session.get(Location, location_id)

    if user is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404
    if location is None:
        return jsonify({"msg": "Localización no encontrada"}), 404

    if location not in user.fav_location:
        user.fav_location.append(location)
        db.session.commit()
        return jsonify({"msg": "Localización añadida a favoritos"}), 200
    else:
        return jsonify({"msg": "Ya está en tu lista de favoritos"}), 400
    
@api.route('/users/<int:user_id>/favorite/locations/<int:location_id>', methods=['DELETE'])
def detele_location_favorite(user_id, location_id):
    user = db.session.get(User, user_id)
    location = db.session.get(Location, location_id)

    if user is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404
    if location is None:
        return jsonify({"msg": "Localización no encontrada"}), 404

    if location in user.fav_location:
        user.fav_location.remove(location)
        db.session.commit()
        return jsonify({"msg": "Localización eliminada de favoritos"}), 200
    else:
        return jsonify({"msg": "No está en tu lista de favoritos"}), 400
    
@api.route('/users/<int:user_id>/favorite/characters/<int:character_id>', methods=['POST'])
def add_character_favorite(user_id, character_id):
    user = db.session.get(User, user_id)
    character = db.session.get(Character, character_id)

    if user is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404
    if character is None:
        return jsonify({"msg": "Personaje no encontrado"}), 404

    if character not in user.fav_character:
        user.fav_character.append(character)
        db.session.commit()
        return jsonify({"msg": "Personaje añadido a favoritos"}), 200
    else:
        return jsonify({"msg": "Ya está en tu lista de favoritos"}), 400
    
@api.route('/users/<int:user_id>/favorite/characters/<int:character_id>', methods=['DELETE'])
def detele_character_favorite(user_id, character_id):
    user = db.session.get(User, user_id)
    character = db.session.get(Character, character_id)

    if user is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404
    if character is None:
        return jsonify({"msg": "Personaje no encontrada"}), 404

    if character in user.fav_character:
        user.fav_character.remove(character)
        db.session.commit()
        return jsonify({"msg": "Personaje eliminado de favoritos"}), 200
    else:
        return jsonify({"msg": "No está en tu lista de favoritos"}), 400