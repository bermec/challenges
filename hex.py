# Convert Decimal to Hexadecimal.

#hexlist = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

input_decimal = int(input("Enter a decimal integer:"))


division = input_decimal // 16
remainder = 0
remainderlist = []

print("Division", division, "Remainder", remainder)

for num in range(division+1):
    division = division // 16
    remainder = division % 16
    remainderlist.append(remainder)
    print("Division", division,'\tRemainder', remainder)
    if division == 0 and remainder == 0:
        break