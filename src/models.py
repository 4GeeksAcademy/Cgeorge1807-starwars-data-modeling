import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

# python src/models.py

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    id_planet = Column(Integer, ForeignKey('planets.id'))
    planets = relationship("Planets")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    users = relationship("User", back_populates="planets")

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    skin_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship("Planets")    

class Favorites(Base):
    __tablename__ = 'favorites'
    id_favorites = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship("User") 
    id_people = Column(Integer, ForeignKey('people.id'))
    people = relationship("People")     
    id_planets = Column(Integer, ForeignKey('planets.id'))
    planets = relationship("Planets")

    
    
def to_dict(self):
    return {}

# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
