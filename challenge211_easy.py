''' Description

If computer programmers had a "patron musician" (if such a thing even exists),
it would surely be the great Shirley Ellis. It is my opinion that in the
history of music, not song has ever come closer to replicating the experience
of programming as her 1964 novelty hit The Name Game. In the lyrics of that
song she lays out quite an elegant and fun algorithm for making a rhyme out
of anybody's name. The lyrics are almost like sung pseudo-code!

Your challenge today will be to implement a computer program that can play
Ms. Ellis' Name Game. You will receive a name for input,
and output the rhyme for that name.

It should be noted that while the rhyming algorithm is very elegant
and easy for humans to follow, Ms. Ellis description is not quite
rigorous. For instance, there's an extra rule that she doesn't mention
that only applies when names start with a vowel (such as "Arnold"),
and it's not quite clear exactly what you should do when the names
start with M, F or B. You will have to fill in the blanks as best you
can on your own. If you're not sure how a specific rule goes,
implement what sounds best to you.

You should primarily refer to the song for instructions,
but I've included the relevant lyrics here:

    Come on everybody!
    I say now let's play a game
    I betcha I can make a rhyme out of anybody's name

    The first letter of the name, I treat it like it wasn't there
    But a "B" or an "F" or an "M" will appear
    And then I say "bo", add a "B", then I say the name
    and "Bonana fanna" and a "fo"

    And then I say the name again with an "F" very plain
    and a "fee fy" and a "mo"
    And then I say the name again with an "M" this time
    and there isn't any name that I can't rhyme

    But if the first two letters are ever the same,
    I drop them both and say the name like

    Bob, Bob drop the B's "Bo-ob"
    For Fred, Fred drop the F's "Fo-red"
    For Mary, Mary drop the M's Mo-ary
    That's the only rule that is contrary.

Formal Inputs & Outputs
Input description

Your input will be a single line with a single name on it.
Note that in all the excitement, an exclamation point has
been added to the end.
Output description

The rhyme of the name!
Example Inputs & Outputs

Examples helpfully provided by Ms. Ellis herself.
Example 1

Lincoln!

Output 1

Lincoln, Lincoln bo Bincoln,
Bonana fanna fo Fincoln,
Fee fy mo Mincoln,
Lincoln!

Example 2

Nick!

Output 2

Nick, Nick bo Bick,
Bonana fanna fo Fick,
Fee fy mo Mick,
Nick!

Challenge input
Input 1

Arnold!

Input 2

Billy!

Input 3

Your username! etc
'''

candidates = ['Arnold', 'Billy', 'Roger']
capB = 'B'
capF = 'F'
capM = 'M'
exceptionList = ['A', 'E', 'I', 'O', 'U']
starts =['M', 'B', 'F']


for candidate in candidates:
    if candidate.startswith(('B', 'G', 'F')):
        firstPhrase = candidate + ', ' + candidate + ', ' + candidate[0] + 'o-' + candidate[1:] + ','
        secondPhrase = "Bonana fanna fo " + capF + candidate[1:] + ','
        thirdPhrase = "Fee fi mo " + capM + candidate[1:] + ','
        last = candidate + '!'

    elif candidate[0] in exceptionList:
        firstPhrase = candidate + ', ' + candidate + ' bo ' + capB + candidate.lower() + ','
        secondPhrase = "Bonana fanna fo " + capF + candidate.lower() + ','
        thirdPhrase = "Fee fi mo " + capM + candidate.lower() + ','
        last = candidate + '!'
    else:
        firstPhrase = candidate + ', ' + candidate + ' bo ' + capB + candidate[1:] + ','
        secondPhrase = "Bonana fanna fo " + capF + candidate[1:] + ','
        thirdPhrase = "Fee fi mo " + capM + candidate[1:] + ','
        last = candidate + '!'


    print("%s\n%s\n%s\n%s" % (firstPhrase, secondPhrase, thirdPhrase, last))