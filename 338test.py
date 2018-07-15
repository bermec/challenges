'''
What day of the week did hitler get elected on?

What day of the week did the Normans invade Britain on?

What day of the week did Jesus die on?

What day of the week did MacDonald get founded on?

Today we're gonna find out

For todays challenge you are allowed to use your languages
built in Calender functions/classes.

But it's more interesting if you do the calculation yourself :)
Hint

It's leap-year if the year is divisible by 4

Ignore leap-year if the year is divisible by 100

Ignore previous rule if the year is divisible by 400
Input example

The input will be 3 integers as such:

YEAR MONTH DATE

Limits for the 3 integers:

8000 > YEAR > 0

13 > MONTH > 0

32 > DATE > 0

Sorry to anyone starting at 0.

January is 1 and December is 12

Assume all dates to be correct (i.e. no 31th of february)

Input will look like:

2017 10 30

Output example

Output is simply the day of the week of the given date,
for above it would be:

Monday

Challenge input

2017 10 30
2016 2 29
2015 2 28
29 4 12
570 11 30
1066 9 25
1776 7 4
1933 1 30
1953 3 6
2100 1 9
2202 12 15
7032 3 26

'''
import datetime
from datetime import date
import calendar
import re

def year_type(y):
    """ int -> str
    leap year check"""
    leap = True
    if (y % 100 == 0 or y % 4 == 0) and not (y % 400 == 0):
        return leap
    return False


a_year = 365
leap_year = 366
day_accumulator = 0



months = {1: 31,
          2: 28,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31}

day_of_week = {0: 'Monday',
               1: 'Tuesday',
               2: 'Wednesday',
               3: 'Thursday',
               4: 'Friday',
               5: 'Saturday',
               6: 'Sunday'}



#-- program ---------------------------------


candidate_date = '2018 07 10'
print('candidate: ', candidate_date)
candidate_yr = int((re.findall('^\d+', candidate_date))[0])
candidate_month = int(candidate_date[5:7])
candidate_day = int(candidate_date[8:10])

date_now = str(datetime.date.today())
# weekday
weekday = datetime.datetime.today().weekday()
weekday = day_of_week[weekday]
print("today's weekday: ", weekday)
targetval = weekday
for key in day_of_week.keys():
    if day_of_week[key] == targetval:
        print("found", targetval, "at key", key)
        break
this_day_number = key
print('this_days number: ', this_day_number)
yr_now = int(date_now[:4])
#print('yr_now: ', yr_now)
month_now = int(date_now[5:7])
#print('month_now: ', month_now)
day_now = int(date_now[8:10])
#print('day_now: ', day_now)
my_date = date.today()
today_is = calendar.day_name[my_date.weekday()]
#print('today_is: ', today_is)
#day_accumulator += day_now
print('day_now - 1: ', day_accumulator)  #================================ << ok



years_elapsed = (yr_now - candidate_yr) -1
print('years_elapsed: ', years_elapsed)
# store elapsed years
year_store = []
for x in range(1, years_elapsed + 1):
    elapsed_year = yr_now - x
    year_store.append(elapsed_year)
print(year_store)
# convert elapsed years into days
temp = 0
for y in year_store:
    year_info = year_type(y)
    if year_info:
        temp += 366
        months[2] = 29
    else:
        temp += 365
        months[2] = 28
day_accumulator -= temp
print('days(years): ', temp)  #====================================<< ok

# days left in candidate month + 1
if candidate_month != month_now:
    candidate_days_left_of_month = months[candidate_month] - candidate_day + 1
    print('candidate month days left: ', candidate_days_left_of_month)
    day_accumulator += candidate_days_left_of_month

    days_used_this_month = day_now - 1
    day_accumulator += days_used_this_month

# months elapsed plus convert into days
days_in_months_elapsed = 0
if years_elapsed <= 0:
    # months elapsed.
    months_elapsed = (month_now) - (candidate_month) -1
    for x in range(month_now - 1, candidate_month, -1):
        days_in_months_elapsed += months[x]
    day_accumulator += days_in_months_elapsed
     #================================<< or

    if months_elapsed <= 0 and candidate_month == month_now:
        days_elapsed = (candidate_day - day_now)
        day_accumulator -= days_elapsed #===============================<<
    elif months_elapsed <= 0:
        days_elapsed = - candidate_days_left_of_month + day_now + 1
        day_accumulator += days_elapsed
else:
    # months gone to date
    for x in range(1, month_now):
        days_in_month = months[x]
        day_accumulator -= days_in_month #===============================<< this

    for x in range(candidate_month +1, 13):
        months_left_in_cand_year = months[x]
        day_accumulator -= months_left_in_cand_year

    candidate_days_remaining = months[candidate_month] - candidate_day + 1
    day_accumulator += candidate_days_remaining #=======================<<

print(day_accumulator)


# -2 to convert to weekday
# add 1 for calc

candidate_day_of_week = ((this_day_number - day_accumulator % 7) + 7) % 7
candidate_day_of_week = day_of_week[candidate_day_of_week]

print('candidate_day_of_week: ', candidate_day_of_week)
print(day_accumulator)



