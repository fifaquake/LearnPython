import sys

# back up the sys.stdout
temp = sys.stdout

# set the new stdout as a file
sys.stdout = open('log.txt', 'a')
print('spam')
print(1, 2, 3)
sys.stdout = temp

print('back here')
print(open('log.txt').read())

# directly print to a file
lg = open('log.txt', 'w')
print(1,2,3, file = lg)