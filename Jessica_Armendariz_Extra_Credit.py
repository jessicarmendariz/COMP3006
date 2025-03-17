#Extra Credit – Pandas
#For this extra credit assignment, you will be working with multiple txt and csv data files.
#The files have 43 columns but we will be working with the following columns only :
#◦ SITE_NBR
#◦ SITE_DIR
#◦ SITE_NAME
#◦ SITE_MODE
#◦ SITE_MORE
#◦ TAX_DIST

#Preparation
#Please create the following project structure defined below. 
#All testing code must be inside of an if __name__==“__main__” and all classes and methods must have all necessary DocString documentation.

#Extra_credit: (folder)
#———run.py
#———project (package):
#——————properties: (package)
#—————————property.py
#——————data:
#————————— various data files (csv, txt)
#—————————my_maps: (create_map method will create this with os module)
#————————————denver_map.html (output file of the create_map method)
#——————freebies: (package)
#—————————helper_functions.py

#Some advise before you get started. 
#Open the data files to familiarize yourself with the structure of the data. 
#Use a jupyter notebook to do fast prototyping so you can quickly figured out how to navigate to the data file folder, how to write your regular expression, add a new column to a DataFrame by combining multiple other columns and check that your imports all work.
#You will need to install geocoder and folium in order for the project to work, make sure that works before running the code.

#Step 1: Create a class and plot some data (20 pts)
#In property.py import all the necessary methods from freebies, using one absolute import and one relative import. 
#You will also implement a class called ApartmentCommercial. 
#This class will contain the entire real estate data set. 
#The class must have the attribute commercial_properties_df.
#This class should implement the following methods:
#• __init__ – Constructor that takes a folder_path, a key_word and an optional file_extension (‘txt’, ‘csv’, or ‘both’, with a default of ‘both’) as arguments. 
#The method should create a commercial_properties_df attribute as an empty pandas DataFrame and makes a call to the load_data method.
#• commercial_properties_df: this is a pandas DataFrame.
• load_data – This method must take the folder_path, key_word and the optional file_extension (‘txt', ‘csv' or ‘both’, with a default of both) from the constructor as arguments. 
#The folder_path should be the path to the data folder where all the files are stored. 
#The key_word argument will be a string that the file name must contain in order to be loaded into the commercial_properties_df DataFrame. 
#If key_word = ‘apartment’ then all data files that contain the string ‘apartment’ as part of their file name should be loaded into the DataFrame.
#Finally all file must also have the file_extension ‘txt’, ‘csv’ or either ’txt’ or ‘csv’.
#To simplify loading in the data you may assume that ‘txt’ files will also have comma separated values so you may use read_csv method for both types of files.
#When looking for file names that match with key_word and file_extension you must also use a regular expression. 
#Make sure your regular expression can match the strings ‘apartment’, ‘commercial’, ‘and’ or ‘characteristic’ (meaning that key_word can be at the beginning, middle or end of the file name). 
#Since you’re loading in data from multiple files, you’ll want to reset the index of the DataFrame to ensure that your indices are numbered from 0 to len(commercial_properties_df).
#Lastly make sure the ‘SITE_NBR’ column values are integer values.
#• denver_filtered_data - This method takes no arguments. 
#The method will modify the existing commercial_properties_df and filter the properties so the resulting DataFrame only has properties from TAX_DIST == ‘DENV’. 
#You will also need to reset the index of the DataFrame to ensure that your indices are numbered from 0 to the new len(commercial_properties_df).
#• create_address - This method takes no arguments and creates an additional 'Address’ column in the commercial_properties_df. 
#This column will combine the data from the columns: SITE_NBR, SITE_DIR, SITE_NAME and SITE_MODE.
#You must also append ‘, Denver, CO’ to each entry. 
#This means that your entries in the ‘Address’ column with be formatted like this: ‘26100 E 88TH AVE, Denver, CO’, which is how property addresses are typically formatted.
#• random_properties - This method takes an argument, prop_amount, of type numeric (float or int). 
#Check that prop_amount is positive and if it’s int or float.
#If prop_amount is an integer, then the function must return a list containing prop_amount number of random integer values between 0 and the number of properties available, all values must be unique.
#If prop_amount is a float between 0 and 1 (this value will be considered a percentage with 0.1 meaning 10%), then you must return a list containing that percentage number of random integer values between 0 and the number of properties available, all values must also be unique.
#The method must return the resulting list of values which represent a collection of row indices of the commercial_properties_df DataFrame.
#• _lat_long - This method takes a list of integers, prop_ind_lst, as an argument.
#This list represents a collection of row indices of the commercial_properties_df DataFrame. 
#The method must check that the commercial_properties_df has an ‘Address’ column, if it doesn’t then it must call the create_address method.
#You will then need to extract the addresses in the DataFrame from each of the random indices contained in prop_ind_lst and store them in a separate list. 
#Once you’ve done this you will call get_lat_lon function, which is provided, to help you retrieve the latitude and longitude coordinates for each address. 
#You must return whatever the get_lat_lon function returns.
#Check get_lan_lon function’s DocString and source code to learn how to use the function, i.e. how to call the function and what it returns.
#• create_map - This method takes the following arguments: num_prop, which is number of random properties you’d like to select from the DataFrame, can be an int or float between [0, 1], map_folder_path, where the map that is created will be saved (this should be in the data/my_maps folder which you will need to create if it doesn’t exist. 
#Use the os module to do this), and finally city, where the properties are, in our case this should be Denver.
#The method will make a call to the random_properties method, the _lat_long method and the make_map helper function provided. 
#Please read the DocString and source code to learn how it works (how to call it and what it returns).
#Make all the necessary calls with the necessary arguments to each function mentioned above in the correct order. Once you make all the necessary calls, you will need to save the resulting map as a .html file in the my_maps folder called denver_map.html. 
#You will need to check the folium.Map documentation to figure out how.

#Step 2: Implement a custom argument parser (15 pts)
#Inside of run.py create a function called main which takes no arguments and creates your custom argparser. 
#Make the necessary changes so your code works with command line arguments as well as the hard coded arguments you used in Step 1.
  
#Step 3: Write unit tests (15 pts)
#Write all the necessary unit tests for Step 1. 
#Note that you will need to test every method except for create_map.

#Upload
#Please ZIP the Extra_credit folder containing all folders and files described above including the data file. 
#Your code must be in the same hierarchy as shown at the beginning of the homework.
