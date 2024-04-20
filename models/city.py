#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """method to initialise city"""
        super().__init__(*args, **kwargs)
