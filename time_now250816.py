import datetime
dt = datetime.datetime
a = 2016
if a == dt.now().year:
    print('aye')
else:
    print('nay')

m = datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%Y, %#m, %#d')

date = datetime.date(m)
print(date.strftime("%B %#d %Y"))

#print(type(date.strftime("%B %d")))

#date.strftime('X%d, X%m, %Y').replace('X0','X').replace('X','')
#print(date)