#January 07 - Week 1 - Day 1

#There are homework guidelines for submitting each assignment
#Functions and Variables = snake_case
#Class Names = CamelCase





#Janaury 09 - Week 1 - Day 2

#Class names are written as:

# class Point3D:
#     pass

# class Student():
#     """
#     Student Class: Creates little students...
#     """
#     pricePerCredit = 1500
#     num_of_students = 0

#     def __init__(self, first, last, credits):
#         self.first_name = first
#         self.last_name = last
#         self.email = first + "." + last + "@du.edu"
#         self.num_credits = credits
#         self.tuitionCost = credits * self.pricePerCredit
#         self.tuitionCost = credits * Student.pricePerCredit

#         # Why use a class variable ?
#         Student.num_of_students += 1
    
#     def fullname(self):
#         return self.first_name + " " + self.last_name

#     def tuition(self):
#         self.tuitionCost = self.num_credits * Student.pricePerCredit

# student1 = Student("Daniel", "Parada", 8)
# print(student1.tuitionCost)
# student1.pricePerCredit = 1400
# student1.tuition()
# print(student1.tuitionCost)

# print(student1.tuitionCost)

# # Let's check the name space for our class and instances :
# print(Student.__dict__)
# print(student1.__dict__)

# # Make it more readable :
# for attr in Student.__dict__:
#     print(attr)

# for attr in student1.__dict__.values():
#     print(attr)





#January 14 - Week 2 - Day 3 (Did Not Attend Class)





#January 16 - Week 2 - Day 4

#private variables - only visible inside the class
#creating a private variables is two underscores 
#__private_variable = "This is a private variable"





#January 21 - Week 3 - Day 5 (Did Not Attend Class)





#January 23 - Week 3 - Day 6

#Unit testing needs to be imported and formatted correctly based on examples provided
#Module we need to import for writing unit tests :

# import unittest
# import CE1_classes

# class TestFunctions(unittest.TestCase):
#     """
#     Absolute banger of a DocString here....
    
#     All methods MUST start with "test_" in order for Python to recognize
#     the method as a test.
#     """
    
#     def test_add(self):
#         """
#         Tests the add function.
#         -assertEqual: checks if 2 values are equal
#         -assertAlmostEqual: checks if 2 values are equal up to 7 decimal points,
#         hence the "almost" equal part. This is useful when comparing floats
#         """
#         print("\nTesting the add function.")
#         self.assertEqual(CE1_classes.add(5,10), 15)
#         self.assertAlmostEqual(CE1_classes.add(5.2,1.3), 6.5)
#         self.assertEqual(CE1_classes.add(5.2,1.3), 6.5)
#         self.assertEqual(CE1_classes.add(-5,-20), -25)
#         self.assertEqual(CE1_classes.add(-5,20), 15)
#         self.assertEqual(CE1_classes.add(0,0), 0)


#     def test_subtract(self):
#         """
#         Tests the subtract function.
#         Make sure that the assert statements are checking not just an average case
#         but also edge cases, like negative values, negative and positive, 0 values
#         (could even check complex values but I'm keeping it real in this class)

#         ...my apologies for that joke. 
#         "i" can't help myself sometimes... Apologies again.
#         I can hear the eye rolls through the screen....
#         """
#         print("\nTesting the subtract function.")
#         self.assertEqual(CE1_classes.subtract(5,10), -5)
#         self.assertAlmostEqual(CE1_classes.subtract(5.2,1.3), 3.9)
#         # self.assertAlmostEqual(CE1_classes.subtract(5.2,1.3), 3.9) #does not work
#         self.assertEqual(CE1_classes.subtract(-5,-20), 15)


#     def test_multiply(self):
#         print("\nTesting the multiply function.")
#         self.assertEqual(CE1_classes.multiply(5,10), 50)


#     def test_divide(self):

#         print("\nTesting the divide function.")
#         self.assertAlmostEqual(CE1_classes.divide(9, 2), 4.5)
#         self.assertRaises(ZeroDivisionError, CE1_classes.divide, 10, 0)

#         #This uses a context manager checks that our code raises the ZeroDivisionError
#         #and we can call our functions as we usually do. (this is equivalent to line 72)
#         with self.assertRaises(ZeroDivisionError):
#             CE1_classes.divide(10, 0)



# # In order to run the unit tests in this file, you must make a call 
# # to unittest.main() method. Uncomment the next if statement to run the 
# # unittests above :

# if __name__ == "__main__":
#     unittest.main()





#January 28 - Week 4 - Day 7

#Homework 4 - will need multiple modules for the assignment and the testing
#How many unit tests are needed? 
    #Keeping guidelines fuzzy so that we have to figure it out alone.


from collections import defaultdict, namedtuple

#Default Dictionary Example
# defaultdict(
#     'Credit Card': {defaultdict
#         'data': [],
#         'stats_Period': []}

#     'Complaints': {defaultdict
#         'data': [],
#         'stats_Product': []
#     })

# #Named Tuples
# phone = namedtuple("Phone", ['cell', 'home'])
# p_test = phone('1234567890', '0987654321')
# print(p_test.cell)

# contact = namedtuple("Contact", ['phone', 'email', 'address'])
# c_test = contact(p_test, 'abc@gmail.com', '123 Street Rd')
# print(c_test)

# person = namedtuple('Person', ['first', 'last', 'contact', 'age'])
# person_test = person('Jessica', 'Armendariz', c_test, '33')
# print(person_test)

# print(person_test.last)
# print(person_test.first, person_test.last)
# print(person_test.contact.email, person_test.contact.address)
# print(person_test.last, person_test.contact.phone.home, person_test.contact.phone.cell)


# def userProfile():
#     pass





#January 30 - Week 4 - Day 8
#record_dict is an attribute in init, not a method
#create container returns the entry named tuple, first line of the file





#February 4 - Week 5 - Day 9


