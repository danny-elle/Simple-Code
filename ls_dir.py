import sys
import os
import subprocess

# Get arbitrary number of arguments on command line
for arg in sys.argv[1:]:
    # Checks if the argument on command line is a directory
    if os.path.isdir(arg):
        print("directory is: ", arg)
        # Error Checking if argument is a directory, throws exception if error occurs
        try:
            output = subprocess.check_output(['ls', arg])
            print(output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    # If argument is not a directory message is printed
    else:
        print(arg, "is not a directory.")
