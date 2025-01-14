#COMP 3006
#Homework 1 - Functional programming and OOP intro
#General Homework Guidelines:
#- Homework must be submitted in a .py file. Please do not submit .ipynb files.
#- Homework should not use packages or functions that have not yet been discussed in class.
#- Use comments to explain what your code is doing.
#- Use a consistent coding style.
#- Use descriptive variable names.
#- Test your code regularly using a variety of different inputs.
#- Every function must include a docstring for documentation (see: https://realpython.com/documenting-python-code/). This docstring should include:
#- 1 or 2 lines describing what the function does
#- Args: input parameters, their types and what they are for
#- Returns: return data type and what it is
#- All tests of your functions should be commented out in your final submission or enclosed with an if __name__=='__main__' codeblock.
#- All functions should use return statements to return a value, 
#rather than printing some value, unless the instructions specifically say to print.

# Question 1:
# Write a function called paired_list that takes in two non-empty lists : a list of strings and
# a list of integers. The function must combine the lists to form a single list and return it.
# The lists do not need to be the same length. If the lists are the same length, then the values
# should be paired up using a value from each list to form a tuple, i.e. ['Matt', 'Alice'] and
# [99, 50] should result in the list [('Matt',99), ('Alice',50)].
# If the lists are not the same length, you should still pair up the values from each list but
# you'll need to handle two cases:
# -if the list containing strings is longer, you should use the placeholder value 'FNU' which stands
# for "first name unknown". Fro example for the lists ['Matt', 'Alice'] and [99, 50, 25] should result
# in the list [('Matt',99), ('Alice',50), ('FNU', 25)].
# -if the list containing integers is longer, you should use the average value of the integer list
# as the value you pair up with the extra strings, i.e. for ['Matt', 'Alice', 'Tom', 'Jake'] and
# [99, 50, 25] should result in the list [('Matt',99), ('Alice',50), ('Tom',25), ('Jake', 58)]. The
# last value 58 is (99+50+25)//3. Please note that "//" is integer division, so the result is rounded down.
# You can use a helper function to calculate the average value of the integers list.
# Note: you may find the itertools module helpful.

# Question 2:
# Write a function called even_odd_pairs which takes a list of tuples (the output of paired_list function)
# and a boolean value, which should have a default value of True. If the boolean value is True, the function
# should filter the list of tuples and return a list containing only the tuples that have an even interger.
# For example if given [('Matt',99), ('Alice',50), ('FNU', 25)] and True, then the function should return
# [('Alice',50)].
# If the boolean value is False, the function should filter the list of tuples and return a list containing
# only the tuples that have an odd interger. For example if given [('Matt',99), ('Alice',50), ('FNU', 25)]
# and True, then the function should return [('Matt',99), ('FNU', 25)].

### ----------------------------------------------------------------------------------------- ###
### We wish to compare and store data on various types of shelters for when we go backpacking ###
### ----------------------------------------------------------------------------------------- ###

#Question 3:
#Create a class, called Tent, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# sqft (float)
# vestibule (bool, True if tent has a vestibule)
# weight (ounces, float)
# structure_poles (bool, True if tent has structural poles. Should have a default value of True)
# seasons (int, 3 or 4. Should have a default value of 3)
#The class should also have the following methods:
# __str__, no particular format is required
# __repr__, no particular format is required
# __lt__ (this should use the num_occupants and sqft attributes to determine if one tent is
# less than another tent, please note that both attributes must be less in order to return True)
# is_better (a tent is considered better if and only if its weight and setup_time is less than
# another tent whilst having equal or better season rating, 4 is better than 3. Again, both
# attributes must be less)
#For example (__lt__ and is_better works similar for questions 4 and 5):
# tent1=Tent(num_occupants=4, material="polyester", setup_time=6, sqft=36, vestibule=False
# weight=12.5, structure_poles=True, seasons=3
# tent2=Tent(num_occupants=4, material="polyester", setup_time=5, sqft=35, vestibule=False
# weight=11.5, structure_poles=True, seasons=3
# tent3=Tent(num_occupants=3, material="polyester", setup_time=4, sqft=35, vestibule=False
# weight=11.0, structure_poles=True, seasons=4
# tent1 < tent2 --> False (num_occupant is equal, not less)
# tent1 < tent3 --> False (num_occupant and sqft are greater)
# tent3 < tent1 --> True (num_occupant and sqft are less)
# tent3 < tent2 --> False (num_occupant is less but sqft is the same)
# tent2.is_better(tent1) --> True (weight and setup_time for tent2 are less whilst maintaining
# the same season rating)
# tent3.is_better(tent1) --> True (weight and setup_time for tent2 are less and the season
# rating is better)
# tent1.is_better(tent2) --> False (heavier and longer setup_time)

