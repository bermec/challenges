import re
# days before 1990
a =  '2 The Godfather (1972)'
ans = re.findall(r'.*\(19[1-8]\d\)', a)
print('days before 1990: ', ans)

# 24bit hex colours
a = 'AliceBlue #F0F8FF'
ans = re.findall(r'#[0-9A-F]{6}', a)
print('24bit: ', ans)

# 24 and 32bit colours
a = '#848484 White #a9a9a9a9 #CC'
ans = re.findall(r'#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})', a)
print('24 &32bit: ', ans)

# grayscale colours
a = '#343434, #CCC, #c1c1c1'
ans = re.search(r'#([0-9A-Fa-f])([0-9A-Fa-f])((?=\2)\1|(?:\1\2){2})\b', a)
print('grayscale: ', ans.group())

# backreference
a = 'Paris in the the spring'
p = re.findall(r'(\w+)\s+\1', a)
#>>>'the the'
print('1: ', p)

a = 'llandudno'
p = re.findall(r'(\w)\1', a)
print(p)

a = 'llllil'
p = re.search(r'(\w)\1\1\1', a)
print('backreference: ', p.group())

p = re.sub(p.group(), 'L' * 4, a)
print(p)