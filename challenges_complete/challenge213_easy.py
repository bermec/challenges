''' The HBO network show "Silicon Valley" has introduced a way to pronounce hex.

Kid: Here it is: Bit… soup. It’s like alphabet soup, BUT… it’s ones and zeros instead of letters.
Bachman: {silence}
Kid: ‘Cause it’s binary? You know, binary’s just ones and zeroes.
Bachman: Yeah, I know what binary is. Jesus Christ, I memorized the hexadecimal
                    times tables when I was fourteen writing machine code. Okay? Ask me
                    what nine times F is. It’s fleventy-five. I don’t need you to tell me what
                    binary is.

Not "eff five", fleventy. 0xF0 is now fleventy. Awesome.
Above a full byte you add "bitey" to the name. The hexidecimal pronunciation rules:
HEX PLACE VALUE 	WORD
0xA0 	“Atta”
0xB0 	“Bibbity”
0xC0 	“City”
0xD0 	“Dickety”
0xE0 	“Ebbity”
0xF0 	“Fleventy”
0xA000 	"Atta-bitey"
0xB000 	"Bibbity-bitey"
0xC000 	"City-bitey"
0xD000 	"Dickety-bitey"
0xE000 	"Ebbity-bitey"
0xF000 	"Fleventy-bitey"

Combinations like 0xABCD are then spelled out "atta-bee bitey city-dee".

For this challenge you'll be given some hex strings and asked to pronounce them.
Input Description

You'll be given a list of hex values, one per line. Examples:

0xF5
0xB3
0xE4
0xBBBB
0xA0C9

Output Description

Your program should emit the pronounced hex. Examples from above:

0xF5 "fleventy-five"
0xB3 “bibbity-three”
0xE4 “ebbity-four”
0xBBBB “bibbity-bee bitey bibbity-bee”
0xA0C9 “atta-bitey city-nine”



0xA0 	'Atta'
0xB0 	'Bibbity'
0xC0 	'City'
0xD0 	“Dickety”
0xE0 	“Ebbity”
0xF0 	“Fleventy”
0xA000 	"Atta-bitey"
0xB000 	"Bibbity-bitey"
0xC000 	"City-bitey"
0xD000 	"Dickety-bitey"
0xE000 	"Ebbity-bitey"
0xF000 	"Fleventy-bitey"
'''

first_digit ={'A':'atta', 'B':'bibbity', 'C': 'city', 'D':'dickety', 'E':'ebbity', 'F':'fleventy'}
digits = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight',
          '9':'nine', 'A':'ay', 'B':'bee', 'C':'cee', 'D':'dee', 'E':'eee', 'F':'eff'}
bitey = 'bitey'
num_list = ['0xF5', '0xB3', '0xE4', '0xBBBB', '0xA0C9']
flag = True

for x in range(0, len(num_list)):
    flag = True
    output = ''
    candidate = num_list[x]
    first_candidate = candidate[2:4]
    second_candidate = candidate[4:]
    header = first_digit[first_candidate[0]]
    try:
        digit = digits[first_candidate[1]]
    except KeyError:
        flag = False
        pass
    if flag:
        output += header + '-'
        output += digit
    else:
        output += header + '-'

    if len(num_list[x]) > 4:
        if flag:
            output += ' ' + bitey
        else:
            output += bitey
        third_candidate = candidate[4:5]
        fourth_candidate = candidate[5:6]
        second_header = first_digit[third_candidate]
        second_digit = digits[fourth_candidate]
        output += ' ' + second_header + '-' + second_digit

    print(output)

