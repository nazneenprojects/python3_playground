"""
NOTES:
Method Resolution Order (MRO): Python uses the C3 linearization algorithm to determine the order in which base classes are
initialized and methods are resolved. This ensures a consistent and predictable method resolution order, even in complex inheritance hierarchies.

super() Function: The super() function is used to call methods from the parent class, ensuring that each class in
the inheritance chain is properly initialized. In multilevel inheritance, it’s crucial to call super().__init__() in each subclass's constructor
to ensure proper initialization from top to bottom.

Attribute and Method Access: An instance of the most derived class (in this case, Child) can access attributes and methods
from all levels in the inheritance hierarchy, demonstrating the power of multilevel inheritance.
"""

class Grandparent:
    def __init__(self):
        self.grandparent_attr = "Grandparent attribute"

    def grandparent_method(self):
        return "Method of Grandparent"


class Parent(Grandparent):
    def __init__(self):
        super().__init__()  # Call Grandparent's __init__ method
        self.parent_attr = "Parent attribute"

    def parent_method(self):
        return "Method of Parent"


class Child(Parent):
    def __init__(self):
        super().__init__()  # Call Parent's __init__ method
        self.child_attr = "Child attribute"

    def child_method(self):
        return "Method of Child"


if __name__ == "__main__":
    # Create an instance of Child
    child_instance = Child()

    # Access attributes and methods from all levels
    print(child_instance.grandparent_attr)  # Output: Grandparent attribute
    print(child_instance.parent_attr)  # Output: Parent attribute
    print(child_instance.child_attr)  # Output: Child attribute

    print(child_instance.grandparent_method())  # Output: Method of Grandparent
    print(child_instance.parent_method())  # Output: Method of Parent
    print(child_instance.child_method())  # Output: Method of Child
