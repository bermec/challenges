''' write an application which will print a triangle of stars of user-specified height,
with each line having twice as many stars as the last. sample output:

@
@@
@@@@

hint: in many languages, the "+" sign concatenates strings.
bonus features: print the triangle in reverse, print the triangle right justified
'''

a = '@'
n = 4
for x in range(1, n):
    a *= x
    print(a.rjust(n - 1, ' '))
    a = '@'

a = '@'
for x in range(1, n):
    b = a * x
    print(b)