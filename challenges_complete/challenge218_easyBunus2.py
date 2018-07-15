'''
Bonus 2: See which numbers don't get palindromic in under 10000 steps.
Numbers that never converge are called Lychrel numbers.
Quote:

"Interestingly 89 takes an unusually long time to palindrome. The 24 steps (rendered above),
is the largest number of steps (of non-Lyrchel numbers) less than 10,000."

from http://datagenetics.com/blog/october12015/index.html.

Discovered this after spending fruitless hours trying to beat the
recursion stack limit, well above my pay grade :)
'''
lst = []
def ispal(n):
    n = str(n)
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
            return lst
        else:
            n = summed
            acc += 1
            if acc >= 25:
                lst.append(m)
                return lst
            continue
    return lst

if __name__ == '__main__':
    for x in range(1, 10001):
        ans = ispal(x)
    print('Lychrel numbers below 10000:  ',len(ans))
































































































































