# Without walrus operator
numbers = [10, 20, 30, 40]
count = len(numbers)
if count > 3:
    print(f"List is too long (length: {count})")

# With walrus operator
numbers = [10, 20, 30, 40]
if (count := len(numbers)) > 3:
    print(f"List is too long (length: {count})")

# Without walrus operator
while True:
    data = input("Enter something: ")
    if not data:
        break
    print("You entered:", data)

    # With walrus operator
while data := input("Enter something: "):
    print("You entered:", data)
