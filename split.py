a = '23'
aa = a[::-1]
slice1 = aa[:0]
slice2 = aa[0:]
b = a[:0]
c = a[0:]
output = set()
n = '1'
temp = ''
lst = [a, aa]

for item in lst:
    for x in range(0, len(a) + 1):
        temp = item[:x] + n + item[x:]
        output.add(temp)

print(output)
