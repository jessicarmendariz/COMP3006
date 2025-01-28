#Step 2: Modify Tent, Tarp, Hammock classes
#Complete the optional question from homework 1. Make all the modifications necessary to the Tent, Tarp and Hammock classes to consolidate the shared code into the Shelter class.
#You will also need to modify the Shelter, Hammock, Tent and Tarp classes str method, so that Hammock, Tent and Tarp make calls to the Shelter str method which will print each instance using the following format :
#• Shelter(num_occupants, material, setup_time, sqft (if applicable), vestibule (if applicable), weight, structure_poles (if applicable), seasons)


#Solution to Optional Question 6 for Homework 1

class Shelter:
    #Base Class Containing Common Attributes and Methods for all Shelter Classes
    def __init__(self, num_occupants, material, setup_time, weight, seasons=3):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.seasons = seasons

    #Less Than Comparison
    def __lt__(self, other):
        if isinstance(other, Shelter):
            return (self.num_occupants < other.num_occupants) and (self.weight < other.weight)
        return NotImplemented

    #Which Shelter is Better Comparison
    def is_better(self, other) -> bool:
        if isinstance(other, Shelter):
            return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
                   (self.seasons >= other.seasons)
        return NotImplemented

    #Returns a String of the Shelter Object 
    def __str__(self) -> str:
        return f"Shelter({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.seasons})"


class Tent(Shelter):
    #Tent Class Extends the Shelter Class
    #Inherits from Shelter

    #Initializes Tenbt Object
    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles=True, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft
        self.vestibule = vestibule
        self.structure_poles = structure_poles

    #Initializes Tent Attributes
    def __str__(self) -> str:
        return f"Shelter({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, {self.vestibule}, " \
               f"{self.weight}, {self.structure_poles}, {self.seasons})"


class Hammock(Shelter):
    def __init__(self, num_occupants, material, setup_time, weight, length=11, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.length = length

    def __str__(self) -> str:
        return f"Shelter({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.length}, {self.seasons})"


class Tarp(Shelter):
    #Tarp Class Extends the Shelter Class
    #Inherits from Shelter

    #Initializes Tarp Object
    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft

    #Initializes Tarp Attributes
    def __str__(self) -> str:
        return f"Shelter({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, {self.weight}, {self.seasons})"
