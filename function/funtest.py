def f(a, L=[]):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(23))
print(f(12))