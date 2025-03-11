#Week 10 Assignment – Command Line Interface
#In this assignment, you will begin working with a public data set from the National Oceanic and Atmospheric Administration and compute some basic statistics over the data.

#Preparation
#Download the Boulder, CO, daily station data for 2018, which is part of the data collected in the U.S. Climate Reference Network (USCRN). 
#Save this file as Data.txt using the “Save As” option in your browser and move it to the directory you are using for this assignment.
#All testing code must be inside an if __name__==“__main__”.
#You will be executing some of these files from the command line so you may need to use python instead of python3 when running form your files.

#Structure
# Assignment10: (folder)
#Step 1 files:
#———Data.txt (will create this)
#———T_DAILY_AVG.txt (will create this)
#——— T_DAILY_AVG_sorted.txt (will create this)
#———Week10_Part1.txt (will create this)
#———compute_stats.py (will create this)
#Step 2 files:
#———main.py
#———program: (package)
#——————autompg.py
#——————custom_logger.py
#——————logs: (folder)
#—————————my_log.log
#——————data: (folder)
#—————————auto-mpg.data.txt
#—————————auto.data.year.txt (will create this)
#—————————auto.data.mpg.txt (will create this)
#—————————auto.data.year.mpg.txt (will create this)

#Step 1: Data Preparation
#The description of the data file format contains a lot of useful information. 
#Please read through it. 
#Not everything is important, but definitely Sections 4 and 5 deserve some attention. 
#We are interested in Field 9, T_DAILY_AVG.
#The program being developed (see Step 2 below) expects its data to come in sorted numerically ascending, one value per line, so we need to use some command-line tools to take care of this.

#Step 1.a: Extract the column of data
#Using the command-line program cut, extract just Field 9 from the data file and save it in a file called T_DAILY_AVG.txt. 
#You will need to read the documentation of the cut program (e.g., man cut) to figure out exactly what options are needed, but it will be something like this:
#cut [cut-options] Data.txt > T_DAILY_AVG.txt
#Step 1.b: Sort the column of data
#The next step is to sort the data numerically using the sort program. 
#The sorted data should be saved in a file named T_DAILY_AVG_sorted.txt. 
#Please read the documentation of sort (e.g., man sort) to figure out how to do this. 
#The general form of the command will be:
#sort [sort-options] T_DAILY_AVG.txt > T_DAILY_AVG_sorted.txt
#Step 1.c: Do it in a pipeline
#As shown in lecture, commands can be combined in a pipeline without saving the intermediate data into files. 
#We could do all of the above in one shot so that the numerically sorted, ascending data is piped directly to a Python program something like this:
#<cut command> | <sort command> | python compute_stats.py
#Note: you may need to use python3 on your computer
#Step 1 Deliverable: Create a document called Week10_Part1.txt containing the three command lines for Parts 1.a, 1.b, and 1.c.

#Step 2: compute_stats.py
#In this part of the assignment, you will implement a Python function, called my_stats, that takes the values from the data coming from standard input. 
#You will want to use sys.stdin to do this). 
#It then computes some basic statistics over the values that are read in, and returns those statistics to standard output. 
#Once the data has gone to standard output you must pipe the data into a file called compute_stats_results.txt 
#This program will be implemented in a file called compute_stats.py.
#This program will assume that the data is read in a stream of numbers, one per line.
#The data coming in will have already been sorted numerically in ascending order (i.e., what you did in Part 1). 
#There might be “missing-data” values (read the data file documentation) that must be ignored when computing the statistics.
#The statistics that must be computed are
#1) Average value
#2) Minimum value
#3) Maximum value
#4) Median value
#Before your program terminates, it should print the computed values with the following format :
#min: -17.9, max: 17.1, average: 2.5414835164835163, median: 1.65
#Using the appropriate command on the command line, take the output from above and store it in the file compute_stats_results.txt

