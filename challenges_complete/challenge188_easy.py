'''
iso 8601 standard for dates tells us the proper way to do an extended day
is yyyy-mm-dd

    yyyy = year
    mm = month
    dd = day

A company's database has become polluted with mixed date formats. They
could be one of 6 different formats

    yyyy-mm-dd
    mm/dd/yy
    mm#yy#dd
    dd*mm*yyyy
    (month word) dd, yy
    (month word) dd, yyyy

(month word) can be: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec

Note if is yyyy it is a full 4 digit year. If it is yy then it is only the
last 2 digits of the year. Years only go between 1950-2049.
Input:

You will be given 1000 dates to correct.
Output:

You must output the dates to the proper iso 8601 standard of yyyy-mm-dd
Challenge Input:

https://gist.github.com/coderd00d/a88d4d2da014203898af
Posting Solutions:

Please do not post your 1000 dates converted. If you must use a gist or
link to another site. Or just show a sampling
'''

def monthToNum(s):

    return{
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9,
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
    }[s]


candidates = '''06#72#03
Dec 26, 75
Jul 13, 07
Nov 21, 14
15*10*1981
13*02*1992
10#51#16
1964-01-10
06*04*1965
01#07#27
02*03*1999
01/11/55
12#16#08
Oct 25, 58
May 17, 08
Mar 21, 1980
07#71#24
11/15/78
1996-10-24
07*11*1953
1970-03-13
Jul 27, 1999
01#95#04
05#78#26
04/22/44
17*07*1979
07#72#15
02/25/08
11/20/12
1985-12-04
28*12*1987'''

reqired_output = 'yyyy-mm-dd'
import re

candidates = candidates.splitlines()
for line in candidates:
    extract = re.findall('\w+', line)
    if '#' in line:
        year = '19' + extract[1]
        month = extract[2]
        day = extract[0]
    elif '/' in line:
        year = '19' + extract[2]
        month = extract[0]
        day = extract[1]
    elif '*' in line:
        year = extract[2]
        month = extract[1]
        day = extract[0]
    elif extract[0].isalpha():
        if len(extract[2]) == 2:
            year = '19' + extract[2]
        else:
            year = extract[2]
        month = monthToNum(extract[0])
        day = extract[1]
    else:
        year = extract[0]
        month = extract[1]
        day = extract[2]

    print(year, month, day)

