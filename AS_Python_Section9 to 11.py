######################################
# 'IfElse' loop in list comprehensions
######################################


# Order matters in list comprehensions if there's 'IfElse' loop is involved.
# 'for' loop always comes after 'IfElse' loop in list comprehensions
# But 'for' loop can come before when there's just 'if' condition is involved. So, 'for' loop can come before 'if' condition (not before 'IfElse' loop)
# For ex:

list1 = [12,13,14,-15,17]

# Now if we want positive numbers, and if any negative number appears it should be replace with 0, then:

list2 = [i if i>0 else 0 for i in list1]
print(list2)
print('*'*50)


# Following code for above logic will not work since we are using for loop before ifElse loop:

#list3 = [i for i in list1 if i>0 else 0]
#print(list3)

###########################
## Reading file in python:
###########################

myfile = open('fruits.txt')
print(myfile.read())
print('*'*50)

# Because of 'file cursor' concept(refer vdo for details), sometimes a variable is created
myfile = open('fruits.txt')
content = myfile.read()
print(content)
print('*'*50)


## Closing file:
myfile = open('fruits.txt')
content = myfile.read()
myfile.close()
print(content)
print('*'*50)

# Now since we have closed the file we will get error if we try to read the file again:
# myfile.read()

## Instead if using above code we can also use 'with' operator so that we will not have to close the file:
with open('fruits.txt') as myfile:
    content = myfile.read()

print(content)
print('*'*50)
## If we put txt file in the folder named #files where .py file is located then we will have to give path as follows:

#with open('files/fruits.txt') as myfile:
#    content = myfile.read()

#print(content)

##################################
## If we want to create a txt file:


with open('files/vegetables.txt', 'w') as myfile2:
    myfile2.write('Tomato\nCucumber\nOnion')
    myfile2.write('\nGarlic')


# If we want to add something in existing txt file:

with open('files/vegetables.txt', 'a') as myfile2:
    myfile2.write('\nOkra')
    # 'a' stands for append in above code
#   content2 = myfile2.read()

#print(content2)

# Now above code will add new text but it's not readable or writable.
# so we need to use 'a+' instead of 'a'

with open('files/vegetables.txt', 'a+') as myfile2:
    myfile2.write('\nOkra')
    myfile2.seek(0)
    content2 = myfile2.read()

print(content2)

###############
## Cheatsheet
###############

#You can read an existing file with Python:
#with open("file.txt") as file:
#    content = file.read()

#You can create a new file with Python and write some text on it:
#with open("file.txt", "w") as file:
#    content = file.write("Sample text")

#You can append text to an existing file without overwriting it:
#with open("file.txt", "a") as file:
#    content = file.write("More sample text")

#You can both append and read a file with:
#with open("file.txt", "a+") as file:
#    content = file.write("Even more sample text")
#    file.seek(0)
#    content = file.read()