def get_Factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return  factors

def getFactorSum(factorLst):
    factorSum = 0
    for factor in factorLst:
        factorSum += factor
    return factorSum

def deficient(n, factorSum):
    return factorSum < 2 * n

def abundant(n, factorSum):
    return factorSum > 2 * n

if __name__ == '__main__':
    n = input('Enter a number:\n')
    n = int(n)
    factorLst = get_Factors(n)
    factorSum = getFactorSum(factorLst)
    if deficient(n, factorSum):
        print(str(n) + ' deficient')
    elif abundant(n, factorSum):
        print(str(n) + ' abundant by ' + str(factorSum - 2 * n))
    else:
        print(str(n) + ' ~~neither~~ deficient')