#Question 4:
# We wish to compare and store data on various types of shelters for when we go backpacking.
# Create a class, called Hammock, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# weight (ounces, float)
# length (int, length of hammock in feet. Should have a default value of 11)
# seasons (int, 3 or 4. Should have a default value of 3)
#The class should also have the following methods:
# __str__
# __repr__
# __lt__ (this should use the weight and setup_time attributes to determine if one hammock is
# less than another hammock, please note that both attributes must be less in order to return True)
# is_better (a hammock is considered better if and only if its weight and setup_time is less than
# another hammock whilst having equal or better season rating, 4 is better than 3)

#Question 5:
# Create a class, called Tarp, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# sqft (float)
# weight (ounces, float)
# seasons (int, 3 or 4. Should have a default value of 3)
#The class should also have the following methods:
# __str__, no particular format is required
# __repr__, no particular format is required
# __lt__ (this should use the num_occupants and sqft attributes to determine if one tarp is
# less than another tarp, please note that both attributes must be less in order to return True)
# is_better (a tarp is considered better if and only if its weight and setup_time is less than
# another tarp whilst having equal or better season rating, 4 is better than 3)

#Question 6 (optional):
# There is lots of repeated code above, let's create a parent class for Tent, Hammock and Tarp
# called Shelter. The Shelter class should have:
# -a constructor that takes over all of the attributes that are common for Tent, Hammock and Tarp
# -is_better method should be moved to the parent class from the Hammock, Tent and Tarp classes
# since it uses weight, setup_time and season rating in the respective classes.
# -total_sleep_spots which will add up the total number of sleeping spots available from a
# non-determined number of Shelters being passed into the method.
# -__str__ and __repr__ methods must also be defined inside of Shelter, no particular format is required
# -last but not least, the __lt__ method must be rewritten in the child classes, Hammock, Tent and
# Tarp, to handle only the cases of comparing two objects of the same subclass (Hammock/Hammock,
# Tent/Tent, Tarp/Tarp) using the same attributes used for the respective class in questions 3 thru 5.
# If you are trying to compare two objects of different subclasses of Shelter, the Shelter class must
# handle those comparisons using the num_occupants, weight and setup_time.
# Rewrite the Tent, Hammock and Tarp classes taking into account the changes brought on by using
# the Shelter parent class. Changes will be needed to the constructor, __lt__ and the removal of
# the method is_better.










#Question 1
#List of Strings (Names)
names = ['Adan', 'Brisa', 'Carly', 'Diane', 'Eddie', 'Grandma', 'Ivy']
#List of Integers (Ages)
ages = [46, 21, 29, 60, 40, 71, 2]

#Function to combine Names List and Age List into Tuples
def paired_list(names, ages):
    #- This function takes two lists and combines them into one list and returns it. 
    #- Args: List Names - Strings and List Ages - Integers
    #- Returns: Returns Tuples of Names and Ages together in a List
    paired = list(zip(names, ages))
    return paired

result = paired_list(names, ages)
print(result)

#Function to calculate the Average Age in the List of Ages - Integers
def calculate_average(integers):
    #- This function calculates the average of the Integers in the Ages List
    #- Args: List Ages - Integers
    #- Returns: Returns the Average of the Integers as an Integer (Note: integer division rounds down)
    if len(integers) == 0:
        return 0
    return sum(integers) // len(integers)

average = calculate_average(ages)
print(f"The average age is {average}.")



#Question 2
#Function to take a List of Tuples abd filter based on Even or Odd
def even_odd_pairs(paired_list, filter_even=True):
    #- This function takes a List of Tuples abd filter based on Even or Odd
    #- Args: paired_list: List of Tuples (name, age) - Strings and Integers
    #- Returns: Returns List of Tuples - Integers
    if filter_even:
        #Filter for Even Ages - Integers
        return [pair for pair in paired_list if pair[1] % 2 == 0]
    else:
        #Filter for Odd Ages - Integers
        return [pair for pair in paired_list if pair[1] % 2 != 0]
    
even_pairs = even_odd_pairs(result, filter_even=True)
odd_pairs = even_odd_pairs(result, filter_even=False)
print(f"Even Pairs: {even_pairs} Odd Pairs: {odd_pairs}")



### ----------------------------------------------------------------------------------------- ###
### We wish to compare and store data on various types of shelters for when we go backpacking ###
### ----------------------------------------------------------------------------------------- ###



