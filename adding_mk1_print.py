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
    carryCheck = False
    carry = 0
    digitLst = []
    carryLst = [' ']
    firstNum = '267'
    secondNum = '56'
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
# good so far

        if x == 0:
            digitLst.append(candidate1 + candidate2 + carry)
            if ((candidate1 + candidate2 + carry) // 10) == 0:
                carryLst.append(' ')
            else:
                carryLst.append((candidate1 + candidate2 + carry) // 10)
        elif x == len(firstNum) - 1:
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


pad = len(firstNum) + 1
print(firstNum.rjust(pad, ' '))
print(add + secondNum)
print(dashes.rjust(pad, ' '))
digiString = ''
for x in range(len(digitLst)- 1, -1, -1):
    digiString += str(digitLst[x])
print(digiString.rjust(pad, ' '))
print(dashes.rjust(pad, ' '))

carryString = ''
for x in range(len(carryLst)- 1, -1, -1):
    carryString += str(carryLst[x])
print(carryString.rjust(pad, ' '))
# 192









