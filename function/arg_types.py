
# Python program to illustrate Default Arguments in Functions
# This function is used to welcome students to school
# A default value can be set for any number of arguments in a function. However, if we have a default argument, we must likewise have default values for all the arguments to their right. Non-default arguments, in other words, cannot be followed by default arguments.
def welcome(fullname, msg = 'Welcome to School!!'):

# If the msg argument value is not provided, then the default value in the Function argument is considered
    print('Hey there', fullname + ', ' + msg)

welcome('Sam')   # 2nd argument value not passed; will use function default argument
welcome('Zack', 'How have you been?')



# Keyword argument# However, we must remember that the keyword arguments must always come after the positional arguments. There will be issues if a positional argument is used after the keyword arguments.
def fruits(a, b, p):
    print('We have', a+ ',', b+ ' and', p+ ' at our store.')

fruits('apple', 'banana', 'pineapple')


# Keyword Arguments in order
fruits(a = 'apple', b = 'banana', p = 'pineapple')

# Keyword Arguments out of order
fruits(b = 'banana', p = 'pineapple', a = 'apple')

# 2 positional, 1 keyword argument
fruits('apple', b = 'banana', p = 'pineapple')


# Python *args allows a function to accept any number of positional arguments i.e. arguments which are non-keyword arguments, variable-length argument list.

# Program to add and display sum of n number of integer
def add(*num):
    sum = 0;
    for n in num:
        sum = sum + n;
    print("Sum:", sum)

add(3,4,5,6,7)
add(1,2,3,5,6,7,8)


"""
Notes :
As guidance:

Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.


Keyword arguments allow us to employ any order, whereas default arguments assist us to deal with the absence of values. And finally, in Python, arbitrary arguments come in handy when we don’t know how many arguments are needed in the program at that moment.


"""
