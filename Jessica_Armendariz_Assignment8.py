#Week 8 Assignment – Numpy and Matplotlib

#In this assignment you will be working with multiple data files created by the Social Security Administration, containing the total number of births for each sex/name combination. 
#The data starts in the year 1880 and goes all the way through 2022. 
#Your job will be to inspect the data and visualize the different trends that are in the data.

#Preparation
#Please download the Assignment 8 zip file. 
#Within the zipped file you should find a folder, called baby_names which contains all of your data.
#Make sure that you have numpy and matplotlib installed on your computer:
#pip3 install numpy (Mac) pip install numpy (Windows)
#pip3 install matplotlib (Mac) pip install matplotlib (Windows)
#All testing code must be inside an if __name__==“__main__”.
#Structure
#Assignment8: (folder)
#———main.py
#———contents: (package)
#——————babynames.py
#——————baby_names: (folder)
#—————————1800s: (folder)
#————————————yob1880.txt
#————————————yob1881.txt
#————————————…
#—————————1900s: (folder)
#————————————00s: (folder)
#———————————————yob1900.txt
#———————————————yob1901.txt
#———————————————…
#————————————10s: (folder)
#————————————…
#—————————2000s: (folder)
#————————————…
#——————helper_functions: (package)
#—————————hf.py

#Step 1: Helper Functions
#You will need to create a new package called helper_functions which will contain hf.py module. 
#In this module you will need to write a helper function, called retrieve_files, which takes a file extension (“.txt”, “.csv”, etc…) as an argument. 
#The function will traverse every folder in the Assignment 8 directory. 
#It will create and return a list containing the path and file name for every file that has the file extension passed into the function. 
#For an extension of .txt you’ll have [./path/to/your/file/file1.txt, ./path/to/ your/file/file2.txt,…]. 
#You may want to use the os module to accomplish this.
#You will also create a generator, called record_loader_gen, which will take a list containing file paths and names:
#([./path/to/your/file/file1.txt, ./path/to/your/file/ file2.txt,…]) as an argument. 
#The function must then open a file and yield each line from every file. 
#Each record line you’re yielding should be composed of the name, gender, births and year. 
#You will need to use a regular expression to extract the year from the file name. 
#You will also need to cast the births and year to an int in order perform mathematical operations on the values later on.

#Step 2: BabyNames class
#This class will be defined inside babynames.py module. This class should implement the following methods:

#• __init__ – Constructor takes no arguments and creates a pandas DataFrame attribute which will load the data from all of the yobxxxx.txt files located inside the baby_names folder. 
#When creating the names_df attribute you will need to use the helper function and generator to load in the data. 
#Once the data is loaded you will make a call to the method sort_data explained below.

#• names_df: this is a pandas DataFrame.

#• sort_data – Method takes no arguments and sorts the names_df DataFrame in ascending order by year, i.e. you should have the entries for 1880 first, then 1881 and so on.

#• m_f_names - Method takes a starting year, should have a default value of 1880 and an ending year, should have a default value of 2022, as arguments. 
#It calculates the total number of male and female births for each year and creates a line plot of the data. 
#The x-axis should be the years. 
#The graph should have an appropriate title, legend, x and y axis labels.

#• most_popular_ever - Method takes no arguments, it calculates the top 3 most popular names throughout history and plots their evolution over the years. 
#You should use a regular line plot (don’t use a scatter nor histogram). 
#The x-axis should be the years. 
#The graph should have an appropriate title, legend, x and y axis labels.

#• unisex - Method takes no arguments, it calculates for each year the total number of births for every name that was given to both men and women and creates a bar plot over the years. 
#The x-axis should be the years. 
#The graph should have an appropriate title, legend, x and y axis labels. 
#You can use the command plt.tick_params(axis=‘x’,which=‘major’,labelsize=7) to make the years more readable (you might need to change labelsize)

#• unisex_evolution - Method takes no arguments, it adds every name that was given to both men and women to a set. 
#It should print the set to the screen and ask the user to pick as many names as they want until they enter ‘q’, and store their input. 
#Your code must verify that the user entered a valid name before storing it. 
#Your code must then plot the total number of births over the years for each name that the user gave you.

#Step 3: main.py
#This should make all the necessary imports so that it can create an instance of the BabyNames class and test every method in the class.

#Upload
#Please ZIP the Assignment8 folder containing all folders and files described above including the data files. 
#Your code must be in the same hierarchy shown at the beginning of the homework.
