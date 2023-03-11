#!/usr/bin/python3
'''
Holds BaseModel class
'''
import uuid
from datetime import datetime

fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    '''
    Representation of a BaseModel instance
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new BaseModel instance
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = datetime.strptime(v, fmt)
                if k != '__class__':
                    self.__dict__[k] = v

    def __str__(self):
        '''
        String representation of a BaseModel instance
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        '''
        Save the current instance
        '''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        '''
        Purified dictionary representation of the instance
        '''
        the_dict = {}
        for k, v in self.__dict__.items():
            if k in ['created_at', 'updated_at']:
                v = v.isoformat()
            the_dict[k] = v
        the_dict['__class__'] = self.__class__.__name__
        return the_dict
