__author__ = 'rog'
'''
Standard deviation is one of the most basic measurments in statistics.
For some collection of values (known as a "population" in statistics),
it measures how dispersed those values are. If the standard deviation is high,
 it means that the values in the population are very spread out; if it's low,
 it means that the values are tightly clustered around the mean value.

For today's challenge, you will get a list of numbers as input which will serve
as your statistical population, and you are then going to calculate the standard
deviation of that population. There are statistical packages for many programming
languages that can do this for you, but you are highly encouraged not to use them:
the spirit of today's challenge is to implement the standard deviation function yourself.

The following steps describe how to calculate standard deviation for a
collection of numbers. For this example, we will use the following values:

5 6 11 13 19 20 25 26 28 37

    First, calculate the average (or mean) of all your values, which is defined
    as the sum of all the values divided by the total number of values in the population.
    For our example, the sum of the values is 190 and since there are 10 different values,
    the mean value is 190/10 = 19

    Next, for each value in the population, calculate the difference between it and the
    mean value, and square that difference. So, in our example, the first value is 5 and
    the mean 19, so you calculate (5 - 19)2 which is equal to 196. For the second value
    (which is 6), you calculate (6 - 19)2 which is equal to 169, and so on.

    Calculate the sum of all the values from the previous step. For our example, it will be
    equal to 196 + 169 + 64 + ... = 956.

    Divide that sum by the number of values in your population. The result is known as the
     variance of the population, and is equal to the square of the standard deviation. For
     our example, the number of values in the population is 10, so the variance is equal to 956/10 = 95.6.

    Finally, to get standard deviation, take the square root of the variance. For our example,
    sqrt(95.6) ≈ 9.7775.

'''
# S.D. is the square root of the Variance
# Variance is the average of the squared differences from the Mean.
# The Mean is simply the average of the numbers.


def clean_up(lst):
    ''' str -> lst
    convert string to list of integers
    '''
    temp_list = []
    lst = lst.split()
    for x in lst:
        temp_list.append(int(x))
    lst = temp_list
    return lst


def mean(lst):
    ''' list -> number
    compute the mean value of a list of integers
    '''
    acc = 0
    for item in lst:
        acc += item
    the_mean = acc / len(lst)
    return the_mean


def difference(lst):
    ''' list -> float
    compute the squared difference
    '''
    acc = 0
    mean_calc = mean(lst)
    for x in lst:
        acc += (float(x) - mean_calc) ** 2
    return  acc


def variance(strng):
    '''str -> float
    find the standard deviation of a
    string of number
    '''
    lst = clean_up(strng)
    var = (difference(lst) / len(lst)) ** 0.5
    return var


if __name__ == '__main__':
    strng = '5 6 11 13 19 20 25 26 28 37'
    ans = variance(strng)
    print('Input1:', round(ans, 4))

    strng = '37 81 86 91 97 108 109 112 112 114 115 117 121 123 141'
    ans = variance(strng)
    print('Input2: ', round(ans, 4))

    strng = '266 344 375 399 409 433 436 440 449 476 502 504 530 584 587'
    ans = variance(strng)
    print('Challenge1: ', round(ans, 4))

    strng = '809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373'
    ans = variance(strng)
    print('Challenge2: ', round(ans, 4))

