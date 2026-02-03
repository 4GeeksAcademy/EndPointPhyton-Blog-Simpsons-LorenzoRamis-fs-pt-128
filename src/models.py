from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

favorites_table = Table(
    'favorite',
    db.metadata,
    # Column('id', db.Integer, primary_key=True),
    Column('User_id', ForeignKey('user.id'), primary_key=True),
    Column('Character_id', ForeignKey('character.id'), primary_key=True),
    # Column('Location_id', ForeignKey('location.id'), primary_key=True)
)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=True)
    favorite: Mapped[list['Character']] = relationship(
        'Character',
        secondary = favorites_table,
        back_populates= 'fav_character_by'
    )

    # fav_location: Mapped[list['Location']] = relationship(
    #     'Location',
    #     secondary= favorites_table,
    #     back_populates='fav_location_by'
    # )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'age': self.age,
            'favorite': self.favorite,
            # 'fav_location': self.fav_location
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    img_char: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[str] = mapped_column(nullable=False)

    fav_character_by: Mapped[list['User']] = relationship(
        'User',
        secondary = favorites_table,
        back_populates= 'favorite'
    )

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'img_char': self.img_char,
            'age': self.age
        }

# class Location(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(120), nullable=False)
#     img_location: Mapped[str] = mapped_column(nullable=False)
#     use_location: Mapped[str] = mapped_column(nullable=False)

#     fav_location_by: Mapped[list['User']] = relationship(
#         'User',
#         secondary= favorites_table,
#         back_populates='fav_location'
#     )

#     def serialize(self):
#         return{
#             'id': self.id,
#             'name': self.name,
#             'img_location': self.img_location,
#             'use_location': self.use_location
#         }