#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False ) #Aquí tienen un error de sintáxis en el ForeignKey, debe ir ForeignKey('users.id')
    #No sé porqué presenta problema cuando se pone al final, ni idea 🙄
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False) # ahh bueno, y acá lleva otro ForeignKey
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0) #Aquí se usa un type de sqlalchemy que es Integer
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(float, nullable=False)
    longitude = Column(float, nullable=False)
    amenity_ids = []

    # Para que la consola funcione como necesitamos, que funcione con mysql, primero necesitamos declarar las variables de entorno en este pc
    # Sino el va a seguir cogiendo el FileStorage, es decir el JSON

    """
    export HBNB_MYSQL_USER='hbnb_dev';
    export HBNB_MYSQL_PWD='hbnb_dev_pwd';
    export HBNB_MYSQL_HOST='localhost';
    export HBNB_MYSQL_DB='hbnb_dev_db';
    export HBNB_ENV='db';
    export HBNB_TYPE_STORAGE='db'
    Posiblemente esto les sirva en un futuro, así que lo voy a dejar aquí
    """