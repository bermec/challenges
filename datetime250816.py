import datetime
from datetime import date

def suffix(strng):
    if strng.endswith('1'):
        addition = 'st'
    elif strng.endswith('2') and not strng.startswith('1'):
        addition = 'nd'
    elif strng.endswith('3'):
        addition = 'rd'
    else:
        addition = 'th'
    return addition


candidates = '2015-07-01 2015-07-04 \
    2015-12-01 2016-02-03 \
    2015-12-01 2017-02-03 \
    2016-03-01 2016-05-05 \
    2017-01-01 2017-01-01 \
    2022-09-05 2023-09-04'
s = candidates.split()

dt = datetime.datetime
a = 2016
if a == dt.now().year:
    print('aye')
else:
    print('nay')

print(dt.now().year)



date = datetime.date(int())


m = suffix(str('%%B'))
num = '%%d%s' % m
var = "%%B %%#d%s %%Y" % m
print(date.strftime(var))