X = 99

def func(Y):
    Z = X + Y
    return Z

print(func(1))

x = 0
y, z = 1, 2
def all_global():
    global x
    x = y + z

all_global()

print(x)

def func1():
    x = 4
    action = (lambda n : x ** n)
    return action

x = func1()
print(x(2))