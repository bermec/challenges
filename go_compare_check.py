
import re
import datetime
from datetime import date
import calendar



dates = """2020 1 1
2100 1 9
2202 12 15
7032 3 26"""

dates = dates.splitlines()

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

day_of_week = {1: 'Monday',
               2: 'Tuesday',
               3: 'Wednesday',
               4: 'Thursday',
               5: 'Friday',
               6: 'Saturday',
               0: 'Sunday'}

for candidate_date in dates:
    year = int((re.findall('^\d+', candidate_date))[0])
    month = int((re.findall('\s(\d+)?', candidate_date))[0])
    day = int((re.findall('\d+$', candidate_date))[0])

    a = (14 - month) // 12
    y = year - a
    m = month + 12*a - 2
    weekday =(day + y + y//4 - y//100 +y//400 + (31 *m) // 12) % 7
    print(day_of_week[weekday])

day_of_week = {0: 'Monday',
               1: 'Tuesday',
               2: 'Wednesday',
               3: 'Thursday',
               4: 'Friday',
               5: 'Saturday',
               6: 'Sunday'}

def year_type(y):
    """ int -> str
    leap year check"""
    leap = True
    if ((y % 4 == 0 and not y % 100 == 0) or (y % 400 == 0)):
        return leap
    return False


def same_month(a, b):
    """ num, num -> num
    calculate days elapsed if dates
     are the same month """
    days_elapsed = (a - b)
    return days_elapsed


def cand_days_in_month(a, b, y):
    """ days left in candidate month """
    year_info = year_type(y)
    if year_info and a == 28:
        a = 29
    days_left = a - b + 1
    return days_left


def months_elapsed_zero(a, b):
    """ this month follows candidate month """
    days_elapsed = - a + b + 1
    return days_elapsed


def days_this_month(a):
    """ days that have passed
    this month """
    days = a - 1
    return days


def years_to_days(a, b):
    """str, str -> int
    Calculate years elapsed and convert into days"""
    # store elapsed years
    year_store = []
    for x in range(a + 1, b):
        elapsed_year = x
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


def future_years_to_days(a, b):
    """str, str -> int
    Calculate years elapsed and convert into days"""

    years_elapsed = (b - a) - 1
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


def future_months_between_dates_same_year(a, b, y):
    """ int, int -> int
    calc months between dates occurring
    in the same year and convert into days"""
    monthz = a - b - 1
    year_info = year_type(y)
    if year_info:
        months[2] = 29
    else:
        months[2] = 28

    dayz = 0
    for x in range(a + 1, b):
        dayz += months[x]
    return dayz


def cand_months_elapsed(a):
    days_in_months_elapsed = 0
    for x in range(a + 1, 13):
        months_left_in_cand_year = months[x]
        # day_accumulator -= months_left_in_cand_year

        year_info = year_type(yr_now)
        if year_info:
            months[2] = 29
        else:
            months[2] = 28
        days_in_months_elapsed = 0
        for x in range(a + 1, 13):
            months_left_in_cand_year = months[x]
            # day_accumulator -= months_left_in_cand_year

            year_info = year_type(yr_now)
            if year_info:
                months[2] = 29
            else:
                months[2] = 28

            days_in_months_elapsed += months[x]

    return days_in_months_elapsed


def future_candidate_months_to_go(a, y):
    """ months to go in candidate year """
    days = 0
    for x in range(a - 1, 0, -1):
        year_info = year_type(y)
        if year_info:
            months[2] = 29
        else:
            months[2] = 28

        days += months[x]
    return days


def future_months_to_go_this_year(a, y):
    """ months to go in candidate year """
    days = 0
    for x in range(a + 1, 13):
        year_info = year_type(yr_now)
        if year_info:
            months[2] = 29
        else:
            months[2] = 28

        days += months[x]
    return days


def future_cand_days_in_month(a):
    days = 0
    days += a
    return days


def days_to_go(d, m):
    days = months[m] - d
    return  days


def ordinal(now, other):
    marker = False
    now = str(now)
    year = int((re.findall('^\d+', now))[0])
    month = int((re.findall('-(\d+)-', now))[0])
    day = int((re.findall('\d+$', now))[0])
    d = datetime.date(year, month, day)
    today = d.toordinal()
    year = int((re.findall('^\d+', other))[0])
    month = int((re.findall('\s(\d+)\s', other))[0])
    day = int((re.findall('\d+$', other))[0])
    e = datetime.date(year, month, day)
    other_date = e.toordinal()
    if other_date > today:
        marker = True
    return marker



for candidate_date in dates:
    candidate_yr = int((re.findall('^\d+', candidate_date))[0])
    candidate_month = int((re.findall('\s(\d+)?', candidate_date))[0])
    candidate_day = int((re.findall('\d+$', candidate_date))[0])
    day_accumulator = 0

    date_now = str(datetime.date.today())
    # weekday
    weekday = datetime.datetime.today().weekday()
    weekday = day_of_week[weekday]
    # print("today's weekday: ", weekday)
    targetval = weekday
    for key in day_of_week.keys():
        if day_of_week[key] == targetval:
            break
    this_day_number = key
    yr_now = int(date_now[:4])
    # print('yr_now: ', yr_now)
    month_now = int(date_now[5:7])
    # print('month_now: ', month_now)
    day_now = int(date_now[8:10])
    # print('day_now: ', day_now)
    my_date = date.today()
    today_is = calendar.day_name[my_date.weekday()]
    # ================================ << ok
    # day_accumulator -= years_elapsed
    months_elapsed = months_elapsed_this_year(month_now, yr_now)
    years_elapsed = years_to_days(yr_now, candidate_yr)
    future_years_elapsed = future_years_to_days(yr_now, candidate_yr)

    flag = ordinal(my_date, candidate_date)
    day_accumulator = 0
    if candidate_month == month_now and (candidate_yr == yr_now):
        days_elapsed = same_month(candidate_day, day_now)

        if flag:
            day_accumulator += days_elapsed
        else:
            day_accumulator -= days_elapsed


        # days left in candidate month + 1
    elif (candidate_month != month_now) and (candidate_yr == yr_now):

        future_cand_days_in_month = candidate_day
        future_days_in_month_now = months[month_now] - day_now
        future_months_between_dates = future_months_between_dates_same_year(
            month_now, candidate_month, yr_now)

        # if flag....
        candidate_days_left_of_month = cand_days_in_month(
            months[candidate_month], candidate_day, candidate_yr)
        # months elapsed to days elapsed
        months_between_dates = months_between_dates_same_year(month_now,
                                                              candidate_month,
                                                              yr_now)
        days_used_this_month = day_now - 1

        if flag:
            day_accumulator += future_cand_days_in_month + future_days_in_month_now + future_months_between_dates
        else:
            day_accumulator += months_between_dates + candidate_days_left_of_month + days_used_this_month

    elif (future_years_elapsed == 0) and (years_elapsed == 0):
        candidate_days_left_of_month = cand_days_in_month(
            months[candidate_month], candidate_day, candidate_yr)
        # days elapsed this month
        days_used_this_month = days_this_month(day_now)
        # day_accumulator += days_used_this_month

        # process months elapsed candidate year
        days_in_months_elapsed = cand_months_elapsed(candidate_month)

        months_this_year = months_elapsed_this_year(month_now, yr_now)

        future_months = future_months_between_dates_same_year(month_now, 13, yr_now)
        days_to_run = days_to_go(day_now, month_now)
        cand_days = future_cand_days_in_month(candidate_day)
        if flag:
            day_accumulator += future_months + days_to_run + cand_days
        else:
            day_accumulator += candidate_days_left_of_month + days_used_this_month + days_in_months_elapsed + months_this_year


    else:
        future_cand_days_in_month = candidate_day - 1
        future_cand_months = future_candidate_months_to_go(candidate_month,
                                                           candidate_yr)
        check = months[candidate_month]
        candidate_days_left_of_month = cand_days_in_month(
            months[candidate_month], candidate_day, candidate_yr)
        # days elapsed this month
        days_used_this_month = days_this_month(day_now)
        # day_accumulator += days_used_this_month

        # process months elapsed candidate year
        days_in_months_elapsed = cand_months_elapsed(candidate_month)
        months_this_year = months_elapsed_this_year(month_now, yr_now)
        # process months elapsed candidate year
        future_days_in_months_elapsed = cand_months_elapsed(candidate_month)
        future_days_in_month_now = months[month_now] - day_now + 1
        future_months_to_go = future_months_to_go_this_year(month_now, yr_now)

        if flag:
            day_accumulator += future_years_elapsed + future_days_in_month_now + \
                               future_cand_days_in_month + future_months_to_go + future_cand_months
        else:
            day_accumulator += candidate_days_left_of_month + days_used_this_month \
                               + days_in_months_elapsed + months_this_year + years_elapsed

    # convert to weekday

    if flag:
        candidate_day_of_week = (((this_day_number + day_accumulator) % 7) + 21) % 7
    else:
        candidate_day_of_week = (((this_day_number - day_accumulator) % 7) + 21) % 7
    candidate_day_of_week = day_of_week[candidate_day_of_week]

    print('candidate_day_of_week: ', candidate_day_of_week, day_accumulator, candidate_date)
    print()
