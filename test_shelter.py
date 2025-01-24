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
