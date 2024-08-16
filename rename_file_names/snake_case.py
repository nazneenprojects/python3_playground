import os
import re

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

directory = '/home/user/Documents/python'

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith('.py'):
            new_name = camel_to_snake(filename[:-3]) + '.py'
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} to {new_path}')