#Step 3: main.py
#This module will implement an argparser inside a function called my_parser. 
#Import pandas and numpy
#This function should take no arguments and it should create and return an argument parser with the following arguments: 
#Add an optional argument called w
#• log - This should be a positional (required) argument which takes in a folder path where your program will write log files to when using autompg2, make this argument type string. 
#For this assignment the logs should be saved inside the “logs” folder. 
#Write the help message as “Name of log file my_1og.log”
#• save - This should be a positional (required) argument which takes in a folder path where your program will save the sorted data, make this argument type string. 
#For this assignment the data files should be saved inside the “data” folder. 
#Should have the help message “Store output in log file!!”
#• -y, --year - This should be an optional argument which when given, results in the “data” attribute of the AutoMPGData class being sorted by year.
#• -m, --mpg - This should be an optional argument which when given, results in the “data” attribute of the AutoMPGData class being sorted by mpg.
#You will be running main.py from the command line, this means that you will create the instance of the AutoMPGData class in this module inside of an if __name__ == “__main__” block. 
#So make sure that your file paths and relative/absolute imports are done correctly and that when you execute your code from the command line that you’re inside the Assignment10 folder (use pwd, cd and ls in your terminal to check).
#You will use the arguments passed in from the command line to instantiate the AutoMPGData class object and use some of the methods defined in the class.
#Note: for -y/--year and -m/--mpg you will want to use the an argument which has “action=‘store_true’”, which creates an argument that stores False by default. 
#I.e. when the corresponding flag isn’t passed in, and it stores True when given the corresponding flag. 
#For example: python3 main.py 
#Namespace(year=False, mpg=False)
#python3 main.py --year
#Namespace(year=True, mpg=False)
#python3 main.py -y -m
#Namespace(year=True, mpg=True)

#Step 4: custom_logger.py
#This module will contain a custom logger function, called my_logger, which will take one argument, which is the file path where the log files will be saved to. 
#The format should be “timestamp::line::message”.
#The logger will have a level of DEBUG. Log the message “Working”

#Step 5: autompg.py
#You will now use the arguments read in from the command line which will be handled by the argument parser in main.py module to improve the AutoMPGData class used in assignment 2. 
#You will use assignment 2’s solution which was provided in week 3 and the auto-mpg.data.txt file. 
#You will enhance the class by modifying/adding the following methods:
#• __init__ - The constructor must now take 2 additional arguments: sort_year and sort_mpg, both of type boolean. 
#The constructor then stores these values into the attributes: sort_year and sort_mpg. 
#The constructor must also log a debug level message “Data loaded.” once it has successfully loaded the data (you will need to import the logger function created inside the custom_logger module defined above).
#• sort_data - New method which takes no arguments and sorts the data by year, or by mpg, or by year and then by mpg based on the values of the attributes sort_year and sort_mpg. 
#The method should return the sorted dataframe. 
#Remember that the AutoMPGData stores the data inside of a list of namedtuples, keep that in mind when trying to sort the data. 
#Write an if statement checking if sort_year or sort_mpg is True, and create an attribute called working and set it to True.
#• save_data - New method which takes a file_path argument and saves the data to the given location (this path is passed in from the command line and my_parser will read it and store it). 
#The file name must have the format : “auto.data.X.txt” where “X” can be “year”, “mpg” or “year.mpg” based on the sort_year and sort_mpg attribute values. 
#If the “sort_year” and “sort_mpg” are both False, then save the file simply as “auto.data.txt”. 
#Once the method saves the file it should write a message to the logger “Data saved, sorted by X !!! ”, where “X” can be “year”, “mpg” or “year.mpg” based on the sort_year and sort_mpg attribute values. 
#If the file was not sorted then the log message should be “Data saved, not sorted.!!!”
#This code will be executed from the command line using commands of the following form (you can use the short flags or the long one, it doesn’t make a difference):
#python3 main.py path/to/log/folder path/to/save/data -y -m.
#python3 main.py path/to/log/folder path/to/save/data -year -mpg.
#path/to/log/folder and path/to/save/data are both required arguments and must be given in the correct order (that is what makes them “positional”). 
#Also remember that depending on your set up you may need to use python instead of python3.

#Upload
#Please ZIP the Assignment10 folder containing all folders and files described above including the data files. 
#Your code must be in the same hierarchy shown at the beginning of the homework.
