# greet.py
import sys

if len(sys.argv) != 2:
    print("Usage: python <name of current file>.py <name>")
    sys.exit(1)

name = sys.argv[1]

print(f"Hello, {name}!")



