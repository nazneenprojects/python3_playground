class MyClass:
    def __init__(self, value):
        self.__private_variable = value                             # Private variable

    def get_private_variable(self):
        return self.__private_variable                              # Accessor method to get the value of the private variable

    def set_private_variable(self, value):
        self.__private_variable = value                             # Mutator method to set the value of the private variable

# Creating an instance of MyClass
obj = MyClass(10)

# Accessing the private variable using a public method
print(obj.get_private_variable())                                   # Output: 10

# Modifying the private variable using a public method
obj.set_private_variable(20)
print(obj.get_private_variable())                                   # Output: 20

# Trying to access the private variable directly (Not recommended)
# print(obj.__private_variable)  # This will raise an AttributeError

# Accessing the private variable directly using name mangling (Not recommended)
print(obj._MyClass__private_variable)                               # Output: 20
