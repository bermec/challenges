while True:
    lst =[x * 0.25 for x in range(-10, 10)]
    for x in lst:
        y = x - 2.0
        print(y,x)
        z = (3.0 * x) * (x + 2.0)
        print(z, x)
        print()
        