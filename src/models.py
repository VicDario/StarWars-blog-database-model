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


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')