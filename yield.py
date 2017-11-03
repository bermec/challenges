lst = '10'

def fib_to_dec(num):
    ''' (str) -> number
    base fibonacci to base 10'''
    output = 0
    f = fibonacci_generator()
    fib = next(f)
    for x in range(len(num) - 1, -1, -1):
        fib = next(f)
        fib_num = num[x]
        if fib_num == str(1):
            output += fib
    return output


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    ans = fib_to_dec(lst)
    print(ans)



