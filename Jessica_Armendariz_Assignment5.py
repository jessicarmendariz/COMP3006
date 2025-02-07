#Week 5 Assignment – File I/O

#In this assignment, you will create multiple new classes and functions.
#You will be working with 1 data file: realtor-data.csv which contains over 1.4 million rows. 
#Use the file provided as it has been modified from the online file from Kaggle.
#The columns of the dataset are:
#realtor-data.csv (1.4 Million+ entries)
#◦ status (Housing status - a. ready for sale or b. ready to build)
#◦ bed (# of beds)
#◦ bath (# of bathrooms)
#◦ acre_lot (Property / Land size in acres)
#◦ city (city name)
#◦ state (state name)
#◦ zip_code (postal code of the area)
#◦ house_size (house area/size/living space in square feet)
#◦ prev_sold_date (Previously sold date)
#◦ price (Housing price, it is either the current listing price or recently sold price if the house is sold recently)

#Please follow the steps outlined below.
#Preparation
#Please create a new folder called Assignment5, within the folder create an additional folder called real_estate. 
#Inside of the real_estate folder create 2 additional folders called helper_functions and load_data.
#Make sure that you’re able to import all the modules from the correct file, 
#i.e. load.py should be able to import calculate_stats and context_manager, and run.py should be able to import load.py.
#Remember that if you’re testing an import within a file, when trying to execute that same import from the run.py file 
#The import statement might not work as expected (review absolute and relative imports files).

#All testing code inside each module should be inside of a if __name__==“__main__” to prevent your test code from running when you import the module.

#Assignment5: (folder)
#———run.py #primary file that executes your code (module)
#———real_estate: (package)
#——————load_data: (package)
#—————————load.py (module)
#—————————data: (package)
#————————————realtor-data.csv
#——————helper_functions: (package)
#—————————calculate_stats.py (module)
#—————————context_manager.py (module)

#Real Estate dataset:
#• https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset

#Step 1: load.py inside the load_data package.
#In load.py implement a class called RealEstate. 
#This class will contain the entire real estate data set. 
#The class must have the attribute properties_dict. 
#You must import the custom contextmanager using an absolute import and you must import the calculate stats module using a relative import.
#This class should implement the following methods:
#• __init__ – Constructor that takes a file_name and a location as arguments. 
#The method should create a properties_dict attribute and makes a call to the load_data method.
#• properties_dict: this is a defaultdict with a nested defaultdict which in turn creates a list, just like in Assignment 4. 
#The keys for the “outer” dictionary will be “US States” and “Territories”. 
#The keys for the “inner” will be the different US States in the file or the two US territories. 
#Just like in assignment 4 you must use a defaultdict and lambda function for this behavior.
#The structure of the properties_dict should be as follows:

defaultdict(<function RealEstate.__init__.<locals>.<lambda> at 0x104691bc0>,
{
'Territories': defaultdict(<class 'list'>,
{
‘Puerto Rico’: [],
‘Virgin Islands’ :[]
}),
'US States': defaultdict(<class 'list'>,
{
‘Massachusetts’: [],
‘Connecticut’: [],
...
})
})

#The US states present in the file are:

#‘Massachusetts', ‘Connecticut’, 'New Hampshire’, ‘Vermont', 'New Jersey’, 'New York' 'South Carolina’, ‘Tennessee', 'Rhode Island’, ‘Virginia', ‘Wyoming', ‘Maine', ‘Georgia', ‘Pennsylvania', 'West Virginia’, ‘Delaware', 'Louisiana'
#• load_data – Method takes file_name and a location as arguments, and loads the data from the file using the custom contextmanager described in Step 2. 
#The method must also make a call to the _create_container method described below. 
#Using the Property namedtuple container created, use it to create a Property namedtuple for each line in the file. 
#Finally add the Property container to the properties_dict, in the US States or Territory dictionary based on the State attribute of the Property namedtuple 
#which will also be used to insert the data into the appropriate state/territory. 

#You should end up with a list of Property namedtuples associated with the keys "US States” or “Territories” and the appropriate state or territory. 
#Please refer to the structure of properties_dict given above.
#This method must be able to handle a file not found error, and should ask the user to input a valid file name until they entered a valid file name or quit if the user enters ‘q’.
#Note: to extract the first line of the file you can use the method next().
#• _create_container – Method takes the first line of the file, which contains the names of the columns, as an argument. 
#You must then unpack the column names to create a namedtuple called Property that will have the column names as the names of the attributes. 
#Return the Property namedtuple.
#• compute_stats - Method takes a function name (one of the functions from calculate_stats module) (str) and a variable number of arguments and keyword arguments and returns the value of the function called.

#Step 2: Create a custom contextmanager in context_manager.py
#You may use either a function or a class to define your contextmanager. 
#It will need to take a file name, a mode, and a destination as arguments.
#If you opt to use a class you will need an __enter__ and __exit__ method.
#If you opt for the function you will need to use the @contextmanager decorator.
#This custom contextmanager changes the current working directory to the folder that contains the data. 
#It will print the message “Loading data” when called. 
#It will then change current working directory back to the original “Assignment5” directory and print “Data loaded” when done.
#To change directories you will need to import the OS module.

#Step 3: calculate_stats.py
#In helper_functions you will write a series of functions that will compute stats of interest for the real estate data. 
#You will need to have the following functions:
#• cheapest – Function that takes the property_dict and a State or Territory, 
#i.e. Connecticut or Virgin Islands, (str) as arguments, and returns the Property container for the cheapest property for the given State/Territory.
#• priciest - Function that takes the property_dict and a State or Territory, 
#i.e. Connecticut or Virgin Islands, (str) and returns the Property container for the most expensive property for the given State/Territory.
#• dirt_cheap - Function takes the property_dict as argument and returns the Property container of the absolute cheapest property in all of the US States and Territories 
#(if you’re clever or lazy, you might be able to leverage the cheapest function to do this but it’s not required).
#• best_deal - Function that takes the property_dict, a State or Territory, 
#i.e. Connecticut or Virgin Islands, (str) a number of bedrooms (int) and a number of bathrooms (float) as arguments.
#And returns the Property container for the property that has the best price per square foot (use price and house_size for this).
#• budget_friendly - Function takes the property_dict, number of bedrooms (int), number of bathrooms (float), and a maximum budget (float) 
#as arguments, and returns the Property container for the property that gives you the best bang for the buck regardless of the 
#State/Territory (if you’re clever or lazy, you might be able to leverage the best_deal function to do this but it’s not required).

#Every function must be able to handle a poorly formatted rows, i.e. ignore the row. 
#This could be a missing value or a “?” in place of a numeric value.
#(I may have punched my keyboard in a few places... khugghgjhjgjvghkhv. If you want to do something evil, do it in something boring.)
#Every function and class needs to have proper DocString documentation. 
#Refer to the homework guideline files if needed :)

#Step 4: run.py
#In this final step you will write a function called main, that takes no arguments and instantiates the RealEstate class. 
#It will print the first 5 Property containers for every
#State and Territory in the format:

‘Puerto Rico’:[Property<...>, Property<...>, Property<...>, Property<...>, Property<...>]
...
‘Louisiana’:[Property<...>, Property<...>, Property<...>, Property<...>, Property<...>]

#It will also call the method computes_stats with every function in the calculate_stats module and print the results 
#(you don’t need to call the functions that require a State or Territory for every State or Territory, just one will suffice to test the function).
#Inside of an if __name__==“__main__” block, call the main function.

#Upload
#Please ZIP the Assignment5 folder containing all folders and files described above including the data file. 
#Your code must be in the same hierarchy as shown at the beginning of the homework.
