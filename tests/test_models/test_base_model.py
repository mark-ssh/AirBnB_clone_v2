#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.__init__ import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from console import HBNBCommand

class test_basemodel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        """ the set up method of the test class"""
        self.model1 = BaseModel()
        self.cli = HBNBCommand()

        test_args = {'created_at': datetime(2017, 2, 11, 2, 6, 55, 258849),
                     'updated_at': datetime(2017, 2, 11, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def tearDown(self):
        """the teardown method of the ctest class"""
        self.cli.do_destroy("BaseModel 46458416-e5d5-4985-aa48-a2b369d03d2a")

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         '46458416-e5d5-4985-aa48-a2b369d03d2a')
        self.assertEqual(self.model2.created_at,
                         datetime(2017, 2, 11, 2, 6, 55, 258849))

    def test_save(self):
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

        self.cli.do_destroy("BaseModel " + self.model1.id)

    def test_to_dict(self):
        """ testing the to_dict method"""
        f_json = self.model2.to_json()
        self.assertNotEqual(self.model2.__dict__, f_json)
        self.assertNotIsInstance(f_json["created_at"], datetime)
        self.assertNotIsInstance(f_json["updated_at"], datetime)
        self.assertEqual(f_json["created_at"], '2017-02-11 02:06:55.258849')
        self.assertTrue(hasattr(f_json, "__class__"))
        self.assertEqual(f_json["__class__"], "BaseModel")

if __name__ == "__main__":
    unittest.main()