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
from Assignment4 import Records, InvalidColumnNames, NoRecordStatsFound

class TestCollections(unittest.TestCase):
    #DOCSTRING
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.records = Records("credit_card_data.csv", "Credit Card")
        cls.records.load_data("complaints_data.csv", "Complaints")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        del cls.records

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_create_container(self):
        print("Executing test_create_container.")
        valid_headers = ["Column1", "Column2", "Column3"]
        invalid_headers = ["Column 1", "Column@2", "Column#3"]

        Entry = self.records._create_container(valid_headers)
        self.assertEqual(Entry._fields, tuple(valid_headers))

        with self.assertRaises(InvalidColumnNames):
            self.records._create_container(invalid_headers)

    def test_record_stats(self):
        print("Executing test_record_stats.")
        self.records.record_stats("Credit Card", "Period", lambda x: x.Period)
        self.records.record_stats("Complaints", "Product", lambda x: x.Product)

        self.assertIn("stats_Period", self.records.record_dict["Credit Card"])
        self.asserIn("stats_Product", self.records.record_dict["Complaints"])

    def test_extract_top_n(self):
        print("Executing test_exract_top_n.")
        self.records.record_stats("Credit Card", "Period", lambda x: x.Period)
        self.records.record_stats("Complaints", "Product", lambda x: x.Product)

        top_10_periods = self.records.extract_top_n(10, "Credit Card", "stats_Period")
        top_10_products = self.records.extract_top_n(10, "Complaints", "stats_Product")

        self.assertIsInstance(top_10_periods, list)
        self.assertIsInstance(top_10_products, list)

        with self.assertRaises(NoRecordStatsFound):
            self.records.extract_top_n(5, "Credit Card", "stats_NonExistent")

if __name__ == "__main__":
    unittest.main()
