'''
The goal of this challenge is to implement a way of converting
two dates into a more friendly date range that could be presented to a user.
It must not show any redundant information in the date range. For example,
if the year and month are the same in the start and end dates, then only
the day range should be displayed. Secondly, if the starting year is the
current year, and the ending year can be inferred by the reader, the year
should be omitted also (see below for examples).
Formal Inputs and Outputs
Input Description

The input will be two dates in the YYYY-MM-DD format, such as:

    2015-07-01 2015-07-04
    2015-12-01 2016-02-03
    2015-12-01 2017-02-03
    2016-03-01 2016-05-05
    2017-01-01 2017-01-01
    2022-09-05 2023-09-04

Output Description

The program must turn this into a human readable date in the Month Day,
Year format (omitting the year where possible).
These outputs correspond to the above inputs:

    July 1st - 4th
    December 1st - February 3rd
    December 1st, 2015 - February 3rd, 2017
    March 1st - May 5th, 2016
    January 1st, 2017
    September 5th, 2022 - September 4th, 2023

'''

import re
import datetime
from datetime import date


def suffix(strng):
    if strng.endswith('1'):
        addition = 'st'
    elif strng.endswith('2') and not strng.endswith('1'):
        addition = 'nd'
    elif strng == '13':
        addition = 'th'
    elif strng.endswith('3'):
        addition = 'rd'
    else:
        addition = 'th'
    return addition

if __name__ == '__main__':

    date_store = []
    candidates = '2015-07-01 2015-07-04 \
    2016-12-01 2017-02-03 \
    2015-12-01 2017-02-03 \
    2016-03-01 2016-05-05 \
    2017-01-01 2017-01-01 \
    2022-09-05 2023-09-04'

    # string of candidates  to list
    candidates = list(candidates.split())

    # calculate the present year for comparison
    now = datetime.datetime.now().year

    # extract year, month, and day from each pairs of candidates
    count = 0
    while count < len(candidates):
        for value in candidates:
            year = int(value[0:4])
            month = int(value[5:7])
            day = int(value[8:10])

            z = datetime.date(year, month, day)

            # convert to readable date
            nice_z = date.strftime(z, '%#B, %#d, %Y')

            # split into 'words'
            nice_z = nice_z.split()

            # leading zeros to go
            nice_z[1] = nice_z[1].strip(',')
            nice_z[1] = str(int(nice_z[1]))

            # commas to go
            stripped_nice_z = ''
            for x in nice_z:
                x = x.strip(',')
                stripped_nice_z = stripped_nice_z + x + ' '
            stripped_nice_z = stripped_nice_z.split()

            # add suffix
            add_suffix = suffix(stripped_nice_z[1])

            suffixed_nice_z = stripped_nice_z[0] + ' ' + stripped_nice_z[1] + add_suffix + ' ' + stripped_nice_z[2]

            date_store.append(suffixed_nice_z)
            count += 1

    # extract in pairs and convert to readable year, month, days
    for x in range(0, len(date_store), 2):
        first = date_store[x]
        second = date_store[x+1]
        day = re.findall('\s\w+\s', date_store[x])
        day = day[0]
        month = re.findall('^\w+', date_store[x])
        month = month[0]
        year = re.findall('\w+$', date_store[x])
        year = year[0]
        day2 = re.findall('\s\w+\s', date_store[x+1])
        day2 = day2[0]
        month2 = re.findall('^\w+', date_store[x+1])
        month2 = month2[0]
        year2 = re.findall('\w+$', date_store[x+1])
        year2 = year2[0]

        # print out appropriate format
        if year == str(now) and year2 == str(now):
            print("{0}{5}{1}{2}{3}{5}{4}".format(month, day, '- ', month2, day2, ' '))
        elif first == second:
            print('{0}'.format(first))
        elif year == year2:
            print('{0}{1}{2}{3}'.format(month, day, '- ', second))
        elif year == str(now):
            print('{0}{1}{2}{3}{4}'.format(month, day, '- ',month2, day2))
        else:
            print('{0}{1}{2}'.format(first, '- ', second))


