''' Write a program that given a floating point number,
gives the number of American dollar coins and bills needed
to represent that number (rounded to the nearest 1/100, i.e.
the nearest penny). For instance, if the float is 12.33, the
result would be 1 ten-dollar bill, 2 one-dollar bills,
1 quarter, 1 nickel and 3 pennies.

For the purposes of this problem, these are the different
denominations of the currency and their values:

    Penny: 1 cent
    Nickel: 5 cent
    Dime: 10 cent
    Quarter: 25 cent
    One-dollar bill
    Five-dollar bill
    Ten-dollar bill
    Fifty-dollar bill
    Hundred-dollar bill

Sorry Thomas Jefferson, JFK and Sacagawea, but no two-dollar bills, half-dollars or dollar coins!

Your program can return the result in whatever format it wants,
but I recommend just returning a list giving the number each coin or bill
needed to make up the change. So, for instance, 12.33 could return [0,0,1,0,2,1,0,1,3]'''

import collections

def currency(n):
    dollar_string = ''
    n *= 100
    num = 0
    dict = collections.OrderedDict([(10000, 'hundred_dollar_bills'), (5000, 'fifty_dollar_bills'),
                                    (1000, 'ten_dollar_bills'), (500, 'five_dollar_bills'),
                                    (100, 'one_dollar_bills'), (25, 'quarters'), (10, 'dimes'),
                                    (1, 'cents')])
    for k, v in dict.items():
        num = n // k
        num = str(int(num))
        dollar_string += num + ' '  + v + '\n'
        n -= int(num) * k

    return dollar_string

if __name__ == '__main__':

    ans = currency(76.97)
    print(ans)

