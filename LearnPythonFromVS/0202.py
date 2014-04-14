filename = 'spam.txt'
print(filename.endswith('.txt'))

print(filename.startswith('File:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('.')
pythonfiles = [name for name in filenames if name.endswith('.py')]
print(pythonfiles)
print(filenames)

