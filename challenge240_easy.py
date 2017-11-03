''' Typoglycemia is a relatively new word given to a purported recent discovery
about how people read written text. As wikipedia puts it:

    The legend, propagated by email and message boards, purportedly demonstrates
    that readers can understand the meaning of words in a sentence even when the
    interior letters of each word are scrambled. As long as all the necessary letters
    are present, and the first and last letters remain the same, readers appear to
    have little trouble reading the text.

Or as Urban Dictionary puts it:

    Typoglycemia
    The mind's ability to decipher a mis-spelled word if the first and last
    letters of the word are correct.

    The word Typoglycemia describes Teh mdin's atbiliy to dpeihecr a msi-selpeld
    wrod if the fsirt and lsat lteetrs of the wrod are cerorct.

Input Description

Any string of words with/without punctuation.
Output Description

A scrambled form of the same sentence but with the word's first and last
letter's positions intact.'''

from random import randrange


def sattoloCycle(items):
    ''' str -> str
    shuffle a string'''
    apos = ''

    items = list(items)
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    item_string = ''
    for item in items:
        item_string += item

    return item_string


if __name__ == '__main__':



    with open('challenge240.txt') as f:
        while True:
            txt = f.readline()
            # detect end of text
            if len(txt) == 0:
                break
            output = ''
            out_string = ''
            comma_index = 0
            index = 0

            txt.split()
            for word in txt.split():
                new_word = word
                if len(word) > 3:
                    pre_shuffle = word

                    if "'" in word:
                        # find index of any ' character
                        index = word.find("'")
                        pre_shuffle = word.replace("'", '')

                    # note start and end characters
                    start_char = word[0]
                    if "." in word or "," in word:
                        last_char = word[-2:]
                    else:
                        last_char =word[-1]


                    # strip off first and last characters
                    if "," in word or "." in word:
                        to_shuffle = pre_shuffle[1:-2]
                    else:
                        to_shuffle = pre_shuffle[1:-1]

                    # shuffle  the resulting string
                    new_word = sattoloCycle(to_shuffle)
                    output = start_char + new_word + last_char

                    # replace apostrophe if present
                    if "'" in word:
                        output2 = output[:index] + word[index] + output[index:]
                        output = output2


                    out_string = out_string + output + ' '


                else:
                    out_string = out_string + word + ' '
            print(out_string)
