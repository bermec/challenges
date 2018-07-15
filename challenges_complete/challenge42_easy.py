''' Write a program that prints out the lyrics for "Ninety-nine bottles of beer",
"Old McDonald had a farm" or "12 days of Christmas".

If you choose "Ninety-nine bottles of beer", you need to spell out the number,
not just write the digits down. It's "Ninety-nine bottles of beer on the wall",
not "99 bottles of beer"!

For Old McDonald, you need to include at least 6 animals: a cow, a chicken, a turkey,
a kangaroo, a T-Rex and an animal of your choosing (Old McDonald has a weird farm).
The cow goes "moo", the chicken goes "cluck", the turkey goes "gobble", the kangaroo
goes "g'day mate" and the T-Rex goes "GAAAAARGH". You can have more animals if you like.

Make your code shorter than the song it prints out!

'''

cap_tens = ['Ninety', 'Eighty', 'Seventy', 'Sixty', 'Fifty', 'Forty', 'Thirty', 'Twenty']
lo_tens = ['ninety', 'eighty', 'seventy', 'sixty', 'fifty', 'forty', 'thirty', 'twenty']
teens = ['Nineteen', 'Eighteen', 'Seventeen', 'Sixteen', 'Fifteen', 'Fourteen', 'Thirteen', 'Twelve', 'Eleven', 'Ten' ]

digits = ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', '']
digits2 = ['Nine bottles', 'Eight bottles', 'Seven bottles', 'Six bottles', 'Five bottles', 'Four bottles',
           'Three bottles', 'Two bottles', 'One bottle', 'no bottles']
nineteen = ['nineteen']

#-- ninety nine to twenty -----------------------------
for x in range(0, len(cap_tens)):
    for y in range(0, len(digits)):
        stock = cap_tens[x] + '-' + digits[y]

        if  x == 7 and y == 9:
            loss = nineteen[0]
        elif y == 9:
            stock = cap_tens[x]
            loss = lo_tens[x + 1] + '-' + digits[0]
        elif  y == 8:
            loss = lo_tens[x]
        elif y == 9:
            loss = lo_tens[x * 1] + '-' + digits[0]

        else:
            loss = lo_tens[x] + '-' + digits[y + 1]
        print(stock + ' bottles of beer on the wall. ' + stock + ' bottles of beer.')
        print('Take one down, pass it around, ' + loss + ' bottles of beer on the wall.')
        print()

#-- nineteen to ten -------------------------------
for x in range(0, len(teens)):
    stock = teens[x]
    if x == 9:
        loss = digits[0]
    else:
        loss = teens[x + 1]
    print(stock + ' bottles of beer on the wall. ' + stock + ' bottles of beer.')
    print('Take one down, pass it around, ' + loss + ' bottles of beer on the wall.')
    print()
#  nine to zero -----------------------------------
for x in range(0, len(digits2)):
    stock = digits2[x]
    if x == 9:
        loss = digits[0]
    else:
        loss = digits2[x + 1]
    print(stock + ' of beer on the wall. ' + stock + '  of beer.')
    print('Take one down, pass it around, ' + loss + ' of beer on the wall.')
    if loss == digits2[9]:
        exit()
    print()


