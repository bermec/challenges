def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for the square root to be computed.

    Returns:
        The square root of x:
    '''

def sqrt(x):
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    import sys
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ZeroDivisionError as e:
        print(e)

    print('Program execution continues normally here.')

if __name__ == '__main__':
    main()