'''
For today's challenge, you should calculate some simple statistical
values based on a list of values. Given this data set, write
functions that will calculate:

    The mean value
    The variance
    The standard deviation

Obviously, many programming languages and environments have standard
functions for these (this problem is one of the few that is really
easy to solve in Excel!), but you are not allowed to use those!
The point of this problem is to write the functions yourself.

mean: average
variance: how far each value is from the mean
           a: subtract the mean from each value in the data
           b: square each of these distances and add together
           c: divide the sum of the squares by the number of values.
standard deviation:  + square root of the variance
'''
import re
import math

def mean(lst):
    sum_of_list = 0
    for item in lst:
        sum_of_list += float(item)
    mean_of_list = sum_of_list / len(lst)
    return mean_of_list


def variance(num, lst):
    sum_of_squares = 0
    for data in lst:
        diff = (float(data) - num) ** 2
        sum_of_squares += diff
        vari = sum_of_squares/ len(lst)
    return vari


def standard_deviation(num):
    std_dev = math.sqrt(num)
    return std_dev


if __name__ == '__main__':
    file = 'data.txt'
    with open(file) as f:
        data_list = []
        for line in f:
            element = re.findall('\d+\.\d+', line)
            data_list.append(element[0])

    mean_of_data = mean(data_list)
    variance_of_data = variance(mean_of_data, data_list)
    std_deviation = standard_deviation(variance_of_data)
    print('mean: ', mean_of_data, ' variance: ', variance_of_data, ' std deviation: ', std_deviation)
