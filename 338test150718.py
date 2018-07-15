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


def same_month(a, b):
    """ num, num -> num
    calculate days elapsed in the same month """
    days_elapsed = (a - b)
    return days_elapsed


def months_elapsed_zero(a, b):
    days_elapsed = - a + b + 1
    return days_elapsed


def years_to_days(a, b):
    """str, str -> int
    Calculate years elapsed and convert into days"""

    years_elapsed = (a - b) - 1
    # store elapsed years
    year_store = []
    for x in range(1, years_elapsed + 1):
        elapsed_year = yr_now - x
        year_store.append(elapsed_year)
    # convert elapsed years into days
    total = 0
    for y in year_store:
        year_info = year_type(y)
        if year_info:
            total += 366
            months[2] = 29
        else:
            total += 365
            months[2] = 28
    return total


def months_elapsed_this_year(a, y):
    """ calculate days in elapsed months """
    day_total = 0
    months_elapsed = a - 1

    for x in range(1, a):
        year_info = year_type(y)
        if x == 2:
            if year_info:
                months[2] = 29
            else:
                months[2] = 28
            day_total += months[x]
        else:
            day_total += months[x]
    return day_total

def months_between_dates_same_year(a, b, y):
    """ int, int -> int
    calc months between dates occuring
    in the same year and convert into days"""
    monthz = a - b - 1
    year_info = year_type(y)
    if year_info:
        months[2] = 29
    else:
        months[2] = 28

    dayz = 0
    for x in range(b + 1, a):
        dayz += months[x]
    return dayz





dates = """2018 07 11      # wed
2018 06 30                 # sat 
2017 10 30                 # mon 
2016 2 29                   # mon
2015 2 28                   # sat
29 4 12                     # tues
570 11 30                   # sun
1066 9 25                   # mon
1776 7 4                    # thur
1933 1 30                   # thur
1953 3 6                    # fri
2100 1 9                    # sat
2202 12 15                  # wed
7032 3 26"""

dates = dates.splitlines()

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

for candidate_date in dates:
    candidate_yr = int((re.findall('^\d+', candidate_date))[0])
    candidate_month = int((re.findall('\s(\d+)?', candidate_date))[0])
    candidate_day = int((re.findall('\d+$', candidate_date))[0])
    day_accumulator = 0

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
    #================================ << ok
    years_elapsed = years_to_days(yr_now, candidate_yr)
    #day_accumulator -= years_elapsed
    months_elapsed = months_elapsed_this_year(month_now, yr_now)

    if candidate_month == month_now:
        days_elapsed = same_month(candidate_day, day_now)
        day_accumulator -= days_elapsed
        # days left in candidate month + 1
    elif (candidate_month != month_now) and (candidate_yr == yr_now):
        candidate_days_left_of_month = months[candidate_month] - candidate_day + 1
        # months elapsed to days elapsed
        months_between_dates = months_between_dates_same_year(month_now, candidate_month, yr_now)
        day_accumulator += months_between_dates
        day_accumulator += candidate_days_left_of_month
        days_used_this_month = day_now - 1
        day_accumulator += days_used_this_month
    elif years_elapsed <= 0:
        # months elapsed to days elapsed
        # months elapsed plus convert into days
        days_in_months_elapsed = 0
        days_used_this_month = day_now - 1
        # day_accumulator += days_used_this_month

        # process candidate months left
        for x in range(candidate_month +1, 13):
            months_left_in_cand_year = months[x]
            #day_accumulator -= months_left_in_cand_year

            year_info = year_type(yr_now)
            if year_info:
                months[2] = 29
            else:
                months[2] = 28
            # process year now months consumed
            for x in range(1, month_now - 1):
                days_in_months_elapsed += months[x]
                #day_accumulator -= days_in_months_elapsed
            #================================<< or

            if months_elapsed <= 0 and candidate_month == month_now:
                days_elapsed = same_month(candidate_day, day_now)
                day_accumulator -= days_elapsed #===============================<<
        else:
            # months gone to date
            for x in range(1, month_now):
                days_in_month = months[x]
                day_accumulator -= days_in_month #===============================<< this

            for x in range(candidate_month +1, 13):
                months_left_in_cand_year = months[x]
                day_accumulator -= months_left_in_cand_year

            #=======================<<

        print(day_accumulator)


        # -2 to convert to weekday
    # add 1 for calc

    candidate_day_of_week = (((this_day_number - day_accumulator) % 7) + 21) % 7
    candidate_day_of_week = day_of_week[candidate_day_of_week]

    print('candidate_day_of_week: ', candidate_day_of_week, candidate_date)
    print(day_accumulator)
    print()


# first two ok
