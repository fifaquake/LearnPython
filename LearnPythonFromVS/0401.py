with open(r'.\0108.py') as f:
    try:
        while True:
            line = next(f)
            print(line)
    except StopIteration:
        pass

items = [1, 2, 3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except:
    pass