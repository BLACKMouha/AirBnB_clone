#!usr/bin/python3
'''
Holds User class
'''
import models
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Represents a User instance
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
