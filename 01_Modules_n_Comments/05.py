# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  

import os

# Specify the directory path you want to list
directory_path = "/"

try:
    # Use os.listdir() to get a list of entries in the directory
    entries = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for entry in entries:
        print(entry)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
