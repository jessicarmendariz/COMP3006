#Week 4 Assignment–Collections, Exceptions & Testing
#In this assignment, you will create multiple new classes, including custom exceptions class and unit testing. 
#You will also use the collections module, which you will need to import.
#You will be working with 2 data files: Credit card transactions and Consumer complaints.
#Please follow the steps outlined below.

#Preparation
#Please create a new folder called Assignment4 and create a new module called Assignment4.py, test_assignment.py and add both dataset files.
#Do not download the files, one of them is 3GB. Use the files provided. 
#Check the links to see the structure of the data files.

#Credit card transactions dataset:
#• https://www.kaggle.com/datasets/najeebz/electronic-card-transactions-dec-2023-new-zealand

#Consumer complaint dataset:
#• https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database

#Step 1: Assignment4.py
#In Assignment4.py implement a class called Records. This class will represent the entire record dataset you’re working with, credit card transactions and consumer complaints.
#The class must have the attribute record_dict.
#This class should implement the following methods:
#• __init__ – Constructor that takes the a file_name and file_title as an argument.
#The method should create a record_dict attribute and makes a call to the load_data method.
#• record_dict: dictionary that will create a key-value pair using file_title as the key and another defaultdict as the value.
#• this nested defaultdict will have an empty list as a value by default. You must use a defaultdict and lambda function for this behavior.
#The structure of the record_dict should be as follows:

defaultdict(<function <lambda> at 0x108b985e0>,
{
'Credit Card': defaultdict(<class 'list'>,
{
'data': [Credit card data here...],
'stats_Period': [Counter for Period column here...]
}),
'Complaints': defaultdict(<class 'list'>,
{
'data': [Credit card data here...],
'stats_Product': [Counter for Period column here...]
})
})
                 
#• load_data – Method takes file_name and file_title as arguments, and loads the data from the file and makes a call to the _create_container method described below.
#Using the Entry namedtuple container created, use it to create an Entry namedtuple for each line in the file. 
#Finally append it to the record_dict using file_title as the key for the top layer defaultdict and data as the key for the nested defaultdict. 
#You should end up with a list of namedtuples associated with the keys file_title and data. 
#Please refer to the structure of record_dict given above.
#This method must be able to handle a file not found error, and should ask the user to input a valid file name until they entered a valid file name or quit if the user enters ‘q’. 
#The exception handling must also make use of an “else” clause to print to the console that the file was loaded successfully.

#Note: to extract the first line of the file you can use the method next().
#• _create_container – Method takes the first line of the file, which contains the names of the columns, as an argument. 
#It must make a call to _standardize_col_names method described below.
#You must then unpack the column names to create a namedtuple called Entry that will have the column names as the names of the attributes. 
#Return the Entry namedtuple.
                 
#• _standardize_col_names - Method takes list of column names and replaces “_”, “-“ and blank spaces with an empty string, you can use str.replace method to do this. 
#After standardizing the column names, check that all column names are alpha-numeric (meaning it’s only letters and numbers). 
#If the column names are not alpha-numeric, you must raise a custom exception called InvalidColumnNames described below in Step 2. 
#You must pass the column names to the exception and your “except” statement should print the msg attribute of the InvalidColumnNames exception class and ask the user to input the names of the columns by hand. 
#Return the standardized columns list.
                 
#• record_stats - Method takes the file_title, a column name you wish to process and a lambda function, as arguments. 
#You will need to retrieve the values for the given column in the appropriate data list using the lambda function that was passed in and the map method. 
#Once you have extracted the values use a Counter object to summarize the number of instances in that column.
#This should give you a Counter object that pairs the value in the column with the number of times that value appeared in your data. 
#Store the result inside of the appropriate file_title dictionary using “stats_column_name” as the key (this should also be done dynamically).
                 
#• extract_top_n - Method takes an integer, file_title and a stats_column_name a arguments. 
#It must return the top n most frequent values for the Counter object created by the record_stats method for the given column, where n is the integer that was passed into the function. 
#If the stats_column_name doesn’t exist, you must raise a custom NoRecordStatsFound exception described below. 
#You must pass the stats_column_name to the exception and your “except” statement should print the msg attribute of the NoRecordStatsFound exception class and ask the user to enter a different stats_column_name or “q” to quit.

#-For the credit card file the 10 most common values in the Period column are :
                 
[('2004.03', 137), ('2005.03', 137), ('2006.03', 137), ('2007.03', 137), ('2008.03',
137), ('2009.03', 137), ('2010.03', 137), ('2011.03', 135), ('2012.03', 135),
('2013.03', 135)]
                 
#-For the customer complaints file the 10 most common values in the Product
column are :
                 
[('Credit reporting or other personal consumer reports', 109620),
('Debt collection', 5826),
('Credit card', 4802),
('Checking or savings account', 3663),
('Mortgage', 1885),
('Student loan', 1144),
('Money transfer, virtual currency, or money service', 1083), 
('Vehicle loan or lease', 920),
('Payday loan, title loan, personal loan, or advance loan', 533),
('Prepaid card', 511)]
                 
