import os
import re

# Get the file name from the user
file_name = input("Enter a file name: ")

# Check if the file exists
if not os.path.exists(file_name):
    print("The file does not exist.")
else:
    # Read the file data and print it
    with open(file_name, 'r') as file:
        file_data = file.read()
        print(file_data)

    # Get the number of characters in the file
    num_chars = len(file_data)
    print(f"\nNumber of characters in the file: {num_chars}")

    # Get the number of function definitions in the file
    num_functions = len(re.findall(r'def\s+\w+\(', file_data))
    print(f"Number of function definitions in the file: {num_functions}")

    # Get the number of equal signs in the file
    num_equals = len(re.findall(r'=', file_data))
    print(f"Number of equal signs in the file: {num_equals}")