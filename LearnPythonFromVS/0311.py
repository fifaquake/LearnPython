import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))

print(random.sample(values, 3))

random.shuffle(values)
print(values)

print(random.randint(0, 100))
print(random.random())

random.seed()