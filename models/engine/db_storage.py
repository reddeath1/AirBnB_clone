#!/usr/bin/python3
"""
class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

modelss = {"Amenity": Amenity, "City": City,
           "Place": Place, "State": State, "User": User}


class DBStorage:
    """ MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """init to Instantiate a Database storage object"""
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST')
        MYSQL_DB = getenv('MYSQL_DB')
        ENV = getenv('_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query the current database session"""
        _dict = {}
        for clss in modelss:
            if cls is None or cls is modelss[clss] or cls is clss:
                objs = self.__session.query(modelss[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    _dict[key] = obj
        return (_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """save all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session object"""
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """A method to retrieve one object
        :return None if not found
        """
        if type(cls) == str:
            cls = modelss.get(cls)
        if cls is None:
            return None
        return self.__session.query(cls).filter(cls.id == id).first()

    def count(self, cls=None):
        """A method to count the number of objects in storage
        :Return the number of objects in storage matching the given class name
        """
        if type(cls) is str:
            cls = modelss.get(cls)
        if cls is None:
            return len(self.all())
        return len(self.all(cls))

    def reload(self):
        """reload the data from the databases """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """remove method on the private session attribute"""
        self.__session.remove()
