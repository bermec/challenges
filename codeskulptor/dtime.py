'''
strng = `2017-12-01 2017-12-27
2016-01-01 2016-01-28
2016-05-01 2016-08-27
2016-01-01 2018-12-27
2015-08-01 2019-08-27
2016-01-01 2017-12-27`;
'''
import re
from datetime import datetime as dt


constant_dates = '2015-08-01 2019-08-27'

dates = re.findall('\d+\-\d+\-\d+', constant_dates)
print(dates)

dates_ordinal = []
for x in range(0, len(dates)):
    d = dt.strptime(dates[x], '%Y-%m-$d').date()
    d = d.toordinal()
    dates_ordinal.append(d)
print(dates_ordinal)