#!/usr/bin/python3
'''
Holds BaseModel class
'''
import uuid
from datetime import datetime
import models

fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    '''
    Representation of a BaseModel instance
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new BaseModel instance
        '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        v = datetime.strptime(v, fmt)
                    setattr(self, k, v)

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
        models.storage.save()

    def to_dict(self):
        '''
        Purified dictionary representation of the instance
        '''
        the_dict = self.__dict__.copy()
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()
        the_dict['__class__'] = self.__class__.__name__
        return the_dict
