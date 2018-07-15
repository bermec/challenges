''' Today we're going to balance words on one of the letters in them. We'll use the position and letter itself
to calculate the weight around the balance point. A word can be balanced if the weight on either side of the
balance point is equal. Not all words can be balanced, but those that can are interesting for this challenge.

The formula to calculate the weight of the word is to look at the letter position in the English alphabet
(so A=1, B=2, C=3 ... Z=26) as the letter weight, then multiply that by the distance from the balance point,
so the first letter away is multiplied by 1, the second away by 2, etc.

As an example:

STEAD balances at T: 1 * S(19) = 1 * E(5) + 2 * A(1) + 3 * D(4))
Input Description

You'll be given a series of English words. Example:

STEAD

Output Description

Your program or function should emit the words split by their
balance point and the weight on either side of the balance point. Example:

S T EAD - 19

This indicates that the T is the balance point and that the
weight on either side is 19.
Challenge Input

CONSUBSTANTIATION
WRONGHEADED
UNINTELLIGIBILITY
SUPERGLUE

Challenge Output

Updated - the weights and answers I had originally were wrong. My apologies.

CONSUBST A NTIATION - 456
WRO N GHEADED - 120
UNINTELL I GIBILITY - 521
SUPERGLUE DOES NOT BALANCE

'''

def balance(candidate):
    indexx = 1
    alphabet =[]
    alphabet = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    temp = []
    while True:

        first_slice = candidate[0:indexx]
        if len(candidate) - len(first_slice) == 1:
            return '{0} DOES NOT BALANCE'.format(candidate)

        # split up the letters of list first_slice
        lst = []
        for letter in first_slice:
            letter = letter.strip()
            lst. append(letter)

        # compute alpha to integer and reverse list for calculation
        #accum = 0
        temp1 =[]
        for y in range(0, len(lst)):
            temp1.append(alphabet.index(lst[y]))
        temp1.reverse()

        # compute the 'weight' of the first slice
        acc2 = 0
        mult = 1
        for n in range(0, len(temp1)):
            acc2 += temp1[n] * mult
            mult += 1

        second_slice = candidate[indexx + 1:]

        # compute alpha to int of second_slice
        for x in range(0, len(second_slice)):
            temp.append(alphabet.index(second_slice[x]))

        # calculate 'weight' of second_slice
        acc = 0
        n = 1
        for y in range(0, len(temp)):
            acc += temp[y] * n
            n += 1

        balance_point = candidate[indexx]

        if acc == acc2:
            return '{0} {1} {2} - {3}'.format(first_slice, balance_point, second_slice, acc)
        else:
            indexx += 1
            temp = []


if __name__ == '__main__':

    ans = balance('WRONGHEADED')
    print(ans)




