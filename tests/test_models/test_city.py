#!/usr/bin/python3
'''
Unittest for City class
'''
import models
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
import uuid
from datetime import datetime
import os


class TestCity(unittest.TestCase):
    '''
    Define test cases for City class
    '''
    def setUp(self):
        '''
        Prepare all tests
        '''
        self.time = "%Y-%m-%dT%H:%M:%S.%f"
        self.s1 = State()
        self.c1 = City()
        self.c2 = State(state_id=self.s1.id, name="MyCity")

    def tearDown(self):
        '''
        Clean up
        '''
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_init(self):
        '''
        Testing initialization of a BaseModel instance
        '''
        self.assertEqual('City', self.c1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at',
                                      'state_id', 'name']
        for att in native_instance_attributes:
            self.assertIn(att, self.c1.__dir__())

        city_attributes = ['state_id', 'name']
        for att in city_attributes:
            self.assertNotIn(att, self.c1.__dict__)

        for att in city_attributes:
            self.assertIn(att, self.c2.__dict__)

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.c1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.c1.id) == str)
        self.assertTrue(str(uuid.UUID(self.c1.id)) == self.c1.id)
        self.assertTrue(str(uuid.UUID(self.c2.id)) == self.c2.id)
        self.assertEqual(str(uuid.UUID(self.c2.state_id)), self.c2.state_id)

        self.c1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.c1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.c1.__dict__)
            self.assertIsInstance(self.c1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.c1.updated_at
        self.c1.save()
        self.assertLess(updated_at_before_save, self.c1.updated_at)

    def test_to_dict(self):
        d = self.c1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.c1.__dict__[att])

        d = self.c2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'state_id']
        for att in instance_attributes:
            self.assertIn(att, d)
