#!/usr/bin/python3
'''
Unittest for Amenity class
'''
import models
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid
from datetime import datetime
import os


class TestAmenity(unittest.TestCase):
    '''
    Define test cases for Amenity class
    '''
    def setUp(self):
        '''
        Prepare all tests
        '''
        self.time = "%Y-%m-%dT%H:%M:%S.%f"
        self.a1 = Amenity()
        self.a2 = Amenity(name="wifi")

    def tearDown(self):
        '''
        Clean up
        '''
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_init(self):
        '''
        Testing initialization of a Amenity instance
        '''
        self.assertEqual('Amenity', self.a1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at',
                                      'name']
        for att in native_instance_attributes:
            self.assertIn(att, self.a1.__dir__())

        amenity_attributes = ['name']
        for att in amenity_attributes:
            self.assertNotIn(att, self.a1.__dict__)

        for att in amenity_attributes:
            self.assertIn(att, self.a2.__dict__)

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.a1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.a1.id) == str)
        self.assertTrue(str(uuid.UUID(self.a1.id)) == self.a1.id)
        self.assertTrue(str(uuid.UUID(self.a2.id)) == self.a2.id)

        self.a1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.a1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.a1.__dict__)
            self.assertIsInstance(self.a1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.a1.updated_at
        self.a1.save()
        self.assertLess(updated_at_before_save, self.a1.updated_at)
        all_objs = models.storage.all()
        key = self.a1.to_dict()['__class__'] + '.' + self.a1.id
        self.assertIn(key, all_objs)
        obj = all_objs[key]
        self.assertEqual(self.a1.updated_at, obj.updated_at)

    def test_to_dict(self):
        d = self.a1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.a1.__dict__[att])

        d = self.a2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'name']
        for att in instance_attributes:
            self.assertIn(att, d)
