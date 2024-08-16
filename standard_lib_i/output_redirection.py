import sys

# Write error message to standard error
# sys.stderr.write("Warning! Thunderstorm warning in your software apps due to Python dependency version change\n")
# sys.stderr.flush()  # Ensure the error message is written immediately

# Write standard output message
sys.stdout.write("This is a standard output message\n")
sys.stdout.flush()  # Ensure the message is written immediately

def main():
    # Prompt the user for input
    sys.stdout.write("Enter your name: ")
    sys.stdout.flush()  # Ensure the prompt is written immediately

    # Read user input from standard input
    name = sys.stdin.readline().strip()  # .strip() to remove any trailing newline characters

    # Print a greeting message to standard output
    sys.stdout.write(f"Hello, {name}!\n")
    sys.stdout.flush()  # Ensure the message is written immediately

    # Print a message to standard error
    sys.stderr.write("End of the program, Goodbye!\n")
    sys.stderr.flush()  # Ensure the message is written immediately

if __name__ == "__main__":
    main()
