#Step 3: test_assignment4.py
#In test_assignment4.py implement a class called TestCollections that inherits from unittest.TestCase class.
#This class should implement the following methods:
#• setUpClass – This method will print “setUpClass” to the console and instantiate an object of the Record class using the credit card file and the complaints file. 
#The data from both files must exist within the same instance.
#• tearDownClass - This method will print “tearDownClass” to the console and delete the instance of Record class created in the setUpClass method.
#• setUp – This method will print “setUp” to the console and nothing else.
#• tearDown - This method will print “tearDown” to the console and nothing else.
#• test_create_container – This method will check that the method is able to create a namedtuple with varying number of column names and that it raises the appropriate exceptions.
#• test_ record_stats – Checks that the function is able to compute record stats correctly for various columns and multiple files. 
#It must also verify that the attribute structure for the Record object where the record stats are being stored is correct.
#• test_extract_top_n – Checks that the method is able to extract the correct top n values for the corresponding column record stats attribute. 
#Note you will need to execute the record_stats method with the column that you want to test.
#Every function will have a print statement that will print the message : “Executing test_name.” where test_name is the name of the current test being executed.


import unittest

class TestCollections(unittest.TestCase):
    #DOCSTRING
    def setUpClass():
        pass

    def tearDownClass():
        pass

    def setUp():
        pass
    #print("setUp")

    def tearDown():
        pass
    #print("tearDown")

    def test_create_container():
        pass

    def test_record_stats():
        pass

    def test_extract_top_n():
        pass

