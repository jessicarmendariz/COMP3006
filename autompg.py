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
