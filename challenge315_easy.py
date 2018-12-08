'''
One way to think about bitwise addition (using the symbol ^)
as binary addition without carrying the extra bits:

   101   5
^ 1001   9
  ----
  1100  12

  5^9=12

So let's define XOR multiplcation (we'll use the symbol @)
in the same way, the addition step doesn't carry:

     1110  14
   @ 1101  13
    -----
     1110
       0
   1110
^ 1110
  ------
  1000110  70

  14@13=70

For this challenge you'll get two non-negative integers as input and
output or print their XOR-product, using both binary and decimal notation.
Input Description

You'll be given two integers per line. Example:

5 9

Output Description

You should emit the equation showing the XOR multiplcation result:

5@9=45

EDIT I had it as 12 earlier, but that was a copy-paste error. Fixed.
Challenge Input

1 2
9 0
6 1
3 3
2 5
7 9
13 11
5 17
14 13
19 1
63 63

Challenge Output

1@2=2
9@0=0
6@1=6
3@3=5
2@5=10
7@9=63
13@11=127
5@17=85
14@13=70
19@1=19
63@63=1365

'''


def bin2dec(n):
    store = 0
    x = 0
    # y = index of n
    for y in range(len(n) - 1, -1, -1):
        m = n[y]
        m = int(m)
        store += m * (2 ** x)
        x += 1
    return  store


def dec2bin(n):
    numstring = ''
    if n % 2 == 0:
        numstring += str(0)
    else:
        numstring += str(1)
    while n > 1:
        n = n // 2

        if n % 2 == 0:
            numstring += str(0)
        else:
            numstring += str(1)
    return numstring[::-1]


def addition(l):
    sum_ones = l.count('1')
    if sum_ones%2 == 1:
        result = '1'
    else:
        result = '0'
    return result


def flatten(n):
    lst = list(''.join(n))
    return lst


if __name__ == '__main__':
    import re

    candidates ='''1 2
    9 0
    6 1
    3 3
    2 5
    7 9
    13 11
    5 17
    14 13
    19 1
    63 63'''

    #candidates = '3 3'
    candidates = candidates.splitlines()
    # extract the numbers and convert to binary
    for nums in candidates:
        mults = re.findall('\d+', nums)
        num_one = int(mults[0])
        num_one = dec2bin(num_one)
        num_two = int(mults[1])
        num_two = dec2bin(num_two)
        # length of the binary number
        len_list_two = len(num_two)

        # do long-hand
        num_two_r = num_two[::-1]
        num = ''
        master_list = []
        lst = []
        for x in range(0, len_list_two):
            if num_two_r[x] == '0':
                lst.append(('0'))
                lst = flatten(lst)
                master_list.append(lst)
                lst = []
            else:
                lst.append(num_one)
                if x > 0:
                    num = '0' * x
                    lst.append(num)
                lst = flatten(lst)
                master_list.append(lst)
                lst = []

        #len_master_list_last = len(master_list[-1])
        # find the columns to add for the result
        n = []
        store = []
        N = len(master_list[-1]) + 1
        for x in range(0, 1):
            for y in range(-1, -N, -1):
                n = []
                for z in range(0, len(master_list)):
                    try:
                        n.append(master_list[x + z][y])
                    except IndexError:
                        n.append(0)
                        continue
                store.append(n)

        # convert store list to binary answer
        result = ''
        for lst in store:
            ans = addition(lst)
            result += str(ans)

        result = result[::-1]
        result = bin2dec(result)

        print('{0}{1}{2}{3}{4}'.format(mults[0], '@', mults[1], '=', result))

