s = '{name} has {n} messages.'
news = s.format(name = 'Guido', n = 37)

print(news)

name = 'lipeng'
n = 12
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(a.__dict__)
print(s.format_map(vars(a)))