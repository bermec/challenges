import re
s = '0.1230'

ans = re.sub("\.|0+", "", s)
print(ans)

import re
t = '06051230'

ans = re.sub("^0+", "", t)
print(ans)


v = '1234rtty5678'
test = re.findall('[a-z]+', v)
print(test)

# negative lookahead (?!) find expression A where B does not follow A(?!B)
test = re.findall('\d+(?!r)', v)
print(test)

# positive lookahead (?=) find expression A where B follows  A(?=B)
test = re.findall('\d+(?=r)', v)
print(test)

# look behind positive (?<=) find expression A where B precedes (?<=B)A
test = re.findall('(?<=y)\d+', v)
print(test)

# look behind negative (?<!) find expression A where B precedes (?<!B)A
test = re.findall('(?<!\s)\d+', v)
print(test)

a = 'qwerty56.56rrr567'
test = re.findall('(?<!\.)\d+(?!\.)', a)
print(test)