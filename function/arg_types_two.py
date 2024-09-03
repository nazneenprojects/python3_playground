def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)  # Positional arguments: "Alice" for `name`, 25 for `age`


def greet(name, age=30):
    print(f"Hello {name}, you are {age} years old.")

greet("Bob")  # Uses default age of 30


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=22, name="Charlie")  # Order doesn't matter for keyword argument


def greet(name, age=None):
    if age:
        print(f"Hello {name}, you are {age} years old.")
    else:
        print(f"Hello {name}, age not specified.")

greet("Diana")  # `age` is optional


#Arbitrary Positional Arguments (using *args)
def greet(*names):
    for name in names:
        print(f"Hello {name}")

greet("Eve", "Frank", "Grace")  # Can pass any number of arguments


#Arbitrary Keyword Arguments (using **kwargs
def greet(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

greet(name="Hank", age=40, city="NYC")  # Can pass any number of keyword arguments
