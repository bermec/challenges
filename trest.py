s = [2, 2, 1]
mx = []
for x in range(len(s)):
    if s[x] == max(s):
        mx.append(x)
print(mx)
indx = mx[-1]
print(indx)