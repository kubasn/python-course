# *** 
# BaseTest
# This class should be the parent class to each non-unit test.

# it will allow for instantiation of the database dynamically and
# makes sure that it is a new, blank database each time

from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
#    runs bafore each test
    def setUp(self):
        # make sure database exists
        # get the test client 
    
        pass
    def tearDown(self):
        # Erase database
        pass

# runs after each test 