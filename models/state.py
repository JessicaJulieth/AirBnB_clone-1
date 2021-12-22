#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(60), nullable=False)
    cities = relationship("City", backref="states", cascade="all")

    @property
    def cities(self):
        """returns the list of City instances with state_id
        equals to the current State.id"""
        from models import storage
        from models.city import City

        tmp = []  # will return this array
        dct = storage.all(City)
        for val in dct.values():
            if val.state_id == self.id:
                tmp.append(val)
        return tmp
