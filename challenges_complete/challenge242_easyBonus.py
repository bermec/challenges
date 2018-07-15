''' The subject rule for this challenge, Rule 90, is one of the simplest,
a simple neighbor XOR. That is, in a 1 dimensional CA system
(e.g. a line), the next state for the cell in the middle of 3 is
simply the result of the XOR of its left and right neighbors.
E.g. "000" becomes "1" "0" in the next state, "100" becomes "1"
in the next state and so on. You traverse the given line in windows
of 3 cells and calculate the rule for the next iteration of the
following row's center cell based on the current one while the
two outer cells are influenced by their respective neighbors.
Here are the rules showing the conversion from one set of cells to another:
"111" 	"101" 	"010" 	"000" 	"110" 	"100" 	"011" 	"001"
0 	0 	0 	0 	1 	1 	1 	1
Input Description

You'll be given an input line as a series of 0s and 1s. Example:

1101010

Output Description

Your program should emit the states of the celular automata for 25 steps.
Example from above, in this case I replaced 0 with a blank and a 1 with an X:

xx x x
xx    x
xxx  x
x xxx x
  x x
 x   x

'''

def rule90(str):
    str_out = ''

    for x in range(0, len(str)):
        # check first in string
        if x == 0:
            str_out += str[1]
        else:
            try:
                if str[x - 1] != str[x+1]:
                    str_out += 'x'
                else:
                    str_out += ' '
            except IndexError:
                # set last in string
                str_out += str[-2]
    return str_out

if __name__ == '__main__':
    instr = '00000000000000000000000000000000000000000000000001' \
            '000000000000000000000000000000000000000000000000'
    first_line = ''
    for x in range(0, len(instr)):
        chk = instr[x]
        if instr[x] == '0':
            first_line += ' '
        else:
            first_line += 'x'
    print(first_line)

    acc = 0
    ans = rule90(first_line)
    print(ans)

    while acc <= 20:
        ans = rule90(ans)
        print(ans)
        acc += 1