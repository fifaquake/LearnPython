def tester(start):
    state = start
    def nested(label):
        nonlocal state
        state += 1
        print(label, state)
    return nested

F = tester(0)
F('spam')