''' Write a program that will take a number and print a right triangle
 attempting to use all numbers from 1 to that number.

Sample Run:

Enter number: 10

Output:

7 8 9 10

4 5 6

2 3

1

Enter number: 6

Output:

4 5 6

2 3

1

'''

def gen():
    n = 0
    while n < 100000000:
        n += 1
        numb = n * (n + 1) / 2
        yield int(numb)


if __name__ == '__main__':

    num = input('Enter a number:  ')
    lst = []
    for x in range(1, int(num) + 1):
        lst.append(x)

    g = gen()
    lst_out = []
    firstindice = 0
    secondindice = next(g)

    while secondindice <= len(lst):
        listinlist = lst[firstindice:secondindice]
        lst_out.append(listinlist)
        firstindice = secondindice
        secondindice = next(g)
    lst_out = lst_out[::-1]

    for array in lst_out:
        s = (', '.join(str(i) for i in array))
        s = s.replace(',', '')
        print(s)

