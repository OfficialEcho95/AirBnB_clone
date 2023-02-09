#!/usr/bin/env python3
"""File storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a json file and deserializes json file
    to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets ___objects with key"""
        if not obj:
            return
        attr = obj.to_dict()
        key = attr['__class__'] + '.' + attr['id']
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to json file"""
        objs = {}
        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objs, f, indent=4)

    def reload(self):
        """deserializes the json file to __objects, only if the
        json file exists"""
        try:
            with open(self.__file_path, "r") as f:
                objs = json.loads(f.read())
                for key, obj in objs.items():
                    if key not in self.__objects:
                        name = obj['__class__']
                        base = eval(f"{name}(**obj)")
                        self.new(base)
        except Exception:
            pass
