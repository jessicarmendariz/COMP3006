#Step 1: test_autompg.py
#In test_autompg.py implement a class called TestAutoMPG that inherits from unittest.TestCase class.
#This class should implement the following methods:
#• setUpClass – This method will instantiate an object of the AutoMPGData class that will be used for testing the code.
#• tearDownClass - This method will delete the auto-mpg.clean.txt file.
#• setUp – This method will simply print “setUp” to the console and nothing else.
#• tearDown - This method will simply print “tearDown” to the console and nothing else.
#• test_str – This method will check that the string being returned by the str method corresponds to the format AutoMPG('chevrolet','chevelle malibu’,1970,18.0)
#• test_eq – Checks that the __eq__ method is working as intended and is using all 4 attributes. Note that this method should only work between AutoMPG objects.
#• test_lt – Checks that the __lt__ method is working as intended and is using all 4 attributes. Note that this method should only work between AutoMPG objects.
#• test_hash – Checks that the has function is working properly.

#Every function must have a print statement that will print the message : “Executing test_name.” where test_name is the name of the current test being executed. 

import unittest


class TestAutoMPG(unittest.TestCase):
    """
    Absolute banger of a DocString here....
    
    All methods MUST start with "test_" in order for Python to recognize
    the method as a test.
    """

