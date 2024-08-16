class Parent:
    def __init__(self):
        self.data =[]


class Child(Parent):
    def __init__(self):
        super().__init__()  # Ensure to call the parent class's __init__ method
        self.info = []


if __name__ == "__main__":
    # Check if Child is a subclass of Parent
    print(issubclass(Child, Parent))  # Should print: True

    # Create an instance of Parent
    instance = Parent()

    # Check if instance is an instance of Parent
    print(isinstance(instance, Parent))  # Should print: True

    # Check if instance is an instance of Child
    print(isinstance(instance, Child))  # Should print: False