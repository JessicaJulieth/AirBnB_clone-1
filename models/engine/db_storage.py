#!/usr/bin/python3
"""DBStorage storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class DBStorage():
    """New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializing the sqlalchemy engine"""
        usr = getenv("HBNB_MYSQL_USER")
        pswrd = getenv("HBNB_MYSQL_PWD")
        hst = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")  # Database

        self.engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                usr, pswrd, hst, db), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.save()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
