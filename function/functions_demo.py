
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()


fib(20)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5


def f(arg=i):
    print(arg)


i = 6



def f1(a, L=[]):
    L.append(a)
    return L

def f2(a, L=""):
    L = a
    return L


print(f1("ham"))
print(f1("burg"))


print(f2("naz"))
print(f2("neen"))