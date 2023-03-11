#!/usr/bin/python3
'''
Unittest for BaseModel class
'''
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''
    Define test cases for BaseModel class
    '''
    def setUp(self):
        '''
        Prepare all tests
        '''
        self.time = "%Y-%m-%dT%H:%M:%S.%f"
        self.b1 = BaseModel()
        self.b2 = BaseModel(my_number=89, name='Holberton')

    def test_init(self):
        '''
        Testing initialization of a BaseModel instance
        '''
        self.assertEqual('BaseModel', self.b1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at']
        for att in native_instance_attributes:
            self.assertIn(att, self.b1.__dir__())

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.b1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.b1.id) == str)
        self.assertTrue(str(uuid.UUID(self.b1.id)) == self.b1.id)
        self.assertTrue(str(uuid.UUID(self.b2.id)) == self.b2.id)
        self.b1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.b1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.b1.__dict__)
            self.assertIsInstance(self.b1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.b1.updated_at
        self.b1.save()
        self.assertLess(updated_at_before_save, self.b1.updated_at)

    def test_to_dict(self):
        d = self.b1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.b1.__dict__[att])

        d = self.b2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'name', 'my_number']
        for att in instance_attributes:
            self.assertIn(att, d)
