#Step 3: test_shelter.py
#In test_shelter.py implement a class called TestShelter that inherits from unittest.TestCase class.
#This class should implement the following methods:
#• setUpClass – This method will simply print “setUpClass” to the console and nothing else.
#• tearDownClass - This method will simply print “tearDown” to the console and nothing else.
#• setUp – This method will create instances of the Tent, Tarp and Hammock classes, as many as you think is needed to thoroughly test your code.
#• tearDown - This method will delete each instance of Tent, Tarp and Hammock that you created in the setUp method.
#• test_str – This method will check that the string being returned by the str method corresponds to the format . Shelter(num_occupants, material, setup_time, sqft (if applicable), vestibule (if applicable), weight, structure_poles (if applicable), seasons).
#• test_lt – Checks that the __lt__ method is working as intended. It should use the corresponding __lt__ methods based on the class of the object.
#• test_is_better – Checks that the is_better method is working as intended.

#Every function must have a print statement that will print the message : “Executing test_name.” where test_name is the name of the current test being executed.

import unittest
from shelter import Tent, Tarp, Hammock  

class TestShelter(unittest.TestCase):
    #- This CLass is the Test Suite for Shelter and Inherits from Unit Test

    #Runs Once Before All Tests and Instantiates Shelter and Assigns in to cls.data
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    #Runs Once After All Tests and Cleans Up
    @classmethod
    def tearDownClass(cls):
        print("tearDown")

    #Runs Before Each Test
    def setUp(self):
        print("Setting up test cases.")
        self.tent1 = Tent(4, "nylon", 30, 100, True, 5, True, "4-season")
        self.tent2 = Tent(2, "canvas", 45, 80, False, 7, False, "3-season")
        self.tarp1 = Tarp("polyester", 10, 50)
        self.tarp2 = Tarp("silnylon", 5, 30)
        self.hammock1 = Hammock("parachute nylon", 15, 300, 2)
        self.hammock2 = Hammock("cotton", 20, 250, 1)

    #Runs After Each Test 
    def tearDown(self):
        print("Tearing down test cases.")
        del self.tent1
        del self.tent2
        del self.tarp1
        del self.tarp2
        del self.hammock1
        del self.hammock2

    #Tests String Methods
    def test_str(self):
        print("Executing test_str.")
        self.assertEqual(str(self.tent1), "Shelter(4, nylon, 30, 100, True, 5, True, 4-season)")
        self.assertEqual(str(self.tarp1), "Shelter(polyester, 10, 50)")
        self.assertEqual(str(self.hammock1), "Shelter(parachute nylon, 15, 300, 2)")

    #Tests Less Than Methods
    def test_lt(self):
        print("Executing test_lt.")
        self.assertTrue(self.tent1 < self.tent2)
        self.assertTrue(self.tarp1 < self.tarp2)
        self.assertTrue(self.hammock2 < self.hammock1)

    #Tests Is Better Than Method
    def test_is_better(self):
        print("Executing test_is_better.")
        self.assertTrue(self.tent1.is_better(self.tent2))
        self.assertFalse(self.tarp2.is_better(self.tarp1))
        self.assertTrue(self.hammock1.is_better(self.hammock2))

#Runs Tests
if __name__ == "__main__":
    unittest.main()
