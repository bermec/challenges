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



dt = datetime.datetime
a = 2016
if a == dt.now().year:
    print('aye')
else:
    print('nay')

print(dt.now().year)



date = datetime.date(2012, 1, 22)


m = suffix(str('%%B'))
num = '%%d%s' % m
var = "%%B %%#d%s %%Y" % m
print(date.strftime(var))

'''
from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

print(custom_strftime('%B {S}, %Y', dt.now()))


# -------------------------------------------------------------------------

#d = '2002-03-01'
d= date.strftime("%d-%m-%Y")
print('d = ', d)
#d = '11/03/02'
d= date.strftime("%#d. %B %Y")
print('2nd_d = ', d)
#'Monday 11. March 2002'
#'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
#'The day is 11, the month is March.'
'''