#COMP3006
#Homework 2 - AutoMPG Data Set Overview

#In this assignment, you will download a publicly available data set and develop some classes that will be useful in working with the data. 
#The data set contains information about fuel efficiency for some different automobiles.
#Please follow the steps outlined below.

#Preparation
#Review the links below that describe the AutoMPG data set that is part of the UCI Machine Learning Repository. 
#This data set consists of 398 records each having nine attributes. 
#Please download the data and save it in a file called auto-mpg.data.txt.
#• https://archive.ics.uci.edu/ml/datasets/Auto+MPG
#• https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data
#• https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.names

#Please create a new Python module in a file autompg.py, taking care to set it up to be useful both as a module and as a program.

#Step 1: AutoMPG class
#In autompg.py implement a class that represents these attributes that are available for each record in the data set:
#• make – String. Automobile manufacturer. First token in the “car name” field of the data set.
#• model – String. Automobile model. All the other tokens in the “car name” field of the data set except the first.
#• year – Integer. Automobile year of manufacturer. This is the four-digit year that corresponds to the “model year” field of the data set.
#• mpg – Float. Miles per gallon. This is a floating point value that corresponds to the “mpg” field of the data set.

#This class should implement the following methods:
#• __init__ – Constructor that takes four parameters after self and initializes the attributes described above.
#• __repr__ and __str__ – Returns the string representation of the object. One of these can call the other one. 
#• __eq__ – Implements equality comparison between two AutoMPG objects. 
            #Should use all four attributes and should only work between AutoMPG objects.
#• __lt__ – Implements less-than comparison between two AutoMPG objects. 
            #Should use all four attributes in the order described above (e.g., if the “make” is the same, then the model should be used).
#• __hash__ – Implement an appropriate hash function for these objects.

#Step 2: AutoMPGData class
#In autompg.py define the AutoMPGData class. 
#This class represents the entire AutoMPG data set. 
#It has a single attribute data that is a list of AutoMPG objects. 
#One issue with the Auto MPG data set is that in the data file, most of the fields are separated by spaces, but the separator before the “car name” field is a TAB character. 
#This makes it difficult to parse with Python’s csv module, so there is a method described below (_clean_data) that takes care of this and saves the “cleaned” data file in auto-mpg.clean.txt. 
#This class should implement these methods:
#• __init__ – Constructor that takes no arguments. It should call the _load_data method described below.
#• __iter__ – Method to make the class iterable. It should return an iterator over the data list.
#• _load_data – Method that will load the cleaned data file (auto-mpg.clean.txt)and instantiate AutoMPG objects and add them to the data attribute. 
            #See below for more details about a useful technique for parsing the data. 
            #This method should call _clean_data if the clean data file does not exist. (Hint: Use os.path.exists to check this.)
#• _clean_data – Method that will read the original data file line by line (auto-mpg.data.txt) and use the expandtabs method available on str objects to convert the TAB character to spaces. 
#Each line should be written to the “cleaned” file auto- mpg.clean.txt.
              
#Parsing Notes
#The main goal of the _load_data method is to read in the data file and instantiate objects of type AutoMPG using a few of the fields that are available. 
#Here are some notes about how to accomplish this:

#• Use the csv module to parse each line with space delimiters and ignore multiple sequential delimiters.
#• This will give you a list of nine elements that correspond to the columns in the data file.
#• Use collections.namedtuple to define a class called Record that has nine attributes that correspond to the nine data fields in the same order as in the file.
#• Using tuple packing/unpacking, assign the list returned by the csv module for a row to create a Record object.
#• Use the attributes of the Record object to pass the appropriate values to the constructor for AutoMPG.
#• You will need to use str.split and str.join to pick out the make and model values from the data since they are contained within “” in the data file, so will be returned by the csv module as a single string value.
                                                                                                                                                
#Step 3: main
#In autompg.py implement a main function that instantiates an AutoMPGData object and then uses the iterator protocol (e.g., for a in AutoMPGData():) to loop across the object, printing each AutoMPG object. 
                                                                                                                                                
#For example, the output should look like this:
#> python3 autompg.py
#AutoMPG('chevrolet','chevelle malibu',1970,18.0)
#AutoMPG('buick','skylark 320',1970,15.0)
#AutoMPG('plymouth','satellite',1970,18.0)
#AutoMPG('amc','rebel sst',1970,16.0)
#AutoMPG('ford','torino',1970,17.0)

#Upload
#Please combine autompg.py and your data files into a single ZIP file.


from collections import namedtuple
import csv


class AutoMPG:
    def __init__(self, make, model, year, mpg):
        #- Implements a class that represents the attributes that are available for each record in the data set.
        #- Args: Attributes of the Data Set
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
    
    #Required String Representation Method
    def __repr__(self):
        return f"AutoMPG(make='{self.make}', model='{self.model}', year={self.year}, mpg={self.mpg})"

    #Required String Defining Method
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.mpg} MPG"

    #Required Double Underscore (==) Method
    def __eq__(self, other):
        if isinstance(other, AutoMPG):
            return (
                self.make == other.make and
                self.model == other.model and
                self.year == other.year and
                self.mpg == other.mpg
            )
        return NotImplemented

    #Required Less Than Method
    def __lt__(self, other):
        if isinstance(other, AutoMPG):
            return (
                (self.make, self.model, self.year, self.mpg) < 
                (other.make, other.model, other.year, other.mpg)
            )
        return NotImplemented

    #Required Hash Method
    def __hash__(self):
        return hash((self.make, self.model, self.year, self.mpg))

class AutoMPGData:
    def __init__(self):
        #- Intializes the Object with the Aata and Loads the Aata
        #- Args: Self
        self.data = []
        self._load_data()

    #Required Iterable Method
    def __iter__(self):
        return iter(self.data)

    def _load_data(self):
        #- This Method Tries to Open a "Clean File" and if there isn't one, it Creates One Recursively
        #- Args: Self
        #- Retruns: Clean File
        clean_file = "auto-mpg.clean.txt"
        original_file = "auto-mpg.data.txt"
        Record = namedtuple("Record", [
            "mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"
        ])

        try:
            with open(clean_file, "r") as file:
                reader = csv.reader(file, delimiter=" ", skipinitialspace=True)
                for row in reader:
                    row = [col for col in row if col]
                    if len(row) < 9:
                        continue

                    record = Record(*row[:8], " ".join(row[8:]))
                    mpg = float(record.mpg)
                    year = 1900 + int(record.model_year) if int(record.model_year) >= 70 else 2000 + int(record.model_year)
                    make, model = record.car_name.split(" ", 1) if " " in record.car_name else (record.car_name, "")

                    self.data.append(AutoMPG(make, model, year, mpg))
        except FileNotFoundError:
            self._clean_data(original_file, clean_file)
            self._load_data()

    def _clean_data(self, original_file, clean_file):
        #- Opens the file in Read Mode, then Write Mode, Replaces Tabs with Spaces
        #- Args: Self, Raw File, and Clean File
        #- Returns: Clean File
        try:
            with open(original_file, "r") as infile, open(clean_file, "w") as outfile:
                for line in infile:
                    outfile.write(line.expandtabs())
        except PermissionError as e:
            print(f"Permission error: {e}")
            print("Ensure you have the necessary permissions to create or write to the file.")
            raise

if __name__ == "__main__":
    dataset = AutoMPGData()
    for car in dataset:
        print(car)
