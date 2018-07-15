'''245
tomorrow
2010-dec-7
OCT 23
1 week ago
next Monday
last sunDAY
1 year ago
1 month ago
last week
LAST MONTH
10 October 2010
an year ago
2 years from tomoRRow
1 month from 2016-01-31
4 DAYS FROM today
9 weeks from yesterday'''

import datetime
import calendar

def submonth(d):
    year, month = d.year, d.month
    if month == 1:
        year -= 1; month = 12
    else:
        month -= 1
    try:
        return d.replace(year=year, month=month)
    except ValueError:
        return d.replace(day=1) - datetime.timedelta(1)


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12)
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)

def interpret(strng):
    'today' = datetime.date.today()
    'yesterday' = datetime.timedelta(days=-1)
    'week' = datetime.timedelta(days=7)
    weeks = week
    output = ''
    strng = strng.split()
    for item in strng:
        output += item

    return today + output

if __name__ == '__main__':
    today = datetime.date.today()
    this_month = today.month


    one_day = datetime.timedelta(days=1)
    print('tomorrow: ', today + one_day)

    date = datetime.date(2010, 12, 7)
    print('2010-dec-7: ', date)

    this_year = today.year  # oct 23
    date = datetime.date(this_year, 10, 23)
    print('OCT 23: ', date)

    week_ago = datetime.timedelta(days=7)
    print('one week ago: ', today - week_ago)

    weekday = datetime.date.weekday(today)
    time_till_next_monday = (0 - weekday) % 7  # (n - weekday) to add time
    days_till = datetime.timedelta(days=time_till_next_monday)
    print('next Monday: ', today + days_till)

    last_sunday = (weekday - 6) % 7  # (weekday - n) to deduct time  # last sunday
    days_till = datetime.timedelta(days=last_sunday)
    print('last sunDay: ', today - days_till)

    year_ago = datetime.timedelta(days=365)
    print('1 year ago: ', today - year_ago)

    ans = submonth(datetime.date.today())
    print('1 month ago: ', ans)

    one_week = datetime.timedelta(days=7)
    print('last week: ', today - one_week)

    ans = submonth(datetime.date.today())
    print('LAST MONTH: ', ans)

    date = datetime.date(2010, 10, 10)
    print('10 October 2010: ', date)

    year_ago = datetime.timedelta(days=365)
    print('an year ago: ', today - year_ago)

    day = datetime.timedelta(days= 1)
    year = datetime.timedelta(days= 365)
    ans = today + day + 2 * year
    print('2 years from tomoRRow: ', ans)

    the_date = datetime.date(2016, 1, 31)
    ans = add_months(the_date, 1)
    print('1 month from 2016-01-31: ', ans)

    four_days = datetime.timedelta(days=4)
    print('4 DAYS FROM today: ', today + four_days)

    nine_weeks = datetime.timedelta(days=63)
    print('9 weeks from yesterday: ', today + nine_weeks - one_day)

    yesterday = datetime.timedelta(days=-1)
    print(today + yesterday)

    the_date = '9 weeks from yesterday'
    ans = interpret(the_date)
    print(add_months())






'''
print ('ordinal:', today.toordinal())
print ('Year:', today.year)
print ('Mon :', today.month)
print ('Day :', today.day)
'''
