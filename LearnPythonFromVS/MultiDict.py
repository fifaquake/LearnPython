from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

print(e)

e['a'].add(2)
e['b'].add(2)
print(e)

from collections import OrderedDict
t = OrderedDict()
t['foo'] = 1
t['bar'] = 2
t['spam'] = 3
t['grok'] = 4

print(t)