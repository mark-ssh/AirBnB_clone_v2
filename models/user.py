#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv

class User(BaseModel, Base):
    """
    Represents users themselves, with personal information
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", 
                              cascade="delete", 
                              backref="user")
        reviews = relationship("Review", 
                               cascade="delete",
                               backref="user")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = ""

    def __init__(self, *args, **kwargs):
        """initializing"""
        super().__init__(*args, **kwargs)
