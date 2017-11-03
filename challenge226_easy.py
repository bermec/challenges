''' For today's challenge, you will get a list of fractions
which you will add together and produce the resulting fraction,
reduced as far as possible.
'''

def factors(n):
    ''' int -> list
    Return a list of factors of n
    '''
    lst = []
    for x in range(1, n):
        if n % x == 0:
            lst.append(x)
    return lst

def reduce_fraction(n, n2):
    ''' number -> tuple
    Return a fraction reduced
    to its factors '''
    temp = 0
    temp2 = 0

    master_lst = []
    master_lst2 = []
    lst1 = (factors(n))
    lst2 = (factors(n2))
    master_lst.extend(lst1)
    master_lst.extend(lst2)

    for items in master_lst:
        if items not in master_lst2:
            master_lst2.append(items)

    for x in range(0, len(master_lst2)):
        num = master_lst2[x]
        if n % num == 0 and n2 % num == 0:
            div = n / master_lst2[x]
            div2 = n2 / master_lst2[x]

            temp = div
            temp2 = div2

    return (int(div), int(div2))

if __name__ == '__main__':
    amount = input('How many fractions?  ')
    amount = int(amount)
    lst = []
    n = 0
    while n != amount:
        fraction = (input('Enter fraction in the form "a/b"  '))
        lst.append(fraction)
        n += 1

    product = 1
    denominator = 1

    for fract in lst:
        seperator = fract.index('/')

        # product of denominators
        denominator = int(fract[seperator + 1:])
        # multiply and add denominator to product
        product *= denominator


    mult = 0
    temp = 0

    for y in lst:
        # seperator, index of forward slash
        seperator = y.index('/')
        numerator = y[:seperator]
        denominator = int(y[seperator + 1:])
        numerator = int(numerator)
        mult += int((product / denominator) * numerator)
        ans = reduce_fraction(product, mult)

    print('Answer = {0}/{1}'.format(ans[1], ans[0]))






























