#!/usr/bin/python3
'''
Unittest for User class
'''
import unittest
from models.base_model import BaseModel
from models.user import User
import uuid
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    '''
    Define test cases for User class
    '''
    def setUp(self):
        '''
        Prepare all tests
        '''
        self.time = "%Y-%m-%dT%H:%M:%S.%f"
        self.u1 = User()
        self.u2 = User(first_name="Betty", last_name='Holberton',
                       email='airbnb@mail.com', password="root")

    def tearDown(self):
        '''
        Clean up
        '''
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_init(self):
        '''
        Testing initialization of a User instance
        '''
        self.assertEqual('User', self.u1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at',
                                      'email', 'password', 'last_name',
                                      'first_name']
        for att in native_instance_attributes:
            self.assertIn(att, self.u1.__dir__())

        user_attributes = ['first_name', 'last_name', 'email',
                                      'password']
        for att in user_attributes:
            self.assertNotIn(att, self.u1.__dict__)

        for att in user_attributes:
            self.assertIn(att, self.u2.__dict__)

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.u1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.u1.id) == str)
        self.assertTrue(str(uuid.UUID(self.u1.id)) == self.u1.id)
        self.assertTrue(str(uuid.UUID(self.u2.id)) == self.u2.id)

        self.u1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.u1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.u1.__dict__)
            self.assertIsInstance(self.u1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.u1.updated_at
        self.u1.save()
        self.assertLess(updated_at_before_save, self.u1.updated_at)

    def test_to_dict(self):
        d = self.u1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.u1.__dict__[att])

        d = self.u2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'first_name', 'last_name', 'email', 'password']
        for att in instance_attributes:
            self.assertIn(att, d)
