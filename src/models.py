from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

favorites_table = Table(
    'favorite',
    db.metadata,
    Column('id', db.Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False),
    Column('character_id', ForeignKey('character.id'), nullable=True),
    Column('location_id', ForeignKey('location.id'), nullable=True)
)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    fav_character: Mapped[list['Character']] = relationship(
        'Character',
        secondary = favorites_table,
        back_populates= 'fav_character_by'
    )

    fav_location: Mapped[list['Location']] = relationship(
        'Location',
        secondary= favorites_table,
        back_populates='fav_location_by'
    )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'fav_character': [char.serialize() for char in self.fav_character],
            'fav_location': [loc.serialize() for loc in self.fav_location]
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    img_char: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[str] = mapped_column(nullable=False)

    fav_character_by: Mapped[list['User']] = relationship(
        'User',
        secondary = favorites_table,
        back_populates= 'fav_character'
    )

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'img_char': self.img_char,
            'age': self.age
        }

class Location(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    img_location: Mapped[str] = mapped_column(nullable=True)
    use_location: Mapped[str] = mapped_column(nullable=False)

    fav_location_by: Mapped[list['User']] = relationship(
        'User',
        secondary= favorites_table,
        back_populates='fav_location'
    )

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'img_location': self.img_location,
            'use_location': self.use_location
        }