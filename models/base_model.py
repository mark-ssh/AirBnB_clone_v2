#!/usr/bin/python3
"""This module defines a base class for all models"""
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import environ


if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The base class for all storage objects in this project"""

    if environ.get("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(), default=datetime.utcnow(),
                            nullable=False)
        updated_at = Column(DateTime(), default=datetime.utcnow(),
                            nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(kwargs) > 0:
            for k in kwargs.keys():
                if k in ('created_at', 'updated_at'):
                    setattr(self, k,
                            datetime.strptime(kwargs[k],
                                              '%Y-%m-%dT%H:%M:%S.%f'))
                elif k == '__class__':
                    continue
                else:
                    setattr(self, k, kwargs[k])
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("_sa_instance_state" in dupe):
            dupe.pop('_sa_instance_state', None)
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe

    def delete(self):
        """deleting current instance"""
        models.storage.__objects.pop(f"{type(self).__name__}.{self.id}")
