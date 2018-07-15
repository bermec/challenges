'''
The Thue-Morse sequence is a binary sequence (of 0s and 1s) that never repeats. It is obtained by starting with 0
 and successively calculating the Boolean complement of the sequence so far.
 It turns out that doing this yields an infinite, non-repeating sequence. This procedure yields
 0 then 01, 0110, 01101001, 0110100110010110, and so on.

Thue-Morse Wikipedia Article for more information.
Input:

Nothing.
Output:

Output the 0 to 6th order Thue-Morse Sequences.
Example:

nth     Sequence
===========================================================================
0       0
1       01
2       0110
3       01101001
4       0110100110010110
5       01101001100101101001011001101001
6       0110100110010110100101100110100110010110011010010110100110010110

Extra Challenge:

Be able to output any nth order sequence. Display the Thue-Morse Sequences for 100.

Note: Due to the size of the sequence it seems people are crashing beyond 25th order
or the time it takes is very long. So how long until you crash. Experiment with it.
'''


def thue_gen(lst):
    out_list = lst
    for x in range(0, len(lst)):
        if lst[x] == '0':
            out_list += '1'
        else:
            out_list += '0'
    return out_list

if __name__ == '__main__':

    thue = '0'
    holding_list = [thue]
    num = 0
    while num < 6:
        ans = thue_gen(thue)
        num += 1
        thue = ans
        holding_list.append(thue)



    width = len(holding_list[-1])

    print('{0:<10}{1:<10}'.format('nth', 'Sequence'))
    print('='*(width + 10))
    for x in range(0, 7):
        print('{0:<10}{1:<10}'.format(x, holding_list[x]))

