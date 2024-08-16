x = input("Enter a number: ")

x = int(x)

if (x % 2) == 0:
    print("Even")
elif (x % 2) != 0:
    print("Odd")
else:
    print("not valid number")

words = ["pen", "window", "tree"]

for i in words:
    print(i, len(i), "\n")

users = {"hans": "taxi", "hamburg": "elbe", "sang": "karat"}
for l1, l2 in users.copy().items():
    if l2 == 'karat':
        del users[l1]
print(users)

for i in range(10):
    print(i + 1, i)

fest = ["merry", "xmas", "happy", "new", "year"]

for i in range(len(fest)):
    print(i, fest[i])

print(enumerate(fest))

for i in range(5):
    if i % 2 == 0:
        print(i, "even")
        continue
    print(i, "odd")

while True:
    pass


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 500:
            return "Internal Server Error"
        case 404 | 404 | 403:
            return "Not found"
        case _:
            return "Something wrong"


