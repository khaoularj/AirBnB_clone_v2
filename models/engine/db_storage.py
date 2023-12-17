#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import Base
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        classes = [State, City, User, Place, Review, Amenity]
        objects = []
        if cls is None:
            for item in classes:
                objects.extend(self.__session.query(item).all())
        else:
            objects = self.__session.query(cls)
        dict_ = {}
        for obj in objects:
            dict_[f"{type(obj).__name__}.{obj.id}"] = obj
        return dict_

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete()

    def reload(self):
        """create all tables in the database
        create the current database session (self.__session) from the engine"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
