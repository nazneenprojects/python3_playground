"""
This Script demonstrates simple data structures of Python
"""

# --------------------------List:A list is an ordered collection of elements that can be modified (mutable).
fruites = ["grannetapple", "banana", "mango"]
fruites.append("kiwi")
fruites.remove("mango")
print(fruites)

#---------------------------Tuple : A tuple is an ordered collection of elements that cannot be modified (immutable).
coordinates = (100, 20)
print(coordinates)

# coordinates[0] = 99  this is not allowed as tuples are immutableS
print(coordinates)

x, y = coordinates
print(x, y)

# ------------------------------Set : A set is an unordered collection of unique elements.
numbers = {1, 2, 4, 7, 0}
numbers.add(9)
numbers.remove(4)
print(numbers)

# ------------------------------ dictionary : A dictionary is a collection of key-value pairs.
# Creating a dictionary
student = {
    "name": "John",
    "age": 22,
    "major": "Computer Science"
}

# Accessing a value
print(student["name"])  # Output: John

# Adding a key-value pair
student["grade"] = "A"

# Modifying a value
student["age"] = 23

# Removing a key-value pair
del student["major"]

print(student)  # Output: {'name': 'John', 'age': 23, 'grade': 'A'}



# ---------------------------------------------------String : A string is a sequence of characters.
# Creating a string
greeting = "Hello, World!"

# Accessing characters
print(greeting[0])  # Output: H

# Slicing a string
print(greeting[7:12])  # Output: World

# String concatenation
new_greeting = greeting + " How are you?"

# String methods
print(greeting.lower())  # Output: hello, world!

print(new_greeting)  # Output: Hello, World! How are you?




# -------------------------------------------------------Queue : A queue is a collection where elements are added at the end and removed from the front (FIFO: First In, First Out).
from collections import deque

# Creating a queue
queue = deque(["a", "b", "c"])

# Adding elements
queue.append("d")

# Removing elements
first = queue.popleft()

print(queue)  # Output: deque(['b', 'c', 'd'])
print(first)  # Output: a


# ---------------------------------------------------------Stack : A stack is a collection where elements are added and removed from the end (LIFO: Last In, First Out).
# Creating a stack
stack = []

# Adding elements
stack.append("x")
stack.append("y")
stack.append("z")

# Removing elements
last = stack.pop()

print(stack)  # Output: ['x', 'y']
print(last)  # Output: z

# -----------------------------------------------Array : An array is a collection of elements of the same type (in Python, you can use the array module for this).
import array as arr

# Creating an array of integers
numbers = arr.array('i', [1, 2, 3, 4])

# Adding an element
numbers.append(5)

# Accessing elements
print(numbers[0])  # Output: 1

# Modifying an element
numbers[1] = 10

# Removing an element
numbers.remove(3)

print(numbers)  # Output: array('i', [1, 10, 4, 5])


# Creating a 2D array (3x3) using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element
print("Element at row 1, column 2:", matrix[0][1])  # Output: 2

# Modifying an element
matrix[1][2] = 10
print("Modified matrix:", matrix)

# Iterating over the 2D array
print("Matrix elements:")
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
