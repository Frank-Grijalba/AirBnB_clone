#!/usr/bin/python3
"""Test module"""


import pep8
import unittest
from models.state import State


class TestMyState(unittest.TestCase):
    """New class to test class State"""

    def setUp(self):
        """Setting up"""
        self.my_state = State()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_state

    def test_is_instance(self):
        """Check if an instance belongs to class State"""
        self.assertIsInstance(self.my_state, State)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.my_state.name, str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_state, State)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.my_state.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Test that we conform to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = 'models/state.py'
        file2 = 'tests/test_models/test_state.py'
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

if __name__ == '__main__':
    unittest.main()