#Step 2: Create 2 custom Exception classes
#You will define a custom class called InvalidColumnNames.
#This Exception class must have the following method:
#• __init__ - Constructor that takes in a list containing the column names that caused the exception and stores it in an attribute called col_names. 
#It will also create an attribute called msg that will contain the following message:
#“The names of the columns are invalid. Column names can only be letters and numbers : {column_names}” 
#Where column_names are the column names from the file that caused an issue (this value must be updated dynamically). Print this message to the console.
#You will define a second custom class called NoRecordStatsFound.
#This Exception class must have the following method:
#• __init__ - Constructor that takes in the stats_column_name that caused the exception and stores it in an attribute called column_name. 
#It will also create an attribute called msg that will contain the following message:
#“The column stats you’re trying to access doesn’t exist. You entered {column_name}.”
#Where column_name is the column you tried to access. Print this message to the console.

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

#Upload
#Please ZIP the Assignment4 folder containing the Assigment4.py, test_assignment4.py and your data files and upload to Canvas.

import csv
from collections import defaultdict, Counter, namedtuple
import re

#Class Loads and Processes the CSV files, Stores Data in the Default Dictionary, Cleans and Standardizes Column Names
class Records:
    #Initializes the Records Instance and Loads Data from the CSV Files
    #Contains 6 Methods: __init__, load_data, _create_container, _standardize_col_names, record_stats, and extract_top_n
    def __init__(self, file_name="", file_title=""):
        self.file_name = file_name
        self.file_title = file_title

        #Creates the Required Default Dictionary
        self.record_dict = defaultdict(lambda: defaultdict(list),
        {
           'credit card': defaultdict(list,
                  {
                    'data': [],
                    'stats_period': Counter()
                  }),
           'complaints': defaultdict(list,
                  {
                    'data': [],
                    'stats_product': Counter()
                  }),
        })
        if self.file_name and self.file_title:
            self.load_data(self.file_name, self.file_title)

    #Load credit_card.csv and customer_complaints.csv into Dictionary
    def load_data(self, file_name, file_title):
        #Reads the CSV File, Creates a NamedTuple, and Loads All Rows into the Dictionary as NamedTuples
        #Finds the Invalid Column Names and Prompts User for the Corrected Names
        while True:
            try:
                with open(file_name, mode='r') as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    Entry = self._create_container(headers)
                    self.record_dict[file_title]['data'] = [Entry(*row) for row in reader]  
                    print(f"File {file_name} Loaded Successfully.")
                break  

            except FileNotFoundError:
                file_name = input("File Not Found. Enter a Valid File Name or 'q' to Quit: ")
                if file_name.lower() == 'q':
                    break

            except InvalidColumnNames as e:
                print(e.msg)
                headers = input("Enter Valid Column Names Separated By Commas: ").split(',')
                Entry = self._create_container(headers)

    def _create_container(self, headers):
        #Creates a NamedTuples using Standardized Column Headers
        standardized_headers = self._standardize_col_names(headers)
        return namedtuple("Entry", standardized_headers)

    def _standardize_col_names(self, headers):
        #Fixes ALL Column Names by Replacing the Spaces and Dashes with Underscores
        #Removes ALL Special Characters and Covnverts Data to Lowercase
        standardized_headers = []
        for col in headers:
            clean_col = col.strip().replace(" ", "_").replace("-", "_")
            clean_col = re.sub(r'[^a-zA-Z0-9_]', '', clean_col)
            clean_col = clean_col.lower()
            standardized_headers.append(clean_col)
        return standardized_headers

    def record_stats(self, file_title, column_name, extract_func):
        #Checks if Data Exists, Standardizes Column Names, Uses Counters to Count Occurances
        #Stores Results in the Dictionary
        if not self.record_dict[file_title]['data']:
            raise ValueError(f"No data found in {file_title}.")
        standardized_column_name = column_name.strip().replace(" ", "_").replace("-", "_").lower()
        if standardized_column_name not in self.record_dict[file_title]['data'][0]._fields:
            raise KeyError(f"Column '{column_name}' not found in {file_title}")
        values = list(map(extract_func, self.record_dict[file_title]['data']))
        self.record_dict[file_title][f'stats_{column_name}'] = Counter(values)

    def extract_top_n(self, n, file_title, stats_column_name):
        #Extracts the Top N Most Common Values
        stats_key = f'stats_{stats_column_name}'
        if stats_key not in self.record_dict[file_title]:
            raise NoRecordStatsFound(stats_column_name)
        return self.record_dict[file_title][stats_key].most_common(n)

#Handles Column Name Exceptions
class InvalidColumnNames(Exception):
    def __init__(self, column_names):
        self.col_names = column_names
        self.msg = f"Invalid Column Names: {column_names}. Please Enter Valid Column Names."
        super().__init__(self.msg)

#Handles Non Existent Records
class NoRecordStatsFound(Exception):    
    def __init__(self, stats_column_name):
        self.column_name = stats_column_name
        self.msg = f"No Record Stats Found For {stats_column_name}. Enter a Different Stats Column Name or 'q' to Quit."
        super().__init__(self.msg)


def main():
    #Creates Required Outputs
    credit_card_records = Records("credit_card.csv", "credit card")
    complaints_records = Records("customer_complaints.csv", "complaints")
    credit_card_records.record_stats("credit card", "Period", lambda x: x.period)
    complaints_records.record_stats("complaints", "Product", lambda x: x.product)
    top_10_credit = credit_card_records.extract_top_n(10, "credit card", "Period")
    top_10_complaints = complaints_records.extract_top_n(10, "complaints", "Product")

    #Print Results
    print("\nFor the credit card file, the 10 most common values in the Period column are:")
    print(top_10_credit)
    print("\nFor the customer complaints file, the 10 most common values in the Product column are:")
    print(top_10_complaints)


if __name__ == "__main__":
    main()
