'''
Write a function step_count(a, b, steps) that returns a list or
array containing steps elements, counting from a to b in steps
of an equal size. steps is a positive integer greater than or
equal to 2, a and b are floating point numbers.

For example:

step_count(18.75, -22.00, 5)
==> [18.75, 8.5625, -1.625, -11.8125, -22.0]

step_count(-5.75, 12.00, 5)
==> [-5.75, -1.3125, 3.125, 7.5625, 12.0]

step_count(13.50, -20.75, 3)
==> [13.5, -3.625, -20.75]

step_count(9.75, 3.00, 9)
==> [9.75, 8.90625, 8.0625, 7.21875, 6.375, 5.53125, 4.6875, 3.84375, 3.0]


'''
import re

def step_count(x, y, z):
    result = []
    # total to be calculated
    total_count = x - y
    step = total_count / z
    if x > y:
        while x >= y:
            result.append(x)
            x = x - step
    else:
        while x <= y:
            result.append(x)
            x = x - step
    return result


if __name__ == '__main__':

    values = '''step_count(18.75, -22.00, 5)
==> [18.75, 8.5625, -1.625, -11.8125, -22.0]

step_count(-5.75, 12.00, 5)
==> [-5.75, -1.3125, 3.125, 7.5625, 12.0]

step_count(13.50, -20.75, 3)
==> [13.5, -3.625, -20.75]

step_count(9.75, 3.00, 9)
==> [9.75, 8.90625, 8.0625, 7.21875, 6.375, 5.53125, 4.6875, 3.84375, 3.0]
'''
    value_list = values.split('\n')
    for line in value_list:
        if line.startswith('step'):
            info = re.findall('([-]\d*\.\d*|\d*\.\d*|\d)', line)

            a = float(info[0])
            b = float(info[1])
            c = float(info[2])

            ans = step_count(a, b, c - 1)
            print(ans)
