''' The array duplicates problem is when one integer is in an array for more than once.

If you are given an array with integers between 1 and 1,000,000 or in some other interval
and one integer is in the array twice. How can you determine which one?

Your task is to write code to solve the challenge.

Note: try to find the most efficient way to solve this challenge.

'''

import time

def lst_split(lst):
    front = lst[:len(lst) // 2]
    back = lst[len(lst) // 2:]
    return (front, back)

def sett(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return (set1, set2)

if __name__ == '__main__':
    split = []
    # set up the list
    array = [50]
    for x in range(1, 20000):
        array.append(x)
    array = sorted(array)
    # ------------------------------
    split = array

    t0 = time.time()

    while len(split) > 500:

        # split the list in two
        ans = lst_split(array)
        #print('split lst: ', ans)

        # create a pair of sets for comparison
        set_chk = sett(ans[0], ans[1])
        #print('the sets: ', set_chk)
        set0 = set_chk[0]
        set1 = set_chk[1]

        # compare set lengths with the split lis#t
        if len(ans[0]) > len(set0):
            split = ans[0]
        else:
            split = ans[1]
            len_split = len(ans[1])
        #print('the longest split list: ', len(split))
        array = split


    for x in range(0, len(array) - 1):
        for y in range(x + 1, len(array)):
            a = array[x]
            b = array[y]
            if a == b:
                print('Duplicate found: ', b)

    t1 = time.time()
    print(t1 - t0)
    exit()
            


