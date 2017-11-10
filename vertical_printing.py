import itertools

candidates = '''Kernel
Microcontroller
Register
Memory
Operator'''
candidates = candidates.split()

txt = ''

for word in candidates:
    txt += word + ' '


l = txt.split(' ')

for i in itertools.zip_longest(*l, fillvalue=" "):
    if any(j != " " for j in i):
        print(" ".join(i))