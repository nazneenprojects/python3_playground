
for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for element in { 1, 2, 3}:
    print(element)

for key, element in {'a': 1, 'b': 2, 'c': 3}.items():
    print(key ,  element)

for char in "123":
    print(char)

for line in open("../input_output/example.txt"):
    print(line, end='' )
    print("\n")


s = 'Life is like riding a bicycle. To keep your balance, you must keep moving. , Einstein'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))