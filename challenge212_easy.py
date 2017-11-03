''' When we Swedes are young, we are taught a SUPER-SECRET language
 that only kids know, so we can hide secrets from our confused parents.
 This language is known as "Rövarspråket" (which means "Robber's language",
 more or less), and is surprisingly easy to become fluent in, at least
 when you're a kid. Recently, the cheeky residents of /r/Sweden decided
 to play a trick on the rest on reddit, and get a thread entirely in
 Rövarspråket to /r/all. The results were hilarious.

Rövarspråket is not very complicated: you take an ordinary word and
replace the consonants with the consonant doubled and with an "o" in
between. So the consonant "b" is replaced by "bob", "r" is replaced
with "ror", "s" is replaced with "sos", and so on. Vowels are left intact.
It's made for Swedish, but it works just as well in English.

Your task today is to write a program that can encode a string of text
into Rövarspråket.

(note: this is a higly guarded Swedish state secret, so I trust that none
of you will share this very privileged information with anyone! If you do,
you will be extradited to Sweden and be forced to eat surströmming as penance.)

(note 2: surströmming is actually not that bad, it's much tastier than its
reputation would suggest! I'd go so far as to say that it's the tastiest
half-rotten fish in the world!)

Formal inputs & outputs
Input

You will receive one line of input, which is a text string
that should be encoded into Rövarspråket.
Output

The output will be the encoded string.

A few notes: your program should be able to handle case properly, which means that
"Hello" should be encoded to "Hohelollolo", and not as "HoHelollolo" (note the
second capital "H").

Also, since Rövarspråket is a Swedish invention, your program should follow Swedish
rules regarding what is a vowel and what is a consonant. The Swedish alphabet is
the same as the English alphabet except that there are three extra characters at
the end (Å, Ä and Ö) which are all vowels. In addition, Y is always a vowel in Swedish,
so the full list of vowels in Swedish is A, E, I, O, U, Y, Å, Ä and .Ö The rest are consonants.

Lastly, any character that is not a vowel or a consonant (i.e. things like punctuation)
should be left intact in the output.

Jag talar Rövarspråket!

Output 1

Jojagog totalolaror Rorövovarorsospoproråkoketot!

Input 2

I'm speaking Robber's language!

Output 2

I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!

Challenge inputs
Input 1

Tre Kronor är världens bästa ishockeylag.

Input 2

Vår kung är coolare än er kung.
'''

def Rovarspraket(strng):
    vowels =['a', 'e', 'i', 'o', 'u', 'y', 'Å', 'Ä', 'Ö']
    output = ''
    for word in strng:
        for x in range(0, len(word)):
            if word[x] in vowels or not word[x].isalnum():
                output += word[x]
                continue
            else:
                replacement = word[x] + 'o' + word[x].lower()
                output += replacement
    return output


if __name__ == '__main__':
    test = "erb'l"
    test = "erb'l"
    ans = Rovarspraket(test)
    print(ans)


    swede_speak = "Jag talar Rövarspråket!"
    ans = Rovarspraket(swede_speak)
    print(ans)

    swede_speak2 = "I'm speaking Robber's language!"
    ans = Rovarspraket(swede_speak2)
    print(ans)

    swede_speak3 = "Tre Kronor är världens bästa ishockeylag."
    ans = Rovarspraket(swede_speak3)
    print(ans)

    swede_speak4 = "Vår kung är coolare än er kung."
    ans = Rovarspraket(swede_speak4)
    print(ans)



