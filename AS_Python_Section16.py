# There are 2 types of errors.
# 1. Syntax error
# 2. Exceptions

# Syntax error:
# following code will give syntax error:
# list1 = [1,2,3,4)
# We can fix this error by completing the list by square bracket

# Exceptions:
# Every error in the code that is not syntax error is an exception

# following code will give type error:

#a = 1
#b = '2'
#print(a+b)


# Now let's check following code:

#a = 1
#b = '2'
#print(a+b)
#print(a))

# Now in above code we can see that both lines 17 and 18 have errors
# line 17 has 'type error' and line 18 has syntax error
# So, we might think that line 17's error should be thrown by the python if we run above code since it's appear beforehand
# But this won't happen, it will throw syntax error first (line 18's error)
# Because python initially checks whether there's any syntax error in the code and then it does double check for other errors (i.e. exceptions)

# following code will give name error:

#a = 1
#b = '2'
#print(c)

# following code will give zero division error:

#d=6
#print(d/0)

# Making the code to handle error itself:

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Zero division is meaningless'

print(divide(1,2))
print('End of program')

# In above code, we can either skip 'ZeroDivisionError' or keeo it
# It's always better to keep the error name over there so that it will handle/accept only given specific error
# And it will not accept any unknown eror
