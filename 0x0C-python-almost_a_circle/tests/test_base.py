#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """Presence of docstrings"""
    def test_presence_of_module_docstring(self):
        module_doc = base.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        init_doc = Base.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_to_json_docstring(self):
        to_js_doc = Base.to_json_string.__doc__
        self.assertTrue(len(to_js_doc) > 1)

    def test_presence_of_from_json_docstring(self):
        f_js_doc = Base.from_json_string.__doc__
        self.assertTrue(len(f_js_doc) > 1)

    def test_presence_of_save_to_file_docstr(self):
        stf_doc = Base.save_to_file.__doc__
        self.assertTrue(len(stf_doc) > 1)

if __name__ == "__main__":
    unittest.main()
