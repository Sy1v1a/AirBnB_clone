#!/usr/bin/python3
"""Write a class BaseModel"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Class Basemodel"""
    def __init__(self, *args, **kwargs):
        """Function for Base model"""
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Instance update"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary of instance"""
        ins_dict = self.__dict__.copy()
        ins_dict['__class__'] = self.__class__.__name__
        ins_dict['created_at'] = self.created_at.isoformat()
        ins_dict['updated_at'] = self.updated_at.isoformat()
        return ins_dict
