
ones = ["one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]

def substring(n):
    strng = ''
    # slice for multiple of tens
    int_n = int(n[1:3])
    # slice for multiples of hundreds
    hund = int(n[0])
    if hund == 0:
        strng += ' and '
    elif hund > 0:
        strng += ' ' + ones[hund - 1] + ' hundred and '

    if int_n <= 19:
        strng += ones[int_n - 1]
    else:
        str_n = str(int_n)
        dec = int(str_n[0])
        strng += tens[dec - 2]
        digit = int(str_n[1])
        # pass if a zero
        if digit == 0:
            pass
        # add the final digit
        else:
            strng += ' ' + ones[digit - 1]
    return strng

if __name__ == '__main__':

    num = '9'
    num = num.zfill(3)
    ans = substring(num)
    print(ans)


