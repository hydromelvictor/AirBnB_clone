#!/usr/bin/python3
"""serialize and deserialize"""

import json
from os import path
import models

class FileStorage:
    """class for save file in json format"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return all dictionnary of instaces"""
        return self.__objects
    
    def new(self, obj):
        """new instances add in dictionnary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """serialization"""
        json_obj = {}
        for key, obj in self.__objects.items():
            json_obj[key] = obj.to_dict()
            
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_obj, file)
    
    def reload(self):
        """deserialization"""
        if path.isfile(self.__file_path):
            to_obj = {}
            with open(self.__file_path, "r", encoding="utf-8") as file:
                to_obj = json.load(file)
                
            for key, dic in to_obj.items():
                self.__objects[key] = models.dic["__class__"](**dic)
