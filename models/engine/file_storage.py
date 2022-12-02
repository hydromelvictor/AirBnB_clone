#!/usr/bin/python3
"""serialize and deserialize"""

import json
from os import path
import os
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

objs = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review}


class FileStorage:
    """class for save file in json format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets obj in __objects"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ serializes to JSON """
        dummy_dict = {}
        for key, value in self.__objects.items():
            dummy_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dummy_dict, f)

    def reload(self):
        """ deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_objs = json.load(f)
                for key, value in json_objs.items():
                    inst = self.objs[value['__class__']](**value)
                    self.__objects[key] = inst
        except FileNotFoundError:
            pass
