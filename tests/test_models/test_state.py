#!/usr/bin/python3
'''
Unittest for State class
'''
import unittest
from models.base_model import BaseModel
from models.state import State
import uuid
from datetime import datetime
import os


class TestState(unittest.TestCase):
    '''
    Define test cases for State class
    '''
    def setUp(self):
        '''
        Prepare all tests
        '''
        self.time = "%Y-%m-%dT%H:%M:%S.%f"
        self.s1 = State()
        self.s2 = State(name="Holberton")

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
        self.assertEqual('State', self.s1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at', 'name']
        for att in native_instance_attributes:
            self.assertIn(att, self.s1.__dir__())

        state_attributes = ['name']
        for att in state_attributes:
            self.assertNotIn(att, self.s1.__dict__)

        for att in state_attributes:
            self.assertIn(att, self.s2.__dict__)

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.s1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.s1.id) == str)
        self.assertTrue(str(uuid.UUID(self.s1.id)) == self.s1.id)
        self.assertTrue(str(uuid.UUID(self.s2.id)) == self.s2.id)

        self.s1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.s1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.s1.__dict__)
            self.assertIsInstance(self.s1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.s1.updated_at
        self.s1.save()
        self.assertLess(updated_at_before_save, self.s1.updated_at)

    def test_to_dict(self):
        d = self.s1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.s1.__dict__[att])

        d = self.s2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'name']
        for att in instance_attributes:
            self.assertIn(att, d)
