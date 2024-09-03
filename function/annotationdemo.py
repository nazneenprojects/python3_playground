# The following example has a required argument, an optional argument, and the return value annotated:
def poem(arg1: str, arg2: str = "WE") -> str:
    return arg1 + '  ' + arg2


print(poem('ME'))
print(poem.__annotations__)
