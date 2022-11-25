#!/usr/bin/python3
"""Test file for BaseModel Class"""

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class Test_Storage(unittest.TestCase):
    """ Test for file storage """

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        cls.storage = BaseModel()
        cls.storage.name = "Konany"
        cls.storage.my_number = 15

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.storage
        try:
            os.remove("file.json")
        except:
            pass

    def test_objects(self):
        """ Test for attributes """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_docstring(self):
        """ Test for docstring for each method into the class """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all_method(self):
        """ Check for all method """
        new = FileStorage()
        objs = new.all()
        self.assertEqual(type(objs), dict)
        self.assertIsNotNone(objs)
        self.assertIs(objs, new._FileStorage__objects)
        key = self.storage.__class__.__name__ + "." + self.storage.id
        obj_to = objs[key]
        output = "[BaseModel] ({}) {}".format(self.storage.id,
                                              self.storage.__dict__)
        self.assertEqual(output, str(obj_to))

    def test_change_length(self):
        """
        Create an object and save it and checks the new length for dictionary
        """
        new = FileStorage()
        len1 = len(new.all())
        second = BaseModel()
        new.save()
        new.reload()
        len2 = len(new.all())
        self.assertEqual(len1, len2 - 1)

    def test_new_method(self):
        """ Test for new method and expected output"""
        new = FileStorage()
        _dict_objs = new.all()
        state = State()
        state.name = "Washington D.C."
        new.new(state)
        self.assertEqual(type(_dict_objs), dict)
        self.assertIsNotNone(_dict_objs)
        self.assertIs(_dict_objs, new._FileStorage__objects)
        key = state.__class__.__name__ + "." + state.id
        self.assertIsNotNone(_dict_objs[key])
        obj_to = _dict_objs[key]
        output = "[State] ({}) {}".format(state.id,
                                          state.__dict__)
        self.assertEqual(output, str(obj_to))

    def test_save_method(self):
        """ Test for save method """
        _dict = self.storage.to_dict()
        new_key = _dict['__class__'] + "." + _dict['id']
        new = FileStorage()
        new.save()
        with open("file.json", 'r') as fd:
            file_r = json.load(fd)
        new = file_r[new_key]
        for key in new:
            self.assertEqual(_dict[key], new[key])

    def test_save(self):
        """ Test if changes was saved """
        Base = BaseModel()
        Base.save()
        self.assertNotEqual(Base.created_at, Base.updated_at)


if __name__ == '__main__':
    unittest.main()
