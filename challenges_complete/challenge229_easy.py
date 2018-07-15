''' Write a program to calculate the Dottie number.
This is the number you get when you type any number into a
scientific calculator and then repeatedly press the cos button,
with the calculator set to radians. The number displayed updates,
getting closer and closer to a certain number,
and eventually stops changing.

cos here is the trigonometric function cosine,
but you don't need to know any trigonometry, or what
cosine means, for this challenge. Just do the same thing
you would with a handheld calculator: take cosine over
and over again until you get the answer
'''
import math

def dottie(n):
    temp = 0
    while True:
        n = (math.cos(n))
        if n == temp:
            return n
        temp = n

if __name__ == '__main__':
    ans = dottie(100)
    print('Dottie number: ',ans)