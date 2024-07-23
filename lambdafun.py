def sqr(n):
    print("The square of given number ", n, "is :")
    return lambda: n ** 2


result = sqr(25)
square_value = result()
print(square_value)

## sorting
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


## demo of lambda

def quote(author):
    """
    This is my first docstring in python
    :rtype: object
    """
    q = "Half finished work generally proves to be labor lost."
    return lambda:f"{q} by {author}"


output =quote("Abraham lincon")
toprint = output()
print(toprint)
print(quote.__doc__)
