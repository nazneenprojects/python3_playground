class DemoClassTwo:
    """
    A Simple class to demo attribute references and instantiation
    """

    """to create objects with instances customized to a specific initial state."""
    def __init__(self, author_name, email):
        self.author = author_name
        self.email = email

    def demofunc(self):
        return "hey , you are inside demofunc"


# instantiation of class
x = DemoClassTwo("Nazneen Mulani", 'naz18mulani@gmail.com')
#Error due to missing params
#y = DemoClassTwo()

print(x)

# Attribute reference
#attribute names:  1) data attributes (instance variables) and  2) methods.
print(x.author, x.email)

print("Docstring : ", x.__doc__)

#method object
print(x.demofunc)

#method function
print(x.demofunc())


"""
Notes :
When you call a method on an object in Python (e.g., x.f()), the method implicitly receives the instance (x) as its first argument. 
This is why x.f() works even if f expects one argument—Python automatically passes x as that argument.

You can also store a method (e.g., xf = x.f) and call it later. 
The method object xf keeps a reference to the instance x and the function f, so when you call xf(), it behaves the same as x.f().

This means x.f() is equivalent to ClassName.f(x)

Essentially, methods in Python are special because they combine the instance and the function into a single callable object, 
ensuring that the instance is always passed as the first argument when the method is called.

Conclusion Points:
Class definitions must be executed to create a usable class object.
Methods automatically receive the instance as the first argument.
Method objects can be stored and called later, preserving the instance context.
"""
