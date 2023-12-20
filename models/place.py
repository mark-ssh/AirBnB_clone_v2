#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Table, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import environ
import models


if environ.get("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"), primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="delete", backref="place")
        amenities = relationship("Amenity", cascade="delete",
                                 back_populates="place_amenities",
                                 secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """attribute for FileStorage that returns list of Review instances"""
            stor = models.storage.all(Review).values()
            return ([a for a in stor if self.id == a.place_id])

        @property
        def amenities(self):
            """Getter attribute to retrieve associated amenities"""
            stor = models.storage.all(Amenity).values()
            return ([a for a in stor if a.id in self.amenity_ids])

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute that adds amenities to the list amenity_ids"""
            if isinstance(obj, models.Amenity):
                amenity_ids.append(obj.id)
