class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

if __name__ == "__main__":
    instance = Bag()
    instance.add(123)
    instance.addtwice(456)

    print(instance.data)
    print(instance.__class__)   #  an object, and therefore has a class (also called its type). It is stored as object.__class__.


""" 
Notes:
Global Scope for Methods:
Methods can access global names in the same way as ordinary functions.
The global scope associated with a method is the module in which the class is defined. The class itself does not provide a global scope.


Global Data and Methods:
While it's not common to use global data directly in methods, there are valid reasons to do so.
For instance, methods can use functions and modules imported into the global scope of the module.


Class Reference:
Although methods can access global names, classes are typically defined in the same global scope. 
Methods can reference their own class if needed, which will be discussed further in the next section.
"""