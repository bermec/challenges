a = '12345'

for x in range(0, len(a)):
    b = a[x:] + a[:x]
    print(b)