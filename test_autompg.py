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
import os

from autompg import AutoMPG, AutoMPGData  # Assuming these classes are defined in autompg.py

class TestAutoMPG(unittest.TestCase):
    #- This CLass is the Test Suite for AutoMPG and Inherits from Unit Test

    #Runs Before All Tests and Instantiates AUtoMPGData and Assigns in to cls.data
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.data = AutoMPGData()

    #Runs After All Tests and Deletes the Clean File After Cleaning the Tests
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        if os.path.exists("auto-mpg.clean.txt"):
            os.remove("auto-mpg.clean.txt")

    #Runs Before Each Individual Test and Prints for Updates
    def setUp(self):
        print("setUp")

    #Runs After Each Individual Test and Prints for Updates
    def tearDown(self):
        print("tearDown")

    #Tests teh String Methods and Verifies the Format
    def test_str(self):
        print("Executing test_str.")
        car = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertEqual(
            str(car),
            "AutoMPG('chevrolet', 'chevelle malibu', 1970, 18.0)"
        )

    #Equlaity Test and Verifies Formatting
    def test_eq(self):
        print("Executing test_eq.")
        car1 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        car2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        car3 = AutoMPG("ford", "mustang", 1968, 16.0)
        self.assertTrue(car1 == car2)
        self.assertFalse(car1 == car3)

    #Less Than Comparison
    def test_lt(self):
        print("Executing test_lt.")
        car1 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        car2 = AutoMPG("ford", "mustang", 1968, 16.0)
        car3 = AutoMPG("toyota", "corolla", 1980, 32.0)
        self.assertTrue(car2 < car1)  # Assuming __lt__ is based on year or another criteria
        self.assertFalse(car3 < car1)

    #Tests the Hash Method and Verifies Formatting for Hash Values
    def test_hash(self):
        print("Executing test_hash.")
        car1 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        car2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        car3 = AutoMPG("ford", "mustang", 1968, 16.0)
        self.assertEqual(hash(car1), hash(car2))
        self.assertNotEqual(hash(car1), hash(car3))


#Run Tests
if __name__ == "__main__":
    unittest.main()
