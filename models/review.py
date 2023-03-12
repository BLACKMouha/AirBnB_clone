#!/usr/bin/python3
'''
Holds Review class
'''
import models
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Representation of Review
    '''
    place_id = ''
    user_id = ''
    text = ''
