#!/usr/bin/python3
"""
A base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """update the public instance updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary representation of the instance"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        if not isinstance(my_dict["created_at"], str):
            my_dict["created_at"] = my_dict["created_at"].isoformat()
        if not isinstance(my_dict["updated_at"], str):
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

    def __str__(self):
        """Returns the string representation of an instance"""
        my_class = self.__class__.__name__
        return "[{}] ({}) {}".format(my_class,  self.id, self.__dict__)
