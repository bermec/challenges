'''
Write a program that reads two arguments from the command line:

    a symbol, +, -, *, or /
    a natural number n (≥ 0)

And uses them to output a nice table for the operation
from 0 to n, like this (for "+ 4"):

+  |  0  1  2  3  4
-------------------
0  |  0  1  2  3  4
1  |  1  2  3  4  5
2  |  2  3  4  5  6
3  |  3  4  5  6  7
4  |  4  5  6  7  8

If you want, you can format your output using the reddit table syntax:

|+|0|1
|:|:|:
|**0**|0|1
|**1**|1|2

Becomes this:
+ 	0 	1
0 	0 	1
1 	1 	2
'''

def interpret_operator(op, t, t2, e):
    if op == '-':
        e = t - t2
    elif op == '+':
        e = t + t2
    elif op == '/':
        e = t / t2
    else:
        op == '*'
        e = t * t2
    return e



def table(a, n):
    num = list(range(1, n))
    target = list(range(1, n))
    top_string = a + ' |'
    body = ''
    exp = 0
    for x in num:
        top_string += str(x).rjust(6)
    print(top_string)
    print('-' * len(top_string))

    for x in range(0, len(target)):
        body = str(target[x]) + ' |'
        for y in range(0, len(num)):
            temp = target[x]
            temp2 = num[y]

            exp = interpret_operator(a, temp, temp2, exp)
            exp = round(exp, 2)

            body += str(exp).rjust(6)
        print(body)


if __name__ == '__main__':
    ans = table('/', 6)


