import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(100))
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_favorite = Column(Integer, nullable=False)
    type_favorite = Column(String(20), nullable=False)
    name = Column(String(100), nullable=False)
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    climate = Column(String(40))
    terrain = Column(String(40))
    gravity = Column(String(20))
    surface_water = Column(Integer)

class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    gender = Column(String(6))
    hair_color = Column(String(15))
    eye_color = Column(String(15))
    mass = Column(String(4))
    height = Column(String(4))
    home_world_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Species(Base):
    __tablename__ = 'specie'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    classification = Column(String(50), nullable=False)
    designation = Column(String(50), nullable=False)
    average_height = Column(Integer, nullable=False)
    average_lifespan = Column(Integer, nullable=False)
    hair_colors = Column(String(100), nullable=False)
    skin_colors = Column(String(100), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Starships(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    model = Column(String(100), nullable=False)
    starship_class = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(String(30), nullable=False)
    hyperdrive_rating = Column(String(10), nullable=False)
    MGLT = Column(String(5), nullable=False)
    cargo_capacity = Column(String(30), nullable=False)
    consumables = Column(String(20), nullable=False)
    pilots = Column(Integer, ForeignKey('character.id'))
    character = relationship(Characters, backref="starchip")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')