import random
d = {'a':1, 'b':2, 'c':3}

for key, value in sorted(d.items(), key=lambda x: random.random()):
    print(key, value)