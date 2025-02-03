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
from collections import namedtuple, Counter

#Loads Data, Cleans Up After Tests, Runs the SetUp adn TearDown, Tests the Functions
class TestCollections(unittest.TestCase):
    #Runs Before All Tests
    #Creates an Instance of Records
    #Prints SetUpClass
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.records = Records("credit_card.csv", "Credit Card")
        cls.records.load_data("customer_complaints.csv", "Complaints")

    #Runs Before All Tests
    #Deletes Records Instance
    #Prints TearDownClass
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        del cls.records

    #Runs Before Each Test
    def setUp(self):
        print("setUp")

    #Runs After Each Test
    def tearDown(self):
        print("tearDown")

    #Tests Create Container and Creates Test Headers (1 & 2)
    #Tests Assertions and Errors
    def test_create_container(self):
        print("Executing test_create_container.")
        headers1 = ["Transaction_ID", "Amount", "Date"]
        headers2 = ["Product", "Category", "Complaint"]

        Entry1 = self.records._create_container(headers1)
        Entry2 = self.records._create_container(headers2)

        self.assertTrue(issubclass(Entry1, tuple))
        self.assertTrue(issubclass(Entry2, tuple))
        self.assertEqual(Entry1._fields, ("transactionid", "amount", "date"))
        self.assertEqual(Entry2._fields, ("product", "category", "complaint"))
        with self.assertRaises(InvalidColumnNames):
            self.records._create_container(["ValidName", "Invalid@Name", "123"])

    #Tests Assertions for Frequency Counts
    def test_record_stats(self):
        print("Executing test_record_stats.")
        self.records.record_stats("Credit Card", "Period", lambda x: x.Period)
        
        stats_key = "stats_Period"
        self.assertIn(stats_key, self.records.record_dict["Credit Card"])
        self.assertIsInstance(self.records.record_dict["Credit Card"][stats_key], Counter)
        self.records.record_stats("Complaints", "Product", lambda x: x.Product)
        
        stats_key = "stats_Product"
        self.assertIn(stats_key, self.records.record_dict["Complaints"])
        self.assertIsInstance(self.records.record_dict["Complaints"][stats_key], Counter)

    #Tests Extracting Top Period Values and Top Product Values
    #Tests Assertions and Error Handling
    def test_extract_top_n(self):
        print("Executing test_extract_top_n.")

        self.records.record_stats("Credit Card", "Period", lambda x: x.Period)
        self.records.record_stats("Complaints", "Product", lambda x: x.Product)

        top_5_credit = self.records.extract_top_n(5, "Credit Card", "Period")
        self.assertEqual(len(top_5_credit), 5)
        self.assertIsInstance(top_5_credit, dict)

        top_3_complaints = self.records.extract_top_n(3, "Complaints", "Product")
        self.assertEqual(len(top_3_complaints), 3)
        self.assertIsInstance(top_3_complaints, dict)

        with self.assertRaises(NoRecordStatsFound):
            self.records.extract_top_n(3, "Credit Card", "NonExistentColumn")

#Run Tests
if __name__ == "__main__":
    unittest.main()
