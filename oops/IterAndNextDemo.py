import page


class Reverse :
    """ Iterator for looping sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return  self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)

#unique_words = set(word for line in page  for word in line.split())

#valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))