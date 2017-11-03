def paddOut(a, b):
    if len(a) == len(b):
        return
    elif len(a) < len(b):
        return a.rjust(len(b), '0')

    else:
        b = b.rjust(len(a), '0')
        return (a, b)



if __name__ == '__main__':
    carryCheck = False
    carry = 0
    digitLst = []
    carryLst = []
    firstNum = '551'
    secondNum = '77'
    paddit = paddOut(firstNum, secondNum)
    firstNum = paddit[0]
    secondNum = paddit[1]
    add = '+'
    dashes = '-' * len(firstNum)

    for x in range(len(firstNum) - 1, -1, -1):
        # is there a carry?
        carryCheck = False
        # pick out the two numbers to be added
        candidate1 = int(firstNum[x])
        candidate2 = int(secondNum[x])
        # do they add up to more than nine?
        if candidate1 + candidate2 >= 10:
            carryCheck = True
# good so far
        # on first run digitLst is empty
        xchk = len(digitLst) - 1
        if (carryCheck == True) and (digitLst == []):
            carry = 0
        else:
            carry = 1
        if x == 0:
            digitLst.append(candidate1 + candidate2)
        else:
            digitLst.append((candidate1 + candidate2 + carry) % 10)
            if ((candidate1 + candidate2 + carry) // 10) == 0:
                carryLst.append(' ')
            else:
                carryLst.append((candidate1 + candidate2 + carry) // 10)
        carryCheck = False
        xchk = 0
print(' ', firstNum)
print(add, secondNum)
print(' ', dashes)
print(' ', end='')
for x in range(len(digitLst)- 1, -1, -1):
    print(digitLst[x], end='')
print(' ')
print('  ', end='')
print(dashes)
print('  ', end='')

for x in range(len(carryLst)- 1, -1, -1):
    print(carryLst[x], end='')
# 192








