#Week 6 Assignment – Pandas

#In this assignment, you will be working with 1 data file: realtor-data.csv which contains over 1.4 million rows. 
#Use the file provided as it has been modified from the online file from Kaggle. 
#The columns of the dataset are :
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
#Please download the Assignment 6 zip file. 
#Within the zipped file you should find two files, a python file called production.py and a Jupyter Notebook file called prototyping.ipynb. 
#You will need to create a folder inside the Assignment 6 folder called data and place the realtor-data.csv inside.
#All testing code must be inside of an if __name__==“__main__”.

#Assignment6: (folder)
#———production.py
#———prototyping.ipynb
#———data: (package)
#——————realtor-data.csv

#Real Estate dataset:
#• https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset

#Step 1: Complete the questions in prototyping.ipynb Data Science revolves primarily around Exploratory Data Analysis (EDA) which consists of importing, visualizing and cleaning data. 
#This is done in order to build a data pipeline which allows processing large amounts of data in a standardized way.
#Any model that requires large amounts of data (which is just about everything these days), must have an efficient and robust data pipeline to help train said model.
#The prototyping notebook will take you through some of the steps that are standard when exploring new data.

#Step 2: Convert the prototype Jupyter Notebook into a module
#Jupyter notebooks are very helpful when you want to perform EDA and fast prototyping. 
#Once you’ve analyzed your data and have a data pipeline, we can create a Python module that can be deployed to teammates or placed in a larger data pipeline.

#In production.py implement a class called RealEstate2. 
#This class will contain the entire real estate data set. 
#The class must have the attribute properties_df.

#This class should implement the following methods:
#• __init__ – Constructor that takes a file_name and a location as arguments. 
#The method should create a properties_df attribute as an empty pandas DataFrame and makes a call to the load_data method.

#• properties_df: this is a pandas DataFrame.

#• load_data – Method takes file_name and a file_path as arguments, and makes a call to loads the data from the realtor-data.csv into the properties_df attribute.
#The method must also make a call to the _col_2_numeric method described below. 
#Once the data is of the correct data types, it should drop duplicate rows.
#This method must be able to handle a file not found error, and should ask the user to input a valid file name until they entered a valid file name or quit if the user enters ‘q’.

#• _col_2_numeric – Method takes no arguments and asks the user to enter the name of the columns they wish to make numeric. 
#The method will ask the user until they enter “q”. 
#The method will then proceed to make each column entered into numeric values and any values that cannot be casted to a numeric type, will be replaced with NaN (Not A Number).
#The method must be able to handle the case of a column name that was given isn’t in the DataFrame. (must use a custom helper function to do this)

#• check_type - Method takes no argument and returns the data types of the columns of the DataFrame.

#• num_nulls - Method takes a column name as an argument and returns the number of null values in the column given.
#The method must be able to handle the case of a column name that was given isn’t in the DataFrame. (must use a custom helper function to do this)

#• get_unique_vals - Method takes a column name as an argument and returns the number of unique values and the unique values themselves for the column given.
#The method must be able to handle the case of a column name that was given isn’t in the DataFrame. (must use a custom helper function to do this)

#• filth_be_gone - Method takes a column name and a value as arguments and removes all rows containing the value given from the column that was passed in.
#The method must be able to handle the case of a column name that was given isn’t in the DataFrame. (must use a custom helper function to do this)

#• col_val_count - Method takes a column name and returns the count of each value present in the given column.
#The method must be able to handle the case of a column name that was given isn’t in the DataFrame. (must use a custom helper function to do this)

#• summary_table - Method takes an undetermined number of columns used to create a multi-index.
#It also takes an undetermined number of columns the user is interested in summarizing and an undetermined number of operations to summarize the columns of interest, these operations can be “mean”, “mode”, “min”, etc. 
#The function returns the resulting DataFrame
#The method must be able to handle the case of a column name that was given isn’t in the DataFrame. (must use a custom helper function to do this)

#Step 3: Write the helper functions
#The helper functions will consist of the function used to handle the case when the user tries to access a column that does not exist, it should print a message to the console and exit the method.
#The second helper function is a custom summary operation that can be used in the summary_table method from Step 2. 
#This summary statistic will calculate the percentage of values which are above the median value of the column, i.e. if the median value for a given column is 5 then what percentage of the values in that particular column are above 5? (think about edge cases and handle them :) )

#Upload
#Please ZIP the Assignment6 folder containing all folders and files described above including the data file. Your code must be in the same hierarchy as shown at the beginning of the homework.
