#!/usr/bin/python3
"""This module defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    setattr(self, k, globals()[v])
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representation of the BaseModel instance."""
        rdict = {
            key: value.isoformat() if isinstance(value, datetime) else value
            for key, value in self.__dict__.items()
        }
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.to_dict())

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a new instance from a dictionary representation."""
        class_name = obj_dict.pop("__class__", None)
        if class_name and class_name in globals():
            obj_class = globals()[class_name]
            return obj_class(**obj_dict)
        else:
            raise ValueError(f"Invalid class name: {class_name}")
