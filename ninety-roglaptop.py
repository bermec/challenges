a = ['1', '2', '3']
b = ['4', '5', '6']
c = ['7', '8', '9']

d = []
e = []
f = []

for x in range(0, len(a)):
    d.append(a[x])
    d.append(a[x+len(a) - 1])
    d.append(a[x + (len(a) * 2) - 1])
print(d)
