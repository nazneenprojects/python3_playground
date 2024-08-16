
"""
This file demonstrate Python data structures
Date: 23 July 2024
Author: Nazneen Mulani
"""

from math import pi
from collections import deque

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

    complexCal = [ str(round(pi, i)) for i in range(1 ,6)]
    print(complexCal)

    letters = ['a', 'b', 'c', 'd']
    letters[2:4] =['C', 'D']
    print(len(letters))
    print(letters)
    letters[2:4] = []
    print(letters)
    letters[:] = []
    print(letters)
    print(len(letters))

    #Nested List
    naturalNumber = [0, 1, 2, 3, 4, 5]

    matrix = [naturalNumber,
              [1, 2, 3, 4],
              [4, 6, 87, 8],
              [2, 6, 7, 7, 3],
              ]

    print(matrix)
    print("printing transpose of matrix -")
    print( [[row[i] for row in matrix] for i in range(4)] )

    print(list(zip(*matrix)))


    # This below list represents squares of number from 1 to 20....
    sample = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

    #append
    sample.append(441)
    print(sample)
    #a[len(a):] = [x]
    sample[len(sample):] = [484]
    print(sample)

    #extend
    sample_more = [529]
    sample.extend(sample_more)
    print(sample)
    # a[len(a):] = iterable
    sample_more = [576]
    sample[len(sample):] = sample_more

    #enumerate
    for index, value in enumerate(sample):
        print(f"Position {index} : {value}")

    #insert
    # similar to a.insert(len(a), x)
    sample.insert(24, 625)
    print(sample)

    #sample.remove(24)  ....ERROR
    sample.remove(625)
    print(sample)

    sample.pop()
    print("Removed the last item", sample)

    sample.pop(22)
    print("Removed the ith item ", sample)

    #index
    print(sample.index(484))
    print(sample.index(484, 10))
    print(sample.index(484, 10, 100))

    # count the appearance of x
    print(sample.count(121))

    #sort
    sample.sort()
    print(sample)
    sample.sort(reverse=True)
    print(sample)
    sample.reverse()
    print(sample)
    sample_new = sample.copy()
    print("sample_new :" ,sample_new)
    sample_copy = sample[:]
    print("sample_shallow copy :", sample_copy)
    del(sample_copy[10])
    print(sample_copy)
    del sample_copy

    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)



def stack_demo():
    """

    :rtype: object
    """
    print("Stack in Python 3")
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)


def queue_demo():
    print("Queue in Pythn 3")
    queue = deque(["Future" , "depends" , "on"])
    queue.append("what")
    queue.append("we")
    queue.append("do in present")
    print(queue)
    queue.popleft()
    print(queue)
    queue.popleft()
    print(queue)



def tuple_sequence_demo():
    """

    :rtype: object
    """
    print("Tuple in python 3")

    # tuple packing
    t = 12345, 54321, 'hello!'
    print(t[0])
    print(t)

    #nested tuples
    u = t, (1, 2, 3, 4, 5)
    print(u)

    #t[0]= 65555 error bcz tuples are immutable

    # but they can contain mutable objects:
    v = ([1, 2, 3], [3, 2, 1])

    # Sequence Unpacking
    x, y, z = t

    # empty
    empty = ()
    # only 1 element in tuple
    singleton = 'hello',


    # sequence
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    for i in reversed(range(1, 10, 2)):
        print(i)

    for i in sorted(range(1, 10, 2)):
        print(i)

    #new sorted list while leaving the source unaltered.
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(basket):
        print(i)

    #Using set() on a sequence eliminates duplicate elements
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)





def set_demo():
    """

    :rtype: object
    """
    print("Set in python 3")
    basket = {'apple', 'orange', 'pear', 'aaple'}
    print(basket) #ndupplicates will be removed
    print('apple' in basket)
    print('avocado' in basket)
    a= set('nazneen')
    b= set('naz')

    #The displayed order is not indicative of randomness or reverse sorting; it's based on how the set is internally managed by Python's hash table implementation.
    print(a)
    print(b)
    print(sorted(a))  # Output: ['a', 'e', 'n', 'z']
    print(sorted(b))  # Output: ['a', 'n', 'z']



    print(a, b)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)

    # set comprehensions
    a = { X for X in 'abracadabra' if X not in 'abc'}
    print(a)



def dictionary_demo():
    """

    :rtype: object
    """
    print("Dictionary in pythin3")
    dict_sample = {'stock': 123, 'name': 122}
    print(dict_sample)
    dict_sample['earning'] = 123455
    print(dict_sample)
    print(sorted(dict_sample))
    print('stock' in dict_sample)

    # dict() constructor
    sample_doct = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(sample_doct)

    print({x: x ** 2 for x in (2, 4, 6)})

    keyarg_dict = dict(sape=4139, guido=4127, jack=4098)
    print(keyarg_dict)

    knights = {'jingle': 'bell', 'mingle': 'dell', 'jingle': 'bell'}
    for k, v in knights.items():
        print(k, v)







list_demo()
stack_demo()
queue_demo()
tuple_sequence_demo()
set_demo()
dictionary_demo()
