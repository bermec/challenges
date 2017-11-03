import datetime
dt = datetime.datetime
a = 2016
if a == dt.now().year:
    print('aye')
else:
    print('nay')



date = datetime.date(2012,12,11)
print(date.strftime("%B %#d %Y"))

