dict1 = {'a':1, 'b':2, 'c':3}
print(dict1)



import random


keys =  list(dict1.keys())      # Python 3; use keys = d.keys() in Python 2
random.shuffle(keys)
result = [(key, dict1[key]) for key in keys]

# shuffle k, v pairs
d = {'a':1, 'b':2, 'c':3}

for key, value in sorted(d.items(), key=lambda x: random.random()):
    print(key, value)