''' If a right angled triangle has three sides A, B and C (where C is the hypothenuse),
the pythagorean theorem tells us that A**2 + B**2 = C**2

When A, B and C are all integers, we say that they are a pythagorean triple.
For instance, (3, 4, 5) is a pythagorean triple because 3**2 + 4**2 = 5**2 .

When A + B + C is equal to 240, there are four possible pythagorean triples:
(15, 112, 113), (40, 96, 104), (48, 90, 102) and (60, 80, 100).

Write a program that finds all pythagorean triples where A + B + C = 504.

Note: After writing a very slow brute-force program, I found I had
already done the ground-work with Euler problem 9 five years ago!
My modified solution:
'''

import math

def main():
    n = 504
    lst = []
    lst2 = []

    # generate two numbers between 1 and 504
    for a in range (1, n):
        for b in range(1, n):
            # work out the c of a,b,c
            c = math.sqrt(a ** 2 + b ** 2)
            result = a + b + c

            if result == n:
                ans = (a, b, c)
                ans = sorted(ans)
                lst.append(ans)
    # remove duplicates
    for i in lst:
        if i not in lst2:
            lst2.append(i)


    print("result = ", lst2)


if __name__ == "__main__":
    main()