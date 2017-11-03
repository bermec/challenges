
import  datetime
from datetime import  date

def str2int(strng):
    out_lst = []
    for x in strng:
        if x.isdigit():
            x = int(x)
            out_lst.append(x)
    out_tup = tuple(out_lst)
    return out_tup


a = '2015-07-01 2019-04-06'
a = a.split()
print('a ', a)

b = a[0].split('-')
print('b', b)

year = int(b[0])
month = int(b[1])
day = int(b[2])

z = datetime.date(year, month, day)
print(z)
print(type(z))
nice_z = date.strftime(z, '%#B, %#d, %Y')
print('nice_z: ', nice_z)
