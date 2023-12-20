#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class with args and kwargs
        """
        super().__init__(*args, **kwargs)
