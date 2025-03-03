import os
import re

#Traverses Every Folder in the Directory
def retrieve_files(extension=".txt"):
    #Args: Extension
    #Returns: A List of File Paths Matching the Extension
    file_list = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assignment_dir = os.path.join(base_dir, "..") 

    for root, _, files in os.walk(assignment_dir):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    
    return file_list

#Takes a List Containing File Paths and Names
def record_loader_gen(file_list):
    #Args: file_list of File Paths to Process
    #Yields: tuple of Name, Gender, Births, Year
    for file in file_list:
        match = re.search(r"yob(\d{4})\.txt", file)
        if match:
            year = int(match.group(1))
            with open(file, "r") as f:
                for line in f:
                    name, gender, births = line.strip().split(",")
                    yield name, gender, int(births), year