#Step 2: Modify Tent, Tarp, Hammock classes
#Complete the optional question from homework 1. Make all the modifications necessary to the Tent, Tarp and Hammock classes to consolidate the shared code into the Shelter class.
#You will also need to modify the Shelter, Hammock, Tent and Tarp classes str method, so that Hammock, Tent and Tarp make calls to the Shelter str method which will print each instance using the following format :
#• Shelter(num_occupants, material, setup_time, sqft (if applicable), vestibule (if applicable), weight, structure_poles (if applicable), seasons)


class Tent:
  def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, \
              structure_poles=True, seasons=3) -> None:
    self.num_occupants = num_occupants
    self.material = material
    self.setup_time = setup_time
    self.sqft = sqft
    self.vestibule = vestibule
    self.weight = weight
    self.structure_poles = structure_poles
    self.seasons = seasons

  def __lt__(self, other):
    if type(self) == type(other):
      return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
    return NotImplemented

  def __str__(self) -> str:
     return self.__repr__()

  def __repr__(self) -> str:
     return f"Tent({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, \
            {self.vestibule}, {self.weight}, {self.structure_poles}, {self.seasons})"
  
  def is_better(self, other) -> bool:
        if type(self) == type(other):
          return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
            (self.seasons >= other.seasons)
        return NotImplemented

class Hammock:
  def __init__(self, num_occupants, material, setup_time, weight, length=11, seasons=3) -> None:
    self.num_occupants = num_occupants
    self.material = material
    self.setup_time = setup_time
    self.weight = weight
    self.length = length
    self.seasons = seasons

  def __lt__(self, other):
    if type(self) == type(other):
      return (self.weight < other.weight) and (self.setup_time < other.setup_time)
    
    return NotImplemented

  def __str__(self) -> str:
     return self.__repr__()

  def __repr__(self) -> str:
     return f"Hammock({self.num_occupants}, {self.material}, {self.setup_time}, \
            {self.weight}, {self.length}, {self.seasons})"
  
  def is_better(self, other) -> bool:
        if type(self) == type(other):
          return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
            (self.seasons >= other.seasons)
        return NotImplemented

class Tarp:
  def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3) -> None:
    self.num_occupants = num_occupants
    self.material = material
    self.setup_time = setup_time
    self.sqft = sqft
    self.weight = weight
    self.seasons = seasons

  def __lt__(self, other):
    if type(self) == type(other):
      return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
    return NotImplemented

  def __str__(self) -> str:
     return self.__repr__()

  def __repr__(self) -> str:
     return f"Tarp({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, \
            {self.weight}, {self.seasons})"
  
  def is_better(self, other) -> bool:
        if type(self) == type(other):
          return (self.weight < other.weight) and (self.setup_time < other.setup_time) and \
            (self.seasons >= other.seasons)
        return NotImplemented
