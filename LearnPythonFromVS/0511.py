import os
path ='/Users/beazlye/Data/data.csv'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp', 'data', os.path.basename(path)))
print(os.path.splitext(path))

names = os.listdir("c:\\")
files = [file for file in names if os.path.isfile(os.path.join('c:\\', file))]
print(files)