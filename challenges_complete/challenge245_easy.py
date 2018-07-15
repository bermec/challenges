'''
Yesterday, Devon the developer made an awesome webform, which the sales
team would use to record the results from today's big new marketing campaign,
but now he realised he forgot to add a validator to the "delivery_date" field!
He proceeds to open the generated spreadsheet but, as he expected, the dates
are all but normalized... Some of them use M D Y and others Y M D, and even
arbitrary separators are used! Can you help him parse all the messy text into
properly ISO 8601 (YYYY-MM-DD) formatted dates before beer o'clock?

Assume only dates starting with 4 digits use Y M D, and others use M D Y.
Sample Input

2/13/15
1-31-10
5 10 2015
2012 3 17
2001-01-01
2008/01/07

Sample Output

2015-02-13
2010-01-31
2015-05-10
2012-03-17
2001-01-01
2008-01-07

'''


import re
import datetime
from datetime import date

if __name__ == '__main__':

    candidates = """2/13/15
    1-31-10
    5 10 2015
    2012 3 17
    2001-01-01
    2008/01/07"""

    print(len(candidates))
    candidates = list(candidates.split('\n'))

    for x in range(0, len(candidates)):
        dates = []
        test = re.findall('\d+', candidates[x])
        # complete year string where required
        if len(test[2]) == 2 and len(test[0]) != 4:
            test[2] = '20' + test[2]
            # year to front
            test.reverse()
            test[1], test[2] = test[2], test[1]
            dates.append(test)
            # year to front of remainder
        elif len(test[2]) == 4:
            test.reverse()
            test[1], test[2] = test[2], test[1]
            dates.append(test)
        else:
            dates.append(test)

        for date in dates:
            print('{0}{3}{1}{3}{2}'.format(date[0], date[1].zfill(2), date[2], '-'))