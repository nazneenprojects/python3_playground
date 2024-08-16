# Step 1: Define a User-Defined Exception
class MyCustomError(Exception):
    """Custom exception class for specific error handling."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Step 2: Function that uses the custom exception
def check_value(value):
    if value < 0:
        raise MyCustomError("Negative value provided: {}".format(value))
    else:
        return "Value is acceptable: {}".format(value)

# Step 3: Use the function and handle the exception
try:
    result = check_value(-10)  # This will raise MyCustomError
    print(result)
except MyCustomError as e:
    print("Caught a custom exception:", e)
