''' Write a program that given two strings, finds out if the
second string is contained in the first, and if it is, where it is.

I.e. given the strings "Double, double, toil and trouble" and
"il an" will return 18, because the second substring is
embedded in the first, starting on position 18.

NOTE: Pretty much every language have this functionality
built in for their strings, sometimes called find() (as in
Python) or indexOf() (as in Java). But the point of this
problem is to write the program yourself, so you are not
allowed to use functions like this!

'''
a ="Double, double, toil and trouble"
b = "il an"
len_a = len(a)
len_b = len(b)

for x in range(0, len_a):
    section = a[x:x + len_b]
    if section == b:
        print('Found it: ', section)
        exit()