# Methods can be searched as follows:
print(dir(str))
print('*'*100)

# Functions can be searched as follows:
print(dir(__builtins__))
print('*'*100)

# Builtin modules can be searched as follows:
import sys
print(sys.builtin_module_names)
print('*'*100)

# If we want to use any module then we need to import it
# For example:
import time

    # We can see different method in time module as follows:
print(dir(time))
print('*'*100)

# Now 'time' module has 'sleep' method in it
# We can use it as follows to take 3 seconds of break while executing the script:

# time.sleep(5)

# Now we can see, it took 5 seconds to run our above script
# This is how we use a module

# Now, not everything is built in our python interpreter software
# Many things that come in different format
                                
# If we want to check where the imported modules are present in the system, then
# type 'sys.prefix' in python terminal and whatever result(path) will come,
# after that path go to lib then python3.8, you will find all imported modules there

# Now we directly imported required modules here and they worked
# Not all the modules are already present, so we need to install packages first
# and then we need to import module

# pip3.8 install pandas
# Now to check where this library is located use sys.prefix command in python3.8 terminal
# Then go to that path check 'site packages' folder  then we will able to find folder of that articular library

# Bunch of modules is called packages

##################################
### Cheatsheet (Imported Modules)
##################################

#In this section, you learned that:

#Builtin objects are all objects that are written inside the Python interpreter in C language.

#Builtin modules contain builtins objects.

#Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

#import time
#time.sleep(5)

#A list of all builtin modules can be printed out with:

#import sys
#sys.builtin_module_names

#Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

#Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

#Packages are a collection of .py modules.

#Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

#Third-party libraries can be installed from the terminal/command line:

#Windows:

#pip install pandas or use python -m pip install pandas if that doesn't work.

#Mac and Linux:

#pip3 install pandas or use python3 -m pip install pandas if that doesn't work.
