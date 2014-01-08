def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts

acts = makeActions()
acts[0](2)
acts[1](2)