#!/usr/bin/python3
'''
Holds FileStorage class
'''
from models.base_model import BaseModel
from models.user import User

classes = {'BaseModel': BaseModel,
           'User': User}


class FileStorage:
    '''
    Representation of FileStorage
    '''

    def __init__(self):
        '''
        Initializes an instance
        '''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''
        Returns the dictionary of instances
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in `__objects` the `obj` with the key `<obj class name>.id`
        '''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        '''
        Serializes `__objects` to the JSON file __file_path
        '''
        objs = {}
        for k, v in self.__objects.items():
            objs[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            from json import dump
            dump(objs, f)

    def reload(self):
        '''
        Deserializes `__file_path` to `__objects`
        '''
        try:
            with open(self.__file_path, 'r') as f:
                from json import load
                objs = load(f)
                for k, v in objs.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        except:
            pass
