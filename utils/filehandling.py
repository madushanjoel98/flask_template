import os

def create_netslocation(location_string):
    # Create nested directories
    try:
        if location_string ==None :
            raise Exception("location is empty")
               
        os.makedirs(location_string)
        print(f"Nested directories '{location_string}' created successfully.")
    except FileExistsError:
        print(f"One or more directories in '{location_string}' already exist.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{location_string}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
