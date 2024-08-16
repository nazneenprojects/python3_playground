"""
In Python, class definitions must be executed before they are usable.
During this execution, a new namespace is created specifically for the class, which acts as the local scope for all assignments and method definitions within the class.
This namespace holds the class's methods and other attributes, effectively capturing the state and behavior defined within the class block.

Once the class definition is completed, a class object is created from this namespace.
This class object acts as a wrapper for the namespace contents and is bound to the class name specified in the definition.
The original scope from before the class definition is restored, and the new class object becomes available
for creating instances and accessing its methods and attributes in the re-established scope.
"""


class DemoClassOne:
    """
    A Simple class to demo attribute references and instantiation
    """

    def __init__(self):
        self.data = []

    i = 12345  # class variable

    def f(self):
        return 'hello world'


if __name__ == "__main__":
    # Attribute reference
    print(".........Attribute reference................")
    print(DemoClassOne.i)
    #method object, not a function object.
    print(DemoClassOne.f)
    print(DemoClassOne.f("hey"))

    # class instantiation
    print("............class instantiation.......")
    x = DemoClassOne()
    print(x)
    print(x.i)
    y = x.f()
    print(y)





