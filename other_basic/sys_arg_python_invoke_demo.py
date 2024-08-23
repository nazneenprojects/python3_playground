# greet.py
import sys

if len(sys.argv) != 2:
    print("Usage: python <name of current file>.py <name>")
    sys.exit(1)

name = sys.argv[1]
temp = sys.argv[0]

print(f"Hello, {name}!,  {temp}")


"""
    Run this program by using -
    python sys_arg_python_invoke_demo.py Flounder
"""



