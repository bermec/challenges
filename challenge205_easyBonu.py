'''
Of course, not all users will want to read a Month Day, Year format. To fix this, allow your
program to receive hints on how to format the dates, by accepting a date format as a third parameter, for example:

    2015-07-01 2015-07-04 DMY
    2016-03-01 2016-05-05 YDM
    2022-09-05 2023-09-04 YMD

would produce:

    1st - 4th July
    2016, 1st March - 5th May
    2022, September 5th - 2023, September 4th

You only need to handle date format strings DMY, MDY, YMD and YDM.

'''

import re
import datetime
from datetime import date

date_format = []
date_store = []


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


def dmy(a, b, c, d, e, f, g, h, i):
    # print out appropriate format

    if (c == str(i) and f == str(i)) and (b == e):
        print("{0}{1}{2}{3}{4}".format(a, '-', d, e, ' '))
    elif c == str(i) and f == str(i):
        print("{0}{1}{2}{3}{4}".format(a, '-', d, e, ' '))
    elif g == h:
        print('{0}{1}{2)'.format(a, b, c))
    elif c == f and b == e:
        print('{0}{4}{3}{5}{1}{5}{2}'.format(a, b, c, d, '-', ' '))
    elif c == f:
        print('{0}{6}{1}{2}{5}{3}{4}'.format(c, a, b, d, e, ' -', ','))
    elif c == str(i):
        print('{0}{1}{2}{3}{4}'.format(a, b, ' - ', d, e))
    else:
        print('{0}{8}{1}{2}{3}{7}{4}{8}{1}{5}{6}'.format(c, ' ', b, a, f, e, d, '- ', ','))



def ydm(a, b, c, d, e, f, g, h, i):
    # print out appropriate format
    if c == str(i) and f == str(i):
        print("{0}{1}{2}{3}{4}".format(a, '-', d, e, ' '))
    elif g == h and b == e:
        print('{0}{5}{a}{4}{2}{3}'.format(c, a, d, b, ' - ', ','))
    elif g == h:
        print('{0}{1}{2)'.format(a, b, c))
    elif c == f and b == e:
        print('{2}{5}{0}{4}{1}3{5}{1}'.format(a, b, c, d, '-', ' ', ''))
    elif c == f:
        print('{0}{6}{1}{2}{5}{3}{4}'.format(c, a, b, d, e, ' -', ','))
    elif c == str(i):
        print('{0}{1}{2}{3}{4}'.format(a, b, '- ', d, f))
    else:
        print('{0}{8}{1}{2}{3}{7}{4}{8}{1}{5}{6}'.format(c, ' ', b, a, f, e, d, '- ', ','))


def ymd(a, b, c, d, e, f, g, h, i):
    # print out appropriate format
    if c == str(i) and f == str(i):
        print("{0}{1}{2}{3}{4}".format(a, '-', d, e, ' '))
    elif g == h and b == e:
        print('{0}{5}{a}{4}{2}{3}'.format(c, a, d, b, ' - ', ','))
    elif g == h:
        print('{0}{1}{2)'.format(a, b, c))
    elif c == f and b == e:
        print('{2}{6}{5}{1}{0}{4}{3}'.format(a, b, c, d, '-', ' '))
    elif c == f:
        print('{0}{6}{1}{2}{5}{3}{4}'.format(c, a, b, d, e, ' -', ','))
    elif c == str(i):
        print('{0}{1}{2}{3}{4}'.format(b, a, '- ', e, d))
    else:
        print('{0}{8}{1}{2}{3}{7}{4}{8}{1}{5}{6}'.format(c, ' ', b, a, f, e, d, '- ', ','))



if __name__ == '__main__':


    candidates = """2015-07-01 2015-07-04 DMY
        2016-03-01 2016-05-05 YDM
        2022-09-05 2023-09-04 YMD"""

    # extract print format codes
    codes = re.findall('(YDM|YMD|DMY)', candidates)


    # string of candidates  to list
    candidates = list(candidates.split())

    # calculate this year for comparison
    now = datetime.datetime.now().year

    # extract year, month, and day from each pairs of candidates
    count = 0
    while count < len(candidates) - 3:
        for value in candidates:
            if value.isalpha():
                date_format.append(value)
                continue
            value = re.findall('\d+', value)
            year = int(value[0])
            month = int(value[1])
            day = int(value[2])

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
            count += 1

            # place in date_store list
            date_store.append(suffixed_nice_z)
            count += 1


    # extract in pairs from date_store and convert to readable year, month, days
    y = 0
    for x in range(0, len(date_store), 2):
        first = date_store[x]
        second = date_store[x + 1]
        day = re.findall('\s\w+\s', date_store[x])
        day = day[0]
        month = re.findall('^\w+', date_store[x])
        month = month[0]
        year = re.findall('\w+$', date_store[x])
        year = year[0]
        day2 = re.findall('\s\w+\s', date_store[x + 1])
        day2 = day2[0]
        month2 = re.findall('^\w+', date_store[x + 1])
        month2 = month2[0]
        year2 = re.findall('\w+$', date_store[x + 1])
        year2 = year2[0]
        if codes[y] == 'DMY':
            dmy(day, month, year, day2, month2, year2, first, second, now)
        elif codes[y] == 'YDM':
            ydm(day, month, year, day2, month2, year2, first, second, now)
        else:
            ymd(day, month, year, day2, month2, year2, first, second, now)
        y += 1
