import re
from datetime import datetime as dt


def ordinal(ordinal_dates):
    '''iso8601 to ordinal'''
    dates_ordinal = []
    dates_orig = []
    for x in range(0, len(ordinal_dates)):
        d = dt.strptime(ordinal_dates[x], '%Y-%m-%d')
        print("d: " + str(d))
        dates_ordinal.append(d.timestamp())
        dates_orig.append(d)
    print("dates_ordinal: " + str(dates_ordinal))
    period = dates_ordinal[1] - dates_ordinal[0]
    return period, dates_ordinal[0], dates_ordinal[1], dates_orig


if __name__ == '__main__':
    strng = '''2017-12-01 2017-12-27
        2016-01-01 2016-01-28
        2016-05-01 2016-08-27
        2016-01-01 2018-12-27
        2016-01-01 2017-12-27
        2015-08-01 2019-08-27'''

    constant_dates = '2015-08-01 2019-08-27'
    # extract dates
    dates = re.findall('\d+\-\d+\-\d+', constant_dates)
    # dates of first project to use as constants
    constant_period = ordinal(dates)[0]
    print('constant: ', constant_period)
    constant_start_date = ordinal(dates)[1]
    constant_end_date = ordinal(dates)[2]
    print('constant_start_date: ', constant_start_date)

    epoch_list = []
    project_start_date_list = []

    for line in strng.splitlines():
        line = line.strip()
        dates = re.findall('\d+\-\d+\-\d+', line)
        print("regex dates:" + str(dates))
        epoch_list.append(ordinal(dates))
        project_start_date_list.append(ordinal(dates)[1])
    percent_list = []
    for data in epoch_list:
        percent_start = int(((data[1] - constant_start_date) / constant_period) * 100)
        percent_end = int(((data[2] - constant_start_date) / constant_period) * 100)
        percent_list.append((percent_start, percent_end))
    print('percent_list_end_dates: ', percent_list)

    print(epoch_list)
    print(project_start_date_list)