#Question 3
#Tent Class that contains the Required Attributes (8)
class Tent:
    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles=True, seasons=3):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.vestibule = vestibule
        self.weight = weight
        self.structure_poles = structure_poles
        self.seasons = seasons

    #Required String Defining Method
    def __str__(self):
        return f"Tent for {self.num_occupants} occupants, material: {self.material}, setup time: {self.setup_time} minutes, size: {self.sqft} sqft, weight: {self.weight} oz, seasons: {self.seasons}"

    #Required String Representation Method
    def __repr__(self):
        return f"Tent({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, {self.vestibule}, {self.weight}, {self.structure_poles}, {self.seasons})"

    #Required Less Than Method
    def __lt__(self, other):
        if isinstance(other, Tent):
            return self.num_occupants < other.num_occupants and self.sqft < other.sqft
        return NotImplemented

    #Required Comparison Method
    def is_better(self, other):
        if isinstance(other, Tent):
            return self.weight < other.weight and self.setup_time < other.setup_time and self.seasons >= other.seasons
        return NotImplemented

#Create Tents
tent1 = Tent(num_occupants=4, material="polyester", setup_time=6, sqft=36, vestibule=False, weight=12.5, structure_poles=True, seasons=3)
tent2 = Tent(num_occupants=4, material="polyester", setup_time=5, sqft=35, vestibule=False, weight=11.5, structure_poles=True, seasons=3)
tent3 = Tent(num_occupants=3, material="polyester", setup_time=4, sqft=35, vestibule=False, weight=11.0, structure_poles=True, seasons=4)

#Testing Less Than Method
print(f"Tent 1 is < Tent 2: {tent1 < tent2}")
print(f"Tent 1 is < Tent 2: {tent1 < tent3}")
print(f"Tent 1 is < Tent 2: {tent2 < tent1}")
print(f"Tent 1 is < Tent 2: {tent2 < tent3}")
print(f"Tent 1 is < Tent 2: {tent3 < tent1}")
print(f"Tent 1 is < Tent 2: {tent3 < tent2}")

#Testing Is Better Method
print(f"Tent 1 is better than Tent 2: {tent1.is_better(tent2)}")
print(f"Tent 1 is better than Tent 2: {tent1.is_better(tent3)}")
print(f"Tent 1 is better than Tent 2: {tent2.is_better(tent1)}")
print(f"Tent 1 is better than Tent 2: {tent2.is_better(tent3)}")
print(f"Tent 1 is better than Tent 2: {tent3.is_better(tent1)}")
print(f"Tent 1 is better than Tent 2: {tent3.is_better(tent2)}")



#Question 4
#Hammock Class that contains the Required Attributes (6)
class Hammock:
    def __init__(self, num_occupants, material, setup_time, weight, length, seasons=3):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.length = length
        self.seasons = seasons

    #Required String Defining Method
    def __str__(self):
        return f"Hammock for {self.num_occupants} occupants, material: {self.material}, setup time: {self.setup_time} minutes, weight: {self.weight} oz, length: {self.length} feet, seasons: {self.seasons}"

    #Required String Representation Method
    def __repr__(self):
        return f"Hammock({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.length}, {self.seasons})"

    #Required Less Than Method
    def __lt__(self, other):
        if isinstance(other, Hammock):
            return self.weight < other.weight and self.setup_time < other.setup_time
        return NotImplemented

    #Required Comparison Method
    def is_better(self, other):
        if isinstance(other, Hammock):
            return self.weight < other.weight and self.setup_time < other.setup_time and self.seasons >= other.seasons
        return NotImplemented

#Create Hammocks
hammock1 = Hammock(num_occupants=1, material="nylon", setup_time=8, weight=19.5, length=13, seasons=3)
hammock2 = Hammock(num_occupants=2, material="polyester", setup_time=12, weight=22.0, length=10, seasons=3)
hammock3 = Hammock(num_occupants=2, material="nylon", setup_time=13, weight=24.5, length=115, seasons=4)

#Testing Less Than Method
print(f"Hammock 1 is < Hammock 2: {hammock1 < hammock2}")
print(f"Hammock 1 is < Hammock 2: {hammock1 < hammock3}")
print(f"Hammock 1 is < Hammock 2: {hammock2 < hammock1}")
print(f"Hammock 1 is < Hammock 2: {hammock2 < hammock3}")
print(f"Hammock 1 is < Hammock 2: {hammock3 < hammock1}")
print(f"Hammock 1 is < Hammock 2: {hammock3 < hammock2}")

