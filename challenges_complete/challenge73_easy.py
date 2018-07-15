''' During the 70s and 80s, some handheld calculators used a very different notation
for arithmetic called Reverse Polish notation (RPN). Instead of putting operators
(+, *, -, etc.) between their operands (as in 3 + 4), they were placed behind them:
to calculate 3 + 4, you first inputted the operands (3 4) and then added them together by pressing +.

Internally, this was implemented using a stack: whenever you enter a number, it's pushed onto the stack,
and whenever you enter an operator, the top two elements are popped off for the calculation.
Here's an example of a RPN calculator calculating 3 4 * 6 2 - +:

[3] --> 3
[4] --> 3 4
[*] --> 12      ( 3 * 4 = 12)
[6] --> 12 6
[2] --> 12 6 2
[-] --> 12 4    ( 6 - 2 =  4)
[+] --> 16      (12 + 4 = 16)

Your task is to implement a program that reads a string in Reverse Polish notation and prints the
result of the calculation. Your program should support positive and negative integers and the
operators +, -, *. (For extra credit, you can implement extra functions, such as decimal numbers,
division, exponentiation, etc.)
'''


def minus(lst):
    total = lst[-2]
    total -= lst[-1]
    return total


def plus(lst):
    global stack
    total = lst[-2]
    total += lst[-1]
    return total


def div(lst):
    total = lst[-2]
    total /= lst[-1]
    return total


def multi(lst):
    total = lst[-2]
    total *= lst[-1]
    return total


def power_of(lst):
    total = lst[0]
    for x in range(1, len(lst)):
        total **= lst[x]
    return total


if __name__ == '__main__':

    quay_press = ''
    stack = []
    temp = []

    operators = ['-', '*', '/', '+', '**']


    while quay_press != 'q':
        quay_press = input('Input expression - "q" to quit...')

        if quay_press in operators:
            temp = []
            for x in range(0, 2):
                b = stack.pop()
                temp.insert(0, b)
            if quay_press == '-':
                ans = minus(temp)
                stack.append(ans)
                print(stack)
            elif quay_press == '+':
                ans = plus(temp)
                stack.append(ans)
                print(stack)
            elif quay_press == '*':
                ans = multi(temp)
                stack.append(ans)
                print(stack)
            elif quay_press == '**':
                ans = power_of(temp)
                stack.append(ans)
                print(stack)
            else:
                quay_press == '/'
                ans = div(temp)
                stack.append(ans)
                print(stack)
        elif quay_press== 'q':
            print(ans)
            exit()
        elif quay_press == str(float(quay_press)):
            stack.append(float(quay_press))
            print(stack)
        elif quay_press == str(int(quay_press)):
            stack.append(int(quay_press))
            print(stack)
        else:
            print('Wrong input!')

