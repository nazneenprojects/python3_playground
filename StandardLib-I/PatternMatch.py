import re

found = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(found)

subparts = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(subparts)

relacement = 'tea for too'.replace('too', 'two')
print(relacement)