#Testing Is Better Method
print(f"Hammock 1 is better than Hammock 2: {hammock1.is_better(hammock2)}")
print(f"Hammock 1 is better than Hammock 2: {hammock1.is_better(hammock3)}")
print(f"Hammock 1 is better than Hammock 2: {hammock2.is_better(hammock1)}")
print(f"Hammock 1 is better than Hammock 2: {hammock2.is_better(hammock3)}")
print(f"Hammock 1 is better than Hammock 2: {hammock3.is_better(hammock1)}")
print(f"Hammock 1 is better than Hammock 2: {hammock3.is_better(hammock2)}")


#Question 5
#Tarp Class that contains the Required Attributes (6)
class Tarp:
    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.sqft = sqft
        self.seasons = seasons

    #Required String Defining Method
    def __str__(self):
        return f"Tarp for {self.num_occupants} occupants, material: {self.material}, setup time: {self.setup_time} minutes, weight: {self.weight} oz, sqft: {self.sqft} sqft, seasons: {self.seasons}"

    #Required String Representation Method
    def __repr__(self):
        return f"Tarp({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.sqft}, {self.seasons})"

    #Required Less Than Method
    def __lt__(self, other):
        if isinstance(other, Tarp):
            return self.num_occupants < other.num_occupants and self.sqft < other.sqft
        return NotImplemented

    #Required Comparison Method
    def is_better(self, other):
        if isinstance(other, Tarp):
            return self.weight < other.weight and self.setup_time < other.setup_time and self.seasons >= other.seasons
        return NotImplemented

#Create Tarps
tarp1 = Tarp(num_occupants=3, material="canvas", setup_time=25, weight=24.5, sqft=100, seasons=3)
tarp2 = Tarp(num_occupants=4, material="polyester", setup_time=30, weight=29.0, sqft=105, seasons=3)
tarp3 = Tarp(num_occupants=5, material="nylon", setup_time=20, weight=18.5, sqft=115, seasons=4)

#Testing Less Than Method
print(f"Tarp 1 is < Tarp 2: {tarp1 < tarp2}")
print(f"Tarp 1 is < Tarp 2: {tarp1 < tarp3}")
print(f"Tarp 1 is < Tarp 2: {tarp2 < tarp1}")
print(f"Tarp 1 is < Tarp 2: {tarp2 < tarp3}")
print(f"Tarp 1 is < Tarp 2: {tarp3 < tarp1}")
print(f"Tarp 1 is < Tarp 2: {tarp3 < tarp2}")

#Testing Is Better Method
print(f"Tarp 1 is better than Tarp 2: {tarp1.is_better(tarp2)}")
print(f"Tarp 1 is better than Tarp 2: {tarp1.is_better(tarp3)}")
print(f"Tarp 1 is better than Tarp 2: {tarp2.is_better(tarp1)}")
print(f"Tarp 1 is better than Tarp 2: {tarp2.is_better(tarp3)}")
print(f"Tarp 1 is better than Tarp 2: {tarp3.is_better(tarp1)}")
print(f"Tarp 1 is better than Tarp 2: {tarp3.is_better(tarp2)}")



#Tests
def test_paired_list():
    #- This test function checks if Empty Lists return an Empty List. 
    #- Args: List Names - Strings - Empty and List Ages - Integers - Empty
    #- Returns: Returns an Empty List
    names_empty = []
    ages_empty = []
    expected_output_empty = []

    result_empty = paired_list(names_empty, ages_empty)
    assert result_empty == expected_output_empty, f"Test Failed: {result_empty}"

    print("The paired_list tests passed!")

def test_calculate_average():
    #- This test function checks the math for one input
    #- Args: One Integer
    #- Returns: The One Integer
    single_element = [30]
    expected_output_single = 30  
    result_single = calculate_average(single_element)
    assert result_single == expected_output_single, f"Test failed: {result_single}"
    
    #- This test function checks the math for Negative Integers
    #- Args: Negative Integers
    #- Returns: Returns the Average of the Integers as an Integer (Note: integer division rounds down)
    negative_values = [-13, -56, -329]
    expected_output_negative = -133
    result_negative = calculate_average(negative_values)
    assert result_negative == expected_output_negative, f"Test failed: {result_negative}"

    print("The calculate_average tests passed!")

def test_even_odd_pairs():
    #- This test function checks the comparison of Empty Lists
    #- Args: Args: List Names - Strings - Empty and List Ages - Integers - Empty
    #- Returns: Returns and Empty List
    empty_paired_list = []
    expected_empty = []
    result_empty = even_odd_pairs(empty_paired_list, filter_even=True)
    assert result_empty == expected_empty, f"Test failed: Expected {expected_empty}, but got {result_empty}"

    print("The even_odd_pairs test passed!")

#Run Tests
# if __name__ == '__main__':
#     test_paired_list()
#     test_calculate_average()
#     test_even_odd_pairs()

