#!/usr/bin/python3
'''
Unit tests for FileStorage class
'''
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    '''
    Define unit test cases for FileStorage class
    '''

    def setUp(self):
        self.file_path = 'file.json'
        self.objects = {}
        self.storage = FileStorage()
        self.b1 = BaseModel(name='John', age=57)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def init(self):
        membs = ['_FileStorage__file_path', '_FileStorage__objects',
                      'save', 'new', 'save', 'reload']
        for memb in membs:
            assertIn(memb, self.storage.__dir__())

    def test_all(self):
        a = self.storage.all()
        assertEqual(type(a), dict)
        assertEqual(
