year = 2026
event = "birtday"

print(f'Results of the year {year} {event}')

sp = 100
cp = 200
loss = cp - sp
percentage_of_loss = (loss / cp) * 100
print(' SP {} and CP {} and Loss % is {:2.2%} '.format(sp, cp, percentage_of_loss))
print(' SP {} and CP {} and Loss % is {} '.format(sp, cp, percentage_of_loss))

quote = "collective consciousness would not help the world , if you do not participate in the common healing"
# human readable
print(str(quote))
# can be read by the interpreter
print(repr(quote))

print(str(1 / 7))

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# formatting string literals
import math

print(f'The value of pi is approximately {math.pi:.3f}.')

greatMens = {'aristocrat': 1, 'Karl Marx': 2, 'Plato': 3}
for name, index in greatMens.items():
    print(f'{name:10} ==> {index:10d}')

animal = 'kangaroo'
print(f'Animals in the zoo are  {animal}')
print(f'Animals in the zoo are  {animal!r}')
print(f'Animals in the zoo are  {animal!s}')

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

print('Happiness is byproduct of {}'.format('our desires'))

print('{1} and {0}'.format('spam', 'eggs'))
print('{tom} and {jerry}'.format(tom='TOM', jerry='JERRY'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# The vars() function in Python returns the __dict__ attribute of an object, which is a dictionary representing the object’s namespace. This dictionary contains all the attributes (both methods and variables) of the object and their corresponding values.
#
# Usage
# Without Arguments: When called without arguments, vars() acts like locals() and returns the dictionary of the local symbol table.
# With Arguments: When called with an object, it returns the __dict__ attribute of the object if the object has one.
#
def example_vars_function():
    x = 10
    y = 20
    print(vars())


example_vars_function()


class ExampleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create an instance of ExampleClass
example_instance = ExampleClass(1, 2)

# Use vars() to get the __dict__ attribute of the instance
print(vars(example_instance))


class ExampleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create an instance of ExampleClass
example_instance = ExampleClass(1, 2)

# Modify the instance variables using vars()
vars(example_instance)['a'] = 10
vars(example_instance)['b'] = 20

# Check the updated values
print(example_instance.a)  # Output: 10
print(example_instance.b)  # Output: 20

for x in range(1, 25):
    print('{0:2d} {1:3d} {2:5d}'.format(x, x * x, x * x * x))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x * x * x).rjust(4))

'-3.14'.zfill(7)
'-003.14'

# old string formatting

import math

print('The value of Pi is approx %10.5f.' % math.pi)

# file IO
f = open('/input_output/workfile1', 'w', encoding='utf-8')
f.write("""Success is getting what you want..
Happiness is wanting what you get.""")

f.close()

with open('/input_output/workfile', encoding='utf-8') as myfile:
    # read_data = myfile.read()
    read_data = myfile.readline()
    print("workfile  content ->> \n", read_data)

if (myfile.closed):
    print("file is closed!")
    #myfile.read()

secretfile = open('/input_output/secret', 'w', encoding='utf-8')
secretfile.write("""Actions speak louder than words, and a smile says, ‘I like you. You make me happy. I am glad to see you.’ That is why dogs make such a hit. They are so glad to see us that they almost jump out of their skins. So, naturally, we are glad to see them.”
― Dale Carnegie, """)

# Open the file in read mode and read its contents
with open('secret', 'r', encoding='utf-8') as secretfile:
    for line in secretfile:
        print(line, end='')
    print("\nfile.list() ...")
    # Reset the file pointer to the beginning of the file
    secretfile.seek(0)
    print(list(secretfile))

    secretfile.readlines()

# Tuple to String
print("\n objects need to be converted from tuple to sTring  :")
value = ('the answer', 42)
s = str(value)
#print(s)
with open('/input_output/secret', 'w', encoding='utf-8') as secretfile:
    secretfile.write(s)

with open('/input_output/secret', 'r', encoding='utf-8') as secretfile:
    data = secretfile.readlines()
    #print(data)
    #returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
    print(secretfile.tell())

#change the byte in the file
f = open('/input_output/workfile', 'rb+')
f.write(b'0123456789abcdef')
# Seek to the 5th byte from the beginning
print(f.seek(5))  # Output: 5
# Read 5 bytes from the current position
print(f.read(5))  # Output: b'56789'

# Seek to the 3rd byte from the end
#f.seek(-3, 2): Moves the file pointer to the 3rd byte from the end of the file. The position will be 13 (since the total length is 16, 16-3 = 13).
print(f.seek(-3, 2))  # Output: 13
# Read 1 byte from the current position
print(f.read(1))  # Output: b'd'

#isatty():
import sys

# Check if standard output (stdout) is a terminal
if sys.stdout.isatty():
    print("Standard output (stdout) is a terminal.")
else:
    print("Standard output (stdout) is not a terminal.")

# Check if standard input (stdin) is a terminal
if sys.stdin.isatty():
    print("Standard input (stdin) is a terminal.")
else:
    print("Standard input (stdin) is not a terminal.")

# Check if standard error (stderr) is a terminal
if sys.stderr.isatty():
    print("Standard error (stderr) is a terminal.")
else:
    print("Standard error (stderr) is not a terminal.")

#Truncate()
# Create and write to the file
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('This is a test file with some initial content.')

# Read and print the initial content of the file
with open('/input_output/example.txt', 'r', encoding='utf-8') as f:
    print("Initial content:")
    print(f.read())

# Truncate the file to 10 bytes
with open('/input_output/example.txt', 'r+') as f:
    f.truncate(10)

# Read and print the content after truncation
with open('/input_output/example.txt', 'r', encoding='utf-8') as f:
    print("\nContent after truncation to 10 bytes:")
    print(f.read())

# Truncate the file to a larger size (25 bytes)
with open('/input_output/example.txt', 'r+') as f:
    f.truncate(25)

# Read and print the content after extending
with open('/input_output/example.txt', 'r', encoding='utf-8') as f:
    print("\nContent after extending to 25 bytes:")
    print(f.read())




