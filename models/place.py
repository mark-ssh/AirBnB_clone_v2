#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import environ

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))


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
        reviews = relationship("Review", cascade="all, delete", 
                               backref="place")
        amenities = relationship("Amenity",
                                secondary='place_amenity',
                                viewonly=False,
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
    
    def __init__(self, *args, **kwargs):
        """Initializes the Place class"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """attribute for Filestorage that returns list of Review instances"""
        values_review = models.storage.all("Review").values()
        review_list = []
        for review in values_review:
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """attribute for Filestorage that returns list of Amenity instances"""
            values_amenity = models.storage.all("Amenity").values()
            amenity_list = []
            for amenity in values_amenity:
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
