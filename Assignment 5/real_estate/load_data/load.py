import csv
import os
from collections import defaultdict, namedtuple

#Absolute Import
from real_estate.helper_functions import context_manager

#Relative Import
from ..helper_functions import calculate_stats

#This Class Contains the Entire Real Estate Data Set and the properties_dict.
class RealEstate:
    #This Class Implements the __init__ Constructor that Takes A file_name And A Location As Arguments
    #This Creates a properties_dict Attribute and Calls The load_data Method
    #This CLass Has 4 Methods, __init__ load_data, -create_container, and compute_stats

    def __init__(self, file_name=None, location=None):
        #Constructor That Takes file_name and location As Arguments 
        #Creates a properties_dict Attribute and Calls load_data method
        #Creates a defaultdict With A Nested defaultdictThat Creates a List 
        #US States and Territories Are The Outer Keys and The Other States and Territories Will Be The Inner Keys 
        self.properties_dict = defaultdict(lambda: defaultdict(list), {
            'Territories': defaultdict(list, {
                'Puerto Rico': [],
                'Virgin Islands': []
            }),
            'US States': defaultdict(list, {
                'Massachusetts': [],
                'Connecticut': [],
                'New Hampshire': [],
                'Vermont': [],
                'New Jersey': [],
                'New York': [],
                'South Carolina': [],
                'Tennessee': [],
                'Rhode Island': [],
                'Virginia': [],
                'Wyoming': [],
                'Maine': [],
                'Georgia': [],
                'Pennsylvania': [],
                'West Virginia': [],
                'Delaware': [],
                'Louisiana': [],
            }),
        })

        self.file_name = file_name
        self.location = location

        if self.file_name and self.location:
            self.load_data(self.file_name, self.location)

    def load_data(self, file_name, location):
        #Takes file_name And location As Arguments And Loads The Data From The File Through contextmanager
        #Calls _create_container
        #Uses namedtuple Container Created To Create a Property namedtuple For Each Line 
        #Adds the Property Container To properties_dict
        while True:
            try:
                with context_manager.data_context_manager(file_name, 'r', location) as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    Property = self._create_container(headers)

                    for row in reader:
                        if len(row) != len(headers):
                            continue

                        prop = Property(*row)
                        state = prop.state
                        category = 'US States' if state in self.properties_dict['US States'] else 'Territories'
                        self.properties_dict[category][state].append(prop)
                break
            except FileNotFoundError:
                file_name = input("File not found. Enter a valid file name or 'q' to quit: ")
                if file_name.lower() == 'q':
                    break

    def _create_container(self, headers):
        #Takes the First Line of the File, Column Names, As An Argument
        #Unpacks Column Names To Create A namedtuple Called Property That Has Attributes As Column Names 
        #Returns the Property namedtuple.
        return namedtuple("Property", headers)

    def compute_stats(self, func_name, *args, **kwargs):
        #Takes a Function Name And A Variable Number of Arguments, And Keyword Arguments
        #Returns the Value of the Function Called
        if hasattr(calculate_stats, func_name):
            return getattr(calculate_stats, func_name)(self.properties_dict, *args, **kwargs)
        return None
