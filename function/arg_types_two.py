def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)  # Positional arguments: "Alice" for `name`, 25 for `age`


def greet(name, age=30):
    print(f"Hello {name}, you are {age} years old.")

greet("Bob")  # Uses default age of 30


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=22, name="Charlie")  # Order doesn't matter for keyword argument


def greet(name, age=None):
    if age:
        print(f"Hello {name}, you are {age} years old.")
    else:
        print(f"Hello {name}, age not specified.")

greet("Diana")  # `age` is optional


#Arbitrary Positional Arguments (using *args)
def greet(*names):
    for name in names:
        print(f"Hello {name}")

greet("Eve", "Frank", "Grace")  # Can pass any number of arguments


#Arbitrary Keyword Arguments (using **kwargs
def greet(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

greet(name="Hank", age=40, city="NYC")  # Can pass any number of keyword arguments


# Function with default, required, and optional arguments
def book_order(title, author, copies=1, discount=None):
    """
    Arguments:
    - title (required): The title of the book
    - author (required): The author of the book
    - copies (default=1): The number of copies to order (default value is 1)
    - discount (optional): Discount on the total price (optional)
    """
    
    price_per_copy = 20  # Example price per book copy
    total_price = price_per_copy * copies
    
    # Apply discount if provided (optional argument)
    if discount:
        total_price = total_price - (total_price * (discount / 100))
    
    print(f"Order Details:\nBook: {title}\nAuthor: {author}\nCopies: {copies}\nTotal Price: ${total_price:.2f}\n")

# Required arguments only (title and author)
book_order("1984", "George Orwell")

# Required + default argument (copies)
book_order("Brave New World", "Aldous Huxley", 3)

# Required + default + optional argument (discount)
book_order("Fahrenheit 451", "Ray Bradbury", 5, 10)

