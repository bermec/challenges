''' Find the number of the year for the given date. For example, january 1st would be 1, and december 31st is 365.

for extra credit, allow it to calculate leap years, as well.

'''

from datetime import date

year = 2015
days = ''

cal = input('Enter date in the form: january 2nd  ')

months ={'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8,
         'september': 9, 'october': 10, 'november': 11, 'december': 12}
cal = cal.split()
month = months[cal[0]]

for char in cal[1]:
    if char.isnumeric():
        days += char

date0 = date(year, 1, 1)
date1 = date(year, month, int(days))
delta = date1 - date0
print(delta.days)