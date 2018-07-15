'''
One of the most annoying and confusing differences between English and basically every other language
in the world is that English uses a weird way to name very large numbers.

For instance, if you wanted to translate "one trillion" from English to French, you might think it
would be "un trillion", but that is wrong. The correct translation of "one trillion" to French is
"un billion". Well, then, you might ask, what is "one billion" in French? It is, in fact, "un milliard".
And "un trillion" in French is equal to english "one quintillion". Confusing, no?

The reason for this is that there are two so-called scales for large numbers, the long scale and the
short scale. English uses the short scale, almost everyone else uses the long scale (though the Arabic
languages also apparently use the short scale). The two systems can be summarized as follows:

    In the short scale, you get a "new word" for the numbers every time the number increases by a factor
    of 1,000. So "a thousand millions" is "one billion" and "a thousand billions" is "one trillion".

    In the long scale, you get a "new word" for the numbers every time the number increases by a factor
    of 1,000,000. So "a million millions" is the same as "one billion" and "a million billions" is the
    same as "one trillion". If we just increase by a factor of 1,000, the "-on" ending on the word is
    replaced by "-ard". So "a thousand millions" is "one milliard", "a thousand billions" is "one billiard".

Here's a table summarizing the words for different numbers:
Actual number 	Short scale name 	Long scale name
106 	million 	million
109 	billion 	milliard
1012 	trillion 	billion
1015 	quadrillion 	billiard
1018 	quintillion 	trillion
1021 	sextillion 	trilliard

And it goes on like that.

Your task today is to write a program that will print out the name of a number in both long-scale and
short-scale. So, for instance, given 1234567891111, it should print out

Short scale: 1 trillion, 234 billion, 567 million, 891 thousand and 111
Long scale:  1 billion, 234 milliard, 567 million, 891 thousand and 111

Bonus points if it prints out everything in letters, i.e.:

Short scale: one trillion, two hundred and thirty-four billion, five hundred
and sixty-seven million, eight hundred and ninety-one thousand and one
hundred and eleven

Long scale:  one billion, two hundred and thirty-four milliard, five hundred
and sixty-seven million, eight hundred and ninety-one thousand and one
hundred and eleven

The program should be able to handle all numbers that can fit into an unsigned 64-bit integers,
i.e. all numbers up to 264 - 1 ("18 trillion, 446 billiard, 744 billion, 73 milliard, 709 million,
551 thousand and 615" in long scale, though it's something completely different in short scale.),
or 263 - 1 if you're using signed 64-bit integers. Of course, you can write your program so it can
handle bigger numbers if you want, but it's not necessary.

'''

ones = ["one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
hundred = 'hundred'
english = [" thousand,", "million,", "billion,",
        "trillion,", "quadrillion,", "quintillion,", "sextillion,"]
french = ["thousand,", "million,", "milliard,",
        "billion,", "billiard,", "trillion,", "trilliard,"]
plus = 'and'

def decode_short(num):
    ones_slice = num[-2:]
    tens_slice = num[-2:-1]
    hundred_slice = num[-3:-2]
    thou_slice = num[-6:-3]
    mill_slice = num[-9:-6]
    bill_slice = num[-12:-9]
    trillion_slice = num[-15:-12]
    string_num = ''
    flag = 0
    if trillion_slice == '':
        pass
    else:
        trillion_slice = trillion_slice.zfill(3)
        trillion_slice = sub_decode(bill_slice, flag)
        string_num += ' ' + trillion_slice + ' trillion'
        flag = 1
    if bill_slice == '':
        pass
    else:
        bill_slice = bill_slice.zfill(3)
        bill_slice = sub_decode(bill_slice, flag)
        string_num += ' ' + bill_slice + ' billion'
        flag = 1

    if mill_slice == ''or mill_slice == '000':
        pass
    else:
        mill_slice = mill_slice.zfill(3)
        mill_slice = sub_decode(mill_slice, flag)
        string_num += ' ' + mill_slice + ' million'
        flag = 1

    if thou_slice == '' or thou_slice == '000':
        pass
    else:
        thou_slice = thou_slice.zfill(3)
        thou_slice = sub_decode(thou_slice, flag)
        string_num += ' ' + thou_slice + english[0]
        flag = 1

    if hundred_slice == '' or hundred_slice == '0':
        if string_num == '':
            pass
        else:
            string_num += ' and'

    else:
        hundred_slice = hundred_slice.zfill(3)
        hundred_slice = sub_decode(hundred_slice, flag)
        string_num += ' ' + hundred_slice + ' hundred  and '
        flag = 1

    if tens_slice == '0' or tens_slice == '':
        pass
    elif tens_slice[0] == 1:
        pass
    else:
        string_num += ' ' + tens[int(tens_slice) - 2]
        flag = 1

    if ones_slice == '':
        pass
    else:
        if int(ones_slice) > 19:
            ones_slice = num[-1]
        ones_slice = ones_slice.zfill(2)
        ones_slice = sub_decode(ones_slice, flag)
        string_num += ' ' + ones_slice
        flag = 1

    return string_num

def sub_decode(n, flag):
    n = str(n)
    strng = ''
    # slice for multiple of tens
    try:
        int_n = int(n[1:3])
    except:
        int_n = 0


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
    num = 11
    num = str(num)
    ans = decode_short(num)
    print(ans)



