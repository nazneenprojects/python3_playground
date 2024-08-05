

"""
This file demonstrate Pythin data structures
Date: 23 July 2024
Author: Nazneen Mulani
"""

from math import pi
def list_demo():
    """

    :rtype: object
    """
    print("List in Python 3")

    squares = []
    for x in range(1, 11):
        squares.append(x ** 2)
    print(squares)

    sqauresUsingLambda = list(map(lambda x: x ** 2, range(5)))
    print(sqauresUsingLambda)
    squaresUsingForLoop = [x ** 2 for x in range(3)]
    print(squaresUsingForLoop)

    vec = [12, 23, 45, -34, -56]
    print([x * 2 for x in vec])
    print([x for x in vec if x >= 0])
    print([hex(x) for x in vec])

    hike = ["shoes  ", "  t ent", "bag  ", "   first aid"]
    new_hike = [n.strip() for n in hike]
    print(new_hike)

    #create a list of two tuple
    tupleList = [(x, x ** 2) for x in range(6)]
    print(tupleList)

    vec = [[12, 2, 3], [45, 5, 67], [6, 45, 89]]
    vecFlat = [ i for elem in vec for i in elem]
    print(vecFlat)

    complexCal = [ str(round(pi, i)) for i in range(1,6)]
    print(complexCal)


    #Nested List
    matrix = [
        [1,2,3,4],
        [4,6,87,8],
        [2,6,7,7,3],
    ]
    print(matrix)


def stack_demo():
    """

    :rtype: object
    """
    print("Stack in Python 3")


def queue_demo():
    print("Queue in Pythn 3")


def tuple_demo():
    """

    :rtype: object
    """
    print("Tuple in python 3")


def set_demo():
    """

    :rtype: object
    """
    print("Set in python 3")


def dictionary_demo():
    """

    :rtype: object
    """
    print("Dictionary in pythin3")


list_demo()
