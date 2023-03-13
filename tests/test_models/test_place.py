#!/usr/bin/python3
'''
Unittest for Place class
'''
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.amenity import Amenity
import uuid
from datetime import datetime
import os


class TestPlace(unittest.TestCase):
    '''
    Define test cases for Place class
    '''
    def setUp(self):
        '''
        Prepare all tests
        '''
        self.time = "%Y-%m-%dT%H:%M:%S.%f"
        self.s1 = State(name="Senegal")
        self.s1.save()
        self.c1 = City(name="Dakar", state_id=self.s1.id)
        self.c1.save()
        self.u1 = User(first_name="Betty", last_name="Holberton",
                       email="airbnb2@mail.com", password="root")
        self.u1.save()
        self.a1 = Amenity(name='fitness')
        self.a1.save()
        self.p2 = Place(user_id=self.u1.id, city_id=self.c1.id,
                        name="King Fadh Palace", description="Hotel 5 stars",
                        number_rooms=50, number_bathrooms=50, max_guest=100,
                        price_by_night=168, latitude=14.55, longitude=14.78,
                        amenity_ids=[self.a1.id])
        self.p2.save()
        self.p1 = Place()
        self.p1.save()

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
        self.assertEqual('Place', self.p1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at',
                                      'city_id', 'user_id', 'name',
                                      'description', 'number_rooms',
                                      'number_bathrooms', 'max_guest',
                                      'price_by_night', 'latitude',
                                      'longitude', 'amenity_ids']
        for att in native_instance_attributes:
            self.assertIn(att, self.p1.__dir__())

        place_attributes = ['city_id', 'user_id', 'name',
                            'description', 'number_rooms',
                            'number_bathrooms', 'max_guest',
                            'price_by_night', 'latitude',
                            'longitude', 'amenity_ids']
        for att in place_attributes:
            self.assertNotIn(att, self.p1.__dict__)

        for att in place_attributes:
            self.assertIn(att, self.p2.__dict__)

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.p1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.p1.id) == str)
        self.assertTrue(str(uuid.UUID(self.p1.id)) == self.p1.id)
        self.assertTrue(str(uuid.UUID(self.p2.id)) == self.p2.id)
        self.assertEqual(str(uuid.UUID(self.p2.city_id)), self.p2.city_id)
        self.assertEqual(str(uuid.UUID(self.p2.user_id)), self.p2.user_id)

        self.p1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.p1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.p1.__dict__)
            self.assertIsInstance(self.p1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.p1.updated_at
        self.p1.save()
        self.assertLess(updated_at_before_save, self.p1.updated_at)

    def test_to_dict(self):
        d = self.p1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.p1.__dict__[att])

        d = self.p2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'description', 'number_rooms',
                               'number_bathrooms', 'max_guest',
                               'price_by_night', 'latitude',
                               'longitude', 'amenity_ids']
        for att in instance_attributes:
            self.assertIn(att, d)
