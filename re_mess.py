import re

a = '123-banana-456'
sample = re.findall(r'(?<=123-)((banana)(?=-456))', a)
print(sample)
rep = 'apple'
a = re.sub(sample[0][0], rep, a)
print(a)

a = '...#ll#.....#.....'
sample = re.findall(r'(?<=^...#)((.*)(?=#)|(?=#))', a)
print(sample[0])
rep = '&'


a = 'streets'
# =============================
# lookahead
# =============================
b = re.findall(r't(?=s)', a)
print('Second  or rear t: ', b)



# =============================
# lookahead
# =============================
b = re.findall(r't(?=s)', a)
print('Second t: ', b)

b = re.findall(r'.*t(?=s)', a)
print(b)

b = re.findall(r'.*t(?=s)', a)
print(b)
# stree't's (ahead of s)

# =============================
# negative lookahead
# =============================
b = re.findall(r't(?!s)', a)
print('First t: ', b)

b = re.findall(r't.*(?!s)', a)
print(b)



a = '....#..#...#...'

sample = re.findall(r'(?<=\.\#)((\.+)(?=\#\.+\#\.+))', a)
print(sample)