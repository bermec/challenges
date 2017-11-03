import re

eq1 = 'y =0.5x+1.3'
eq2 = 'y = -1.4x-0.2'
# extract numbers complete with signs
extract1 = re.findall('[-+]?\d*\.\d+|[-+]\d+', eq2)
extract2 = re.findall('[-+]?\d*\.\d+|[-+]\d+', eq1)
print(extract1)
print(extract2)

# extract email
email = 'I sent richie5@gmail.com a copy'

his_email = re.findall('\w*@\w*.\w*', email)
print(his_email)


eye = 'That Eye of newt stares at me.'
section = re.findall(r'([^.]*Eye of newt[^.]*\.)', eye)
print(section[0])

# extract Proposal to debt
text = 'Proposal will boost bailout fund, inject cash' \
           ' into banks and cut Greek debt says reports.'
pattern = re.compile(r'Proposal[\s\S]*?debt')
print(re.findall(pattern, text)[0])

# -- first and last ------------
a = 'm11uu2v And.'

c = re.findall('^\w', a)
b = re.findall('\w\.$', a)
print(c, b)

hand = open('blah.txt')
for line in hand:
    line = line.rstrip()
    if  line.find('From:') >= 0:
        print(line)

# is equivalent to

hand = open('blah.txt')
for line in hand:
    line = line.rstrip()
    if  re.search('From:', line):
        print(line)

# search looks for
# findall extracts

# ^X.*: start, char X, any character, many times, colon
# ^X-\S+:  Start, chars X-, any non-whitespace character, one or more times, colon
# [0-9]+  zero to nine one or more times

x = 'From: Using the :character'
y = re.findall('^F.+:', x)
print(y) # greedy
y = re.findall('^F.+?:', x)
print(y)  # stops at first character

x ='From rog@pynguins.com on Sat 13th'
y = re.findall('\S+@\S+', x)
print(y)  # push in a greedy manner outwards

y = re.findall('^From (\S+@\S+)', x)
print(y)

y = re.findall('@([^ ]*)', x)
print(y)  # any non-blank character, extract all in parenthesis but not '@'

# more specific...
y = re.findall('^From .*@([^ ]*)', x)
print(y)

# extract first, last
a = 'rtty'
b = re.findall('^\w(\w+)\w\Z', a)
print(b)

words ='cCvVf'
ans = re.findall('[^vVcC\s]', words)
if ans != []:
    print('Sorry, wrong input!')

words = '*-5+8-2'
ans = re.findall('[^\d+][^-]', words)
print('ans:', ans )

words = '*-5+8-2'
ans = re.findall('[-][\d]', words)
print(ans)

# match the rear words
line = '"Schoolmaster" ? "The classroom"'
ans = re.findall('(?<=\?\s\")[\w+].*[^\"\']', line)
print(ans)
# and the front
ans = re.findall('[^\'\"].*(?=\"\s\?)', line)
print(ans)

# substitute '0' and '.' with ""
s = '0.1230'
ans = re.sub("\.|0+", "", s)
print(ans)

# pull out letters only
v = '1234rtty5678'
test = re.findall('[a-z]+', v)
print(test)

def integers(s):
    ints = re.findall('(?<![.\d])\d+(?!\d*\.)', s)
    return ints

if __name__ == '__main__':

    candidate = '334ght5.89abc567'
    ans = integers(candidate)
    print('ans: ', ans)
