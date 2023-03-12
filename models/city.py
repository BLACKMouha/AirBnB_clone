#!/usr/bin/python3
'''
Holds City class
'''
import models
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Representation of City
    '''
    state_id = ''
    name = ''
