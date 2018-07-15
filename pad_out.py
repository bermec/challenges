
import re

def pad(s):
    nums = re.findall('\^(\d+)', s)
    s = s.split()
    s = list(s)
    print(s)
    for x in range(0, len(s)):
        m = s[x]
        end = m[-1]
        if str(x) in nums:
            continue
        else:
            s.insert(x, '0x^' + str(x))
    return s






a = ' 4x^4 -3x^3 +1x^1 -3x^0'

b = pad(a)

print(b)