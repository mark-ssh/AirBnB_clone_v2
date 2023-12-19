#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import environ


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class with args and kwargs
        """
        super().__init__(*args, **kwargs)
