#Week 3 Assignment – AutoMPG and Shelter Tests
#In this assignment, you will use the same auto-mpg data that was used in assignment 2. 
#You will also use the code for the classes: Shelter, Hammock, Tent and Tarp that you created in assignment 1 question 6.
#Please follow the steps outlined below.

#Preparation
#Please create a new folder called Assignment3 and place inside it the autompg.py file from assignment 2. 
#Also create a new module called shelter.py with the code from assignment 1 question 6.
#This should have the Shelter, Hammock, Tarp and Tent classes with the appropriate inheritance.
#Inside the Assignment3 folder, please create two new Python modules called test_autompg.py and test_shelter.py.
#Take care to set them up to be useful both as a module and as a program.

#Step 1: test_autompg.py
#In test_autompg.py implement a class called TestAutoMPG that inherits from unittest.TestCase class.
#This class should implement the following methods:
#• setUpClass – This method will instantiate an object of the AutoMPGData class that will be used for testing the code.
#• tearDownClass - This method will delete the auto-mpg.clean.txt file.
#• setUp – This method will simply print “setUp” to the console and nothing else.
#• tearDown - This method will simply print “tearDown” to the console and nothing else.
#• test_str – This method will check that the string being returned by the str method corresponds to the format AutoMPG('chevrolet','chevelle malibu’,1970,18.0)
#• test_eq – Checks that the __eq__ method is working as intended and is using all 4 attributes. Note that this method should only work between AutoMPG objects.
#• test_lt – Checks that the __lt__ method is working as intended and is using all 4 attributes. Note that this method should only work between AutoMPG objects.
#• test_hash – Checks that the has function is working properly.

#Every function must have a print statement that will print the message : “Executing test_name.” where test_name is the name of the current test being executed. 1

#Step 2: Modify Tent, Tarp, Hammock classes
#Complete the optional question from homework 1. Make all the modifications necessary to the Tent, Tarp and Hammock classes to consolidate the shared code into the Shelter class.
#You will also need to modify the Shelter, Hammock, Tent and Tarp classes str method, so that Hammock, Tent and Tarp make calls to the Shelter str method which will print each instance using the following format :
#• Shelter(num_occupants, material, setup_time, sqft (if applicable), vestibule (if applicable), weight, structure_poles (if applicable), seasons)

#Step 3: test_shelter.py
#In test_shelter.py implement a class called TestShelter that inherits from unittest.TestCase class.
#This class should implement the following methods:
#• setUpClass – This method will simply print “setUpClass” to the console and nothing else.
#• tearDownClass - This method will simply print “tearDown” to the console and nothing else.
#• setUp – This method will create instances of the Tent, Tarp and Hammock classes, as many as you think is needed to thoroughly test your code.
#• tearDown - This method will delete each instance of Tent, Tarp and Hammock that you created in the setUp method.
#• test_str – This method will check that the string being returned by the str method corresponds to the format . Shelter(num_occupants, material, setup_time, sqft (if applicable), vestibule (if applicable), weight, structure_poles (if applicable), seasons).
#• test_lt – Checks that the __lt__ method is working as intended. It should use the corresponding __lt__ methods based on the class of the object.
#• test_is_better – Checks that the is_better method is working as intended.

#Every function must have a print statement that will print the message : “Executing test_name.” where test_name is the name of the current test being executed.

#Upload
#Please ZIP the Assignment3 folder containing the autompg.py, test_autompg.py, shelter.py and test_shelter.py files and upload to Canvas.




#Homework 1 Solution to Number 6 (Optional)
# class Tent:
#   def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, \
#               structure_poles=True, seasons=3) -> None:
#     self.num_occupants = num_occupants
#     self.material = material
#     self.setup_time = setup_time
#     self.sqft = sqft
#     self.vestibule = vestibule
#     self.weight = weight
#     self.structure_poles = structure_poles
#     self.seasons = seasons

#   def __lt__(self, other):
#     if type(self) == type(other):
#       return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
#     return NotImplemented

#   def __str__(self) -> str:
#      return self.__repr__()

#   def __repr__(self) -> str:
#      return f"Tent({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, \
#             {self.vestibule}, {self.weight}, {self.structure_poles}, {self.seasons})"
  
#   def is_better(self, other) -> bool:
#         if type(self) == type(other):
#           return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
#             (self.seasons >= other.seasons)
#         return NotImplemented

# class Hammock:
#   def __init__(self, num_occupants, material, setup_time, weight, length=11, seasons=3) -> None:
#     self.num_occupants = num_occupants
#     self.material = material
#     self.setup_time = setup_time
#     self.weight = weight
#     self.length = length
#     self.seasons = seasons

#   def __lt__(self, other):
#     if type(self) == type(other):
#       return (self.weight < other.weight) and (self.setup_time < other.setup_time)
    
#     return NotImplemented

#   def __str__(self) -> str:
#      return self.__repr__()

#   def __repr__(self) -> str:
#      return f"Hammock({self.num_occupants}, {self.material}, {self.setup_time}, \
#             {self.weight}, {self.length}, {self.seasons})"
  
#   def is_better(self, other) -> bool:
#         if type(self) == type(other):
#           return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
#             (self.seasons >= other.seasons)
#         return NotImplemented

# class Tarp:
#   def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3) -> None:
#     self.num_occupants = num_occupants
#     self.material = material
#     self.setup_time = setup_time
#     self.sqft = sqft
#     self.weight = weight
#     self.seasons = seasons

#   def __lt__(self, other):
#     if type(self) == type(other):
#       return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
#     return NotImplemented

#   def __str__(self) -> str:
#      return self.__repr__()

#   def __repr__(self) -> str:
#      return f"Tarp({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, \
#             {self.weight}, {self.seasons})"
  
#   def is_better(self, other) -> bool:
#         if type(self) == type(other):
#           return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
#             (self.seasons >= other.seasons)
#         return NotImplemented





# https://archive.ics.uci.edu/ml/datasets/Auto+MPG
# https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data
# https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.names
