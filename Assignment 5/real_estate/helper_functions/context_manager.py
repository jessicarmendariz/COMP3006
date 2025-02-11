import os
from contextlib import contextmanager

@contextmanager
def data_context_manager(file_name, mode, destination):
    #Arguments: File Name, Mode, and Destination 
    #Changes the Current Working Directory to the Folder with the Data and Changes Current Working Directory Back When Done

    original_dir = os.getcwd()
    try:
        os.chdir(destination)
        print("Loading Data...")
        with open(file_name, mode, encoding="utf-8") as file:
            yield file
        print("Data Loaded:")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' NOT FOUND In {destination}.")
        raise
    finally:
        os.chdir(original_dir)
