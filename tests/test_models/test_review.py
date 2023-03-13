#!/usr/bin/python3
'''
Unittest for Review class
'''
import models
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.city import City
from models.amenity import Amenity
import uuid
from datetime import datetime
import os


class TestReview(unittest.TestCase):
    '''
    Define test cases for Review class
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

        self.r1 = Review()
        self.r2 = Review(place_id=self.p2.id, user_id=self.u1.id,
                         text="Magnfique! I love this place")
        self.r1.save()
        self.r2.save()

    def tearDown(self):
        '''
        Clean up
        '''
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_init(self):
        '''
        Testing initialization of a Review instance
        '''
        self.assertEqual('Review', self.r1.__class__.__name__)
        native_instance_attributes = ['id', 'created_at', 'updated_at',
                                      'place_id', 'user_id', 'text']
        for att in native_instance_attributes:
            self.assertIn(att, self.r1.__dir__())

        review_attributes = ['place_id', 'user_id', 'text']
        for att in review_attributes:
            self.assertNotIn(att, self.r1.__dict__)

        for att in review_attributes:
            self.assertIn(att, self.r2.__dict__)

        native_public_instance_methods = ['save', 'to_dict']
        for meth in native_public_instance_methods:
            self.assertIn(meth, self.r1.__dir__())

    def test_id(self):
        '''
        All tests of id instance attribute
        '''
        self.assertTrue(type(self.r1.id) == str)
        self.assertTrue(str(uuid.UUID(self.r1.id)) == self.r1.id)
        self.assertTrue(str(uuid.UUID(self.r2.id)) == self.r2.id)
        self.assertEqual(str(uuid.UUID(self.r2.place_id)), self.r2.place_id)
        self.assertEqual(str(uuid.UUID(self.r2.user_id)), self.r2.user_id)

        self.r1.id = 'this is a bad UUID format'
        with self.assertRaises(
                ValueError,
                msg='badly formed hexadecimal UUID string') as e:
            uuid.UUID(self.r1.id)

    def test_date(self):
        '''
        Testing date in an instance
        '''
        dates = ['created_at', 'updated_at']
        for date in dates:
            self.assertIn(date, self.r1.__dict__)
            self.assertIsInstance(self.r1.__dict__[date], datetime)

    def test_save(self):
        '''
        Testing save public instance method
        '''
        updated_at_before_save = self.r1.updated_at
        self.r1.save()
        self.assertLess(updated_at_before_save, self.r1.updated_at)
        all_objs = models.storage.all()
        key = self.r1.to_dict()['__class__'] + '.' + self.r1.id
        self.assertIn(key, all_objs)
        obj = all_objs[key]
        self.assertEqual(self.r1.updated_at, obj.updated_at)

    def test_to_dict(self):
        d = self.r1.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn('__class__', d)
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for att in instance_attributes:
            self.assertIn(att, d)
            if att in ['created_at', 'updated_at']:
                self.assertIsInstance(att, str)
                self.assertEqual(datetime.strptime(d[att], self.time),
                                 self.r1.__dict__[att])

        d = self.r2.to_dict()
        instance_attributes = ['id', 'created_at', 'updated_at', '__class__',
                               'text', 'place_id', 'user_id']
        for att in instance_attributes:
            self.assertIn(att, d)
