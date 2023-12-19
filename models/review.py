#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ


class Review(BaseModel, Base):
    """ Review class to represent user review"""
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), 
                      nullable=False)
        place_id = Column(String(60), 
                          ForeignKey("places.id"), 
                          nullable=False)
        user_id = Column(String(60), 
                         ForeignKey("users.id"), 
                         nullable=False)
        place = relationship("Place",
                             back_populates="reviews")

    else:
        text = ""
        place_id = ""
        user_id = ""
