"""Test file for BaseModel Class"""

import unittest

from models.base_model import BaseModel
from datetime import datetime


class Test_Model(unittest.TestCase):
    """ Test for ModelBase """

    @classmethod
    def setUpClass(cls):
        """ Set up an instance for tests """
        cls.Base1 = BaseModel()
        cls.Base1.name = "Student"
        cls.Base1.my_number = 45
        cls.Base2 = BaseModel()
        cls.Base2.name = "Teacher"
        cls.Base2.my_number = 54

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.Base1
        del cls.Base2
        try:
            os.remove("file.json")
        except:
            pass

    def test_docstring(self):
        """ Test if all methods have docstring """
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_instance(self):
        """ Test if objs are instance of BaseModel and check if data is ok """
        self.assertTrue(isinstance(self.Base1, BaseModel))
        self.assertEqual(self.Base1.name, "Student")
        self.assertEqual(self.Base1.my_number, 45)
        self.assertTrue(isinstance(self.Base2, BaseModel))
        self.assertEqual(self.Base2.name, "Teacher")
        self.assertEqual(self.Base2.my_number, 54)

    def test_uniq_id(self):
        """ Check that each instance of a class have different ids"""
        self.assertNotEqual(self.Base1.id, self.Base2.id)

    def test_str(self):
        """ Check if output is OK """
        string = "[BaseModel] ({}) {}".format(self.Base1.id,
                                              self.Base1.__dict__)
        self.assertEqual(string, str(self.Base1))

    def test_save(self):
        """ Test if changes was saved """
        self.Base2.save()
        self.assertNotEqual(self.Base2.created_at, self.Base2.updated_at)

    def test_obj_to_dict(self):
        """ Test if obj was converted to dict """
        _dict = self.Base1.to_dict()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(type(_dict), dict)
        self.assertEqual(type(_dict['created_at']), str)
        self.assertEqual(type(_dict['updated_at']), str)
        self.assertEqual(_dict['updated_at'],
                         self.Base1.updated_at.strftime(time_format))
        self.assertEqual(_dict['created_at'],
                         self.Base1.created_at.strftime(time_format))

    def test_dict_to_BaseObj(self):
        """ Test if a dictionary could be converted to Obj of BaseModel """
        base_json = self.Base1.to_dict()
        obj = BaseModel(**base_json)
        self.assertTrue(isinstance(obj, BaseModel))
        self.assertEqual(obj.name, self.Base1.name)
        self.assertEqual(obj.my_number, self.Base1.my_number)
        self.assertEqual(obj.id, self.Base1.id)
        self.assertEqual(obj.created_at, self.Base1.created_at)
        self.assertEqual(obj.updated_at, self.Base1.updated_at)
        self.assertNotEqual(obj, self.Base1)


if __name__ == '__main__':
    unittest.main()
