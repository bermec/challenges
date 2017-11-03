'''
    The Dottie number is what's known as the fixed point of the
    function f(x) = cos(x). Find the fixed point of the
    function f(x) = x - tan(x), with a starting value of x = 2.
    Do you recognize this number?
    Find a fixed point of f(x) = 1 + 1/x (you may need to try more
    than one starting number). Do you recognize this number?
    What happens when you try to find the fixed point of
    f(x) = 4x(1-x), known as the logistic map, with most
    starting values between 0 and 1?

'''

import math

def tangent(value):
    temp = 0
    while True:
        temp = value - math.tan(value)
        if  temp == value:
            return temp
        value = temp

def oneOverX(value):
    temp = 0
    while True:
        temp = 1 + (1 / value)
        if  temp == value:
            return temp
        value = temp

def logistic(value):
    temp = 0
    lst = []
    a = 0.05
    for value in range(0, 100, 5):
        value = value/100
        temp = (4 * value) * (1 - value)
        lst.append(temp)
    return lst



if __name__ == '__main__':
    ans = tangent(2)
    print('pi: ',ans)
    ans = oneOverX(2)
    print('golden ratio: ',ans)
    ans = logistic(0.6)
    print('logistic numbers:')
    for x in ans:
        print('{0:10.2f}'.format(x))

