#!/usr/bin/python3
"""
Containing the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User

models = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "State": State, "User": User}


class FileStorage:
    """ Serialize and deserializes instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """return the dictionary __objects"""
        if cls is not None:
            _dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    _dict[key] = value
            return _dict
        return self.__objects

    def new(self, obj):
        """set in __objects """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serialize the __objects to the JSON file (path: __file_path)"""
        obj = {}
        for key in self.__objects:
            obj[key] = self.__objects[key].to_dict(True)
        with open(self.__file_path, 'w') as f:
            json.dump(obj, f)

    def get(self, cls, id):
        """A method to retrieve one object
        None if not found
        """
        if type(cls) is str:
            cls = models.get(cls)
        if cls is None:
            return None
        for item in self.__objects.values():
            if item.__class__ == cls and item.id == id:
                return item

    def count(self, cls=None):
        """ count the number of objects in storage
        """
        if type(cls) is str:
            cls = models.get(cls)
        if cls is None:
            return len(self.all())
        return len(self.all(cls))

    def reload(self):
        """deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = models[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete object from __objects"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """deserializing the JSON file to objects"""
        self.reload()
