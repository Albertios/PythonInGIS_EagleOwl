import os

def my_open_function(path):
    # Check if it exists
    if os.path.exists(path):
        # If yes, open and put content in variable
        with open(path) as f:
            data = f.read()
    else:
        # If no, put None in the same variable
        data = None
    return data

# Working directory
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', 'data')
# Path to the file
in_path = os.path.join(data_dir, 'JammertalHalternerStausee.gpx')

# Execute function
# Test with correct path
print(my_open_function(in_path))
# And with incorrect path
print(my_open_function('nonsense'))