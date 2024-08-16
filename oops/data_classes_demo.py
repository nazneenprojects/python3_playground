"""
Python's dataclasses module, introduced in Python 3.7, provides a decorator and functions for automatically adding special methods to classes,
like __init__, __repr__, and __eq__,
without having to write them explicitly. It's a convenient way to create classes that are primarily used to store data.
"""
from dataclasses import dataclass

@dataclass
class Employee:
    name : str
    dept : str
    salary : int

# creating a instance of the Employee dataclass
emp = Employee(name='bob', dept='sales', salary=120000)

# Accessing fields
print("Name", emp.name)
print("Dept",emp.dept)
print("Salary", emp.salary)

# The __repr__ method automatically added
print(emp)

# The __eq__ method is also automatically added
emp_on_contract = Employee(name="alice", dept='IT', salary=150000)
print(emp == emp_on_contract)
