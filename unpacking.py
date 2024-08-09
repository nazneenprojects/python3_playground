# Generating a list from range
range_list = list(range(1, 10))
print(range_list)

# Using *args to unpack the arguments for range
args = [1, 5]
range_from_args = list(range(*args))
print(range_from_args)



def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


parrot("voltage")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)