#!/usr/bin/python3
""" Class BaseModel defines all common attributes/methods for other classes """
import uuid
from datetime import datetime

class BaseModel:
    """ Class for base model """

    def __init__(self):
        """ Initialization """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Str format for references """
        return (f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        """ Update with current date time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Dictionary containing all keys/values """
        dct = dict(self.__dict__)
        dct['_class_'] = self.__class__.__name__
        dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dct
