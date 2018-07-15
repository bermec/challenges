'''
It's the year 2095. In an interesting turn of events, it was decided 50 years ago that BASIC is by far the universally best language. You work for a company by the name of SpaceCorp, who has recently merged with a much smaller company MixCo. While SpaceCorp has rigorous formatting guidelines, exactly 4 space per level of indentation, MixCo developers seem to format however they please at the moment. Your job is to bring MixCo's development projects up to standards.
Input Description

You'll be given a number N, representing the number of lines of BASIC code.
Following that will be a line containing the text to use for indentation,
which will be ···· for the purposes of visibility. Finally, there will be
N lines of pseudocode mixing indentation types (space and tab, represented
by · and » for visibility) that need to be reindented.

Blocks are denoted by IF and ENDIF, as well as FOR and NEXT.
Output Description

You should output the BASIC indented by SpaceCorp guidelines.
Challenge Input

12
····
VAR I
·FOR I=1 TO 31
»»»»IF !(I MOD 3) THEN
··PRINT "FIZZ"
··»»ENDIF
»»»»····IF !(I MOD 5) THEN
»»»»··PRINT "BUZZ"
··»»»»»»ENDIF
»»»»IF (I MOD 3) && (I MOD 5) THEN
······PRINT "FIZZBUZZ"
··»»ENDIF
»»»»·NEXT

Challenge Output

VAR I
FOR I=1 TO 31
····IF !(I MOD 3) THEN
········PRINT "FIZZ"
····ENDIF
····IF !(I MOD 5) THEN
········PRINT "BUZZ"
····ENDIF
····IF (I MOD 3) && (I MOD 5) THEN
········PRINT "FIZZBUZZ"
····ENDIF
NEXT

Bonus

Give an error code for mismatched or missing statements.
For example, this has a missing ENDIF:

FOR I=0 TO 10
····IF I MOD 2 THEN
········PRINT I
NEXT

This has a missing ENDIF and a missing NEXT:

FOR I=0 TO 10
····IF I MOD 2 THEN
········PRINT I

This has an ENDIF with no IF and a FOR with no NEXT:

FOR I=0 TO 10
····PRINT I
ENDIF

This has an extra ENDIF:

FOR I=0 TO 10
····PRINT I
NEXT
ENDIF
'''

prog = '''····
VAR I
·FOR I=1 TO 31
»»»»IF !(I MOD 3) THEN
··PRINT "FIZZ"
··»»ENDIF
»»»»····IF !(I MOD 5) THEN
»»»»··PRINT "BUZZ"
··»»»»»»ENDIF
»»»»IF (I MOD 3) && (I MOD 5) THEN
······PRINT "FIZZBUZZ"
··»»ENDIF
»»»»·NEXT
'''

import re
a = '....'

def program_check(prog, d):

    results = []
    prog = prog.splitlines()
    prog_string = ''
    for strng in prog:
        prog_string += strng + ' '
    prog = re.findall(r'[A-Z]+', prog_string)
    for word in prog:
        try:
            dict_val = d[word]
        except:
            continue
        if d[word] in prog:
            prog.remove(word)
            prog.remove(dict_val)
        else:
            results.append(dict_val)
    return display(results)


def display(l):
    if len(l) == 1:
        return 'Missing ' + l[0]
    else:
        return 'Missing ' + l[0] + ' and ' + l[1]


prog = prog.splitlines()
for line in prog:
    select = re.findall(r'[A-Z].*', line)
    try:
        select = select[0]
    except IndexError:
        continue
    if  select.startswith('I') or select.startswith('E'):
        print(a + select)
    elif select.startswith('P'):
        print(a * 2 + select)
    else:
        print(select)



words = {'FOR': 'NEXT',
         'NEXT': 'FOR',
         'IF': 'ENDIF',
         'ENDIF': 'IF'}

prog = '''FOR I=0 TO 10
····IF I MOD 2 THEN
········PRINT I
NEXT
'''

prog2 ='''FOR I=0 TO 10
····IF I MOD 2 THEN
········PRINT I'''

prog3 = '''FOR I=0 TO 10
····PRINT I
ENDIF'''

prog4 = '''FOR I=0 TO 10
····PRINT I
NEXT
ENDIF'''



ans = program_check(prog, words)
print(ans)

ans = program_check(prog2, words)
print(ans)

ans = program_check(prog3, words)
print(ans)

ans = program_check(prog4, words)
print(ans)





