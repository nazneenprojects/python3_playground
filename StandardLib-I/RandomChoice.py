import random
var_random = random.choice(['apple', 'mango', 'banana'])
print(var_random)
var_sample = random.sample(range(100), 10)   # sampling without replacement
print(var_sample)

print(random.random())    # random float

print(random.randrange(6))