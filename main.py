# This is a sample Python script.
from ArrowPrint import printarrow
from Literals import printing_literals


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_output(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome!, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("My name is ", end="")
    print("Monty Python.")
    print("My", "name", "is", "Monty", "Python.", sep="-")

    print("My", "name", "is", sep="_", end="*")
    print("Monty", "Python.", sep="*", end="*\n")

    print("Programming", "Essentials", "in", sep="***", end="...")
    print("Python")

    print("My\nname\nis\nBond.", end=" ")
    print("James Bond.")

    #syntax error
    #print(sep="&", "fish", "chips")

    print('Greg\'s book.')
    print("'Greg's book.'")
    print('"Greg\'s book."')
    print("Greg\'s book.")
    # SyntaxError, because the ' symbol in the Greg's book. string requires an escape character.
    #print('"Greg's book."')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_output('This project is created as a part of python 3 hands on learning ')
    #printarrow()
    printing_literals()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
