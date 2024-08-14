"""
Generators are a simple and powerful tool for creating iterators.
They are written like regular functions but use the yield statement whenever they want to return data
Each time next() is called on it, the generator resumes where it left off
"""

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('HAMBURG'):
    print(char)



# Generator Expression
print(sum(i*i for i in range(10)) )

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))