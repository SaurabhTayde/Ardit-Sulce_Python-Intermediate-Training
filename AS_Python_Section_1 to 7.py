# variable addition:

a = '10'
b = '20'
c = a+b
print(c)

# Float and int addition:
x = 10.0
y = 10
z = x+y
print(z) # Note that output is float

###############################################################################################
# Attributes in python (To check operations that could be performed with different data types)
###############################################################################################

print(dir(list))
print(50*'*')
print(dir(str)) 

# In above case there are atttributes that starts with double underscore and end with double underscore
# Those attributes python uses intrnally and as of now we don't need to use them

# Check one of the attribute of list:
list1 = [98,97,96,95,94,93]
print(list1.index(94))
print(50*'*')

# Check one of the attribute of string:
print('hello'.upper())
print(50*'*')

# Check all the functions available:
print(dir(__builtins__))
print(50*'*')

# Creating a function:
# Let's create a function in python that will give average of the values in list:

def mean(mylist):
    the_mean = sum(mylist)/len(mylist)
    return the_mean

print(mean([1,2,3,4]))
print(mean(list1))


######################
#### 'isinstance'
######################

# Suppose we want find mean of either list or dictionary (values in dictonary)

def mean(val):
    if type(val) == dict:
        the_mean = sum(val.values())/ len(val)
    else:
        the_mean = sum(val)/len(val)
    return the_mean

temp = [12,13,14,15]
age = {'sam': 10, 'ray': 15, 'dave': 20}

print(mean(temp))
print(mean(age))

# Now in above code we are using 'type(val) == dict' in the conditionals, 
# But it is highly recommended that we shuld use 'isinstance(val,dict)' in the conditionals wherever type of variable is involved
# i.e. Check if a value is of a particular type with 'isinstance' ('==' will also work but not recommended)
# So the code should be:


def mean(val):
    if isinstance(val,dict):
        the_mean = sum(val.values())/ len(val)
    else:
        the_mean = sum(val)/len(val)
    return the_mean

temp = [12,13,14,15]
age = {'sam': 10, 'ray': 15, 'dave': 20}

print(mean(temp))
print(mean(age))

######################
#### Input From User
######################

# Take a string input from user and print it's lower case:

user_input = input('Enter String fro which lower cases needs to be printed:')
print(user_input.lower())

# Now, by default code takes input in string format only unless specified
# For example, consider following code:

#def weather_condition(tempe):
#    if tempe > 7:
#        return 'warm'
#    else:
#        return 'cold'

#user_input = input('Enter Temperature:')
#print(weather_condition(user_input))

# But above code will give error (Uncomment above code to check the error), since system will consider input from user as string only (even if input entered is number)
# and in the program this input (as a string) will be comapared with number, so error will come
# So, we need to specify to the code that input we are taking from user is float
# Now following code will work:

def weather_condition(tempe):
    if tempe > 7:
        return 'warm'
    else:
        return 'cold'

user_input = float(input('Enter Temperature:'))
print(weather_condition(user_input))

# String formatting:
# How to take input from user and use that input to print something else:

user_input = input('Enter your name:')
message = f'Hello {user_input} !!'
print(message)

# In above code for python versions lower than V3.6, we need to use following code:
# message = 'Hello %s' % user_input

# Now to input multiple variables, we can write following code:

name = input('Enter your name:')
surname = input('Enter your surname:')
message = f'Hello {name} {surname}!!'
print(message)

# In above code for python versions lower than V3.6, we need to use following code:
# message = 'Hello %s' % (name, surname)

#########################################
## Cheatsheet (Processing User Input)
#########################################

# In this section, we learned that:
# A Python program can get user input via the input function:
# The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")

# The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
print("Hi %s, you have %s years of experience." % (name, experience_years))

# You can format strings with (works both on Python 2 and 3):

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
# Output: Hi Sim, you have 1.5 years of experience.

# You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
# Output: Hi Sim, you have 1.5 years of experience.


#######################################
# Dictionary Loop and String Formatting
#######################################

# You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


###########################################
### Taking user input and using while loop
###########################################

username = ''

while username != 'saurabh':
    username = input('Enter username:')


# Or above code can also be written as:

while True:
    username = input('Enter Username')
    if username == 'saurabh':
        break
    else:
        continue
    
