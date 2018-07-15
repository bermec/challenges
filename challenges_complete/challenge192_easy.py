def display(a, p):
    return a.rjust(p, ' ')

# add zeroes to keep the numbers the same length.
def paddOut(a, b):
    if len(a) == len(b):
        return (a, b)
    elif len(a) < len(b):
        a = a.rjust(len(b), '0')
        return (a, b)
    else:
        b = b.rjust(len(a), '0')
        return (a, b)



if __name__ == '__main__':

    carry = 0
    digiString = ''
    digitLst = []
    carryLst = [' ']
    firstNum = '267'
    secondNum = '956'
    paddit = paddOut(firstNum, secondNum)
    firstNum = paddit[0]
    secondNum = paddit[1]
    add = '+'
    dashes = '-' * len(firstNum)

    for x in range(len(firstNum) - 1, -1, -1):

        # pick out the two numbers to be added
        candidate1 = int(firstNum[x])
        candidate2 = int(secondNum[x])
        # do they add up to more than nine?
        if candidate1 + candidate2 >= 10:
            carry = 1

        if x == 0:
            # no carry in first column
            digitLst.append(candidate1 + candidate2 + carry)
            if ((candidate1 + candidate2 + carry) // 10) == 0:
                carryLst.append(' ')
            else:
                carryLst.append((candidate1 + candidate2 + carry) // 10)
        elif x == len(firstNum) - 1:
            # no need for carry on final addition
            digitLst.append((candidate1 + candidate2) % 10)
            if ((candidate1 + candidate2 + carry) // 10) == 0:
                carryLst.append(' ')
            else:
                carryLst.append((candidate1 + candidate2 + carry) // 10)

        else:
            digitLst.append((candidate1 + candidate2 + carry) % 10)
            if ((candidate1 + candidate2 + carry) // 10) == 0:
                carryLst.append(' ')
            else:
                carryLst.append((candidate1 + candidate2 + carry) // 10)

    # pad out for display
    pad = len(firstNum) + 1

    # convert the list into strings
    for x in range(len(digitLst) - 1, -1, -1):
        digiString += str(digitLst[x])

    # ditto
    carryString = ''
    for x in range(len(carryLst)- 1, -1, -1):
        carryString += str(carryLst[x])

    add = add + secondNum
    firstNum = display(firstNum, pad)
    add = display(add, pad)
    dashes = display(dashes, pad)
    digiString = display(digiString, pad)
    carryString = display(carryString, pad)

    print("{0}\n{1}\n{2}\n{3}\n{4}\n{5}".format(firstNum, add, dashes,
                        digiString, dashes, carryString))







