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


class Nigeria:
    def __init__(self):
        self.country_speciality = ["Nigerian cuisine"]


class SouthAfrica:
    def __init__(self):
        self.country_animals = ["Lion", "Elephant"]


class Uganda:
    def __init__(self):
        self.country_birds = ["African Fish Eagle", "Shoebill"]


class Madagascar:
    def __init__(self):
        self.country_water_animals = ["Aye-aye", "Madagascar Poison Frog"]


class AfricaContinent(Nigeria, SouthAfrica, Uganda, Madagascar):
    def __init__(self):
       # super().__init__()  # Call the parent class __init__ methods  but this did not work for calling multple parents attributes using single super()
        Nigeria.__init__(self)  # Initialize Nigeria's __init__
        Uganda.__init__(self)  # Initialize Uganda's __init__
        Madagascar.__init__(self)  # Initialize Madagascar's __init__
        SouthAfrica.__init__(self)  # Initialize South Africa's __init__
        self.info = []


if __name__ == "__main__":
    continent_instance = AfricaContinent()

    # Access attributes from multiple inherited classes
    print("Speciality from Nigeria:", continent_instance.country_speciality)
    print("Animals from South Africa:", continent_instance.country_animals)
    print("Birds from Uganda:", continent_instance.country_birds)
    print("Water animals from Madagascar:", continent_instance.country_water_animals)
    print("Additional info:", continent_instance.info)

    print("inspect the MRO, This will show you the order in which Python resolves the methods and attributes from the "
          "parent classes: \n", AfricaContinent.__mro__)
