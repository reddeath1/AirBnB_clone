#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

modelss = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "State": State, "User": User}


class Command(cmd.Cmd):
    """ HBNB console """
    prompt = '(hbnb) '

    def _EOF(self, arg):
        """ Exit console """
        return True

    def clear(self):
        """ overwriting the clearing method """
        return False

    def quit(self, arg):
        """ command to exit the program """
        return True

    def key_value_parser(self, args):
        """ create a dictionary from a list of string """
        _dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                _dict[key] = value
        return _dict

    def create(self, arg):
        """ Create a new instance of a class """
        args = arg.split()
        if len(args) == 0:
            print("class name missing")
            return False
        if args[0] in modelss:
            _dict = self.key_value_parser(args[1:])
            instance = modelss[args[0]](**_dict)
        else:
            print("class doesn't exist")
            return False
        print(instance.id)
        instance.save()

    def show(self, arg):
        """ Print the instance as a string based on the class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("class name missing")
            return False
        if args[0] in modelss:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("no instance found")
            else:
                print("instance id missing")
        else:
            print("class doesn't exist")

    def destroy(self, arg):
        """ Delete the instance based on the class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in modelss:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("no instance found")
            else:
                print("instance id missing")
        else:
            print("class doesn't exist")

    def all(self, arg):
        """ Print string representation of the instance """
        args = shlex.split(arg)
        _list = []
        if len(args) == 0:
            _dict = models.storage.all()
        elif args[0] in modelss:
            _dict = models.storage.all(modelss[args[0]])
        else:
            print(" class doesn't exist ")
            return False
        for key in _dict:
            _list.append(str(_dict[key]))
        print("[", end="")
        print(", ".join(_list), end="")
        print("]")

    def update(self, arg):
        """ Update the instance based on the class name """

        args = shlex.split(arg)

        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]

        floats = ["latitude", "longitude"]

        if len(args) == 0:
            print(" class name missing ")
        elif args[0] in modelss:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print(" Value missing ")
                    else:
                        print(" Attribute name missing ")
                else:
                    print(" No instance found ")
            else:
                print(" instance id missing ")
        else:
            print(" class doesn't exist ")

if __name__ == '__main__':
    Command().cmdloop()
