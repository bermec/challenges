'''
A fraction exists of a numerator (top part) and a denominator (bottom part) as you probably all know.

Simplifying (or reducing) fractions means to make the fraction as simple as possible. Meaning that
the denominator is a close to 1 as possible. This can be done by dividing the numerator and
denominator by their greatest common divisor.
Formal Inputs & Outputs
Input description

You will be given a list with 2 numbers seperator by a space. The first is the numerator, the second
the denominator

4 8
1536 78360
51478 5536
46410 119340
7673 4729
4096 1024

Output description

The most simplified numbers

1 2
64 3265
25739 2768
7 18
7673 4729
4 1

Notes/Hints

Most languages have by default this kind of functionality, but if you want to challenge yourself,
you should go back to the basic theory and implement it yourself.
Bonus

Instead of using numbers, we could also use letters.

For instance

ab   a
__ = _
cb   c

And if you know that x = cb, then you would have this:

ab   a
__ = _
x    c

and ofcourse:

a    1
__ = _
a    1

aa   a
__ = _
a    1

The input will be first a number saying how many equations there are. And after the equations,
you have the fractions.

The equations are a letter and a value seperated by a space. An equation can have another
equation in it.

3
x cb
y ab
z xa
ab cb
ab x
x y
z y
z xay

output:

a c
a c
c a
c 1
1 ab

'''
r

def gcd(a, b):
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        d += 1
    while a != b:
        if a % 2 == 0:
            a /= 2
        elif b% 2 == 0:
            b /= 2
        elif a > b:
            a = (a - b) / 2
        else:
            b = (b - a) / 2
    g = a
    gcd = g * (2 ** d)
    return gcd


def simplify(a, b):
    ''' divide num = denom by gcd'''
    gcf = gcd(a, b)
    num = a / gcf
    denom = b / gcf
    return (num, denom)


if __name__ == '__main__':

    candidates = '''4 8
    1536 78360
    51478 5536
    46410 119340
    7673 4729
    4096 1024'''
    candidates = candidates.splitlines()

    for candidate in candidates:
        candidate= candidate.split()
        numerator = int(candidate[0])
        denominator = int(candidate[1])

        gcf = simplify(numerator, denominator)
        print(int(gcf[0]), int(gcf[1]))