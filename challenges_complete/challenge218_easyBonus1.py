'''
Bonus: see which input numbers, through 1000, yield identical palindromes.

'''

def ispal(n):
    n = str(n)
    # a copy for output
    m = n
    acc = 1
    while True:
        n = str(n)
        # reverse the string
        reversed_n = str(n[::-1])
        # convert to integer and add
        summed = int(n) + int(reversed_n)
        summed = str(summed)
        # are they a palindrome?'
        if summed == summed[::-1]:
            return (summed, m)
        else:
            n = summed
            acc += 1
            if acc >= 25:
                return None
            continue


if __name__ == '__main__':
    dikt = {}
    output = []
    for x in range(1, 1001):
        # output a tuple of (resulting palindrome, candidate)
        ans = ispal(x)
        # this ans would not converge
        if ans == None:
            continue
        # check if palindrome is in dictionary
        if ans[0] in dikt:
            # if so, add the two keys (candidates) to a list
            output.append((ans[1], dikt.get(ans[0])))
        else:
            # else add to dictionary
            dikt[ans[0]] = ans[1]

    print('output: ', output)

