#!/usr/bin/python3
"""Test of console"""

import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


class TestConsole(unittest.TestCase):
    """inheritance of unittest class"""

    def test_docstrings(self):
        """checker for docs"""
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_noargrs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '')

    def test_do_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')

# noarguments
    def test_do_create_noargs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_show_noargs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_destroy_noargs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_all_noargs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            ob = models.storage.all()
            self.assertTrue(f.getvalue())

    def test_do_update_noargs(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

# class doesn't exist
    def test_do_create_dont_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModels")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_show_dont_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModels")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_destroy_dont_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModels")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_all_dont_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModels")
            Objcls = models.storage.all()
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_update_dont_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModels")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

# good arguments class
    def test_do_create_good(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(f.getvalue())

    def test_do_all_good(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            Objcls = models.storage.all()
            self.assertTrue(f.getvalue())

# id missing
    def test_do_show_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_destroy_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_update_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

# no instances found
    # def test_do_show_inst_found(self):
    # def test_do_destroy_inst_found(self):
    # def test_do_update_inst_found(self):

# attribut missing
    # def test_do_update_attr_missing(self):
# value missing
    # def test_do_update_val_missing(self):


if __name__ == '__main__':
    unittest.main()
