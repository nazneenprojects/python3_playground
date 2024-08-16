class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, city='{self.city}')"

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name and
                    self.age == other.age and
                    self.city == other.city)
        return False

# Creating instances of the Person class
person1 = Person(name="Alice", age=30, city="New York")
person2 = Person(name="Alice", age=30, city="New York")
person3 = Person(name="Bob", age=25, city="Los Angeles")

# Accessing attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
print(person1.city)  # Output: New York

# Using __repr__ method
print(person1)  # Output: Person(name='Alice', age=30, city='New York')

# Comparing instances using __eq__ method
print(person1 == person2)  # Output: True
print(person1 == person3)  # Output: